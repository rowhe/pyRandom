"""
Backup perforce shelves and commits.

Usage:
    p4_backup [options] write_commits --output-dir=PATH
    p4_backup [options] backup_shelves --output-dir=PATH
    p4_backup [options] backup_commits --output-dir=PATH

Options:
    --p4port=ADDRESS:PORT       Perforce server and port [default: p4.saber3d.net:1666]
    --p4user=USER               Perforce user
    --p4workspace=WORKSPACE     Perforce workspace
    -h --help                   Show this screen.
"""
import csv
import os
from docopt import docopt

from saber.lib.io import write_json_file
from saber.lib.perforce import parse_options_and_create_p4, PerforceClient


def write_commits(p4: PerforceClient, change_type: str, *, count: int, output_file: str):
    lst = p4.run_impl('changes', '-m', count, '-s', change_type)

    fields = set()
    for p in lst:
        fields |= set(p.keys())

    with open(output_file, 'w') as f:
        wr = csv.DictWriter(f, fieldnames=list(fields))
        wr.writeheader()
        wr.writerows(lst)


def write_text_file(path, data):
    os.makedirs(os.path.dirname(path), exist_ok=True)

    with open(path, 'w', encoding='utf8') as f:
        f.write(data)


BROKEN_CHANGELIST = {
    '11241215',
    '11237950',
}


def backup_shelves(p4: PerforceClient, *, output_dir: str):
    data = read_csv(os.path.join(output_dir, 'shelves.csv'))

    for p in data:
        change, user = p['change'], p['user']
        if user.startswith('swarm') or user == 'builder':
            continue

        shelve_dir = os.path.join(output_dir, 'shelves', change)
        if os.path.exists(shelve_dir):
            continue

        if change in BROKEN_CHANGELIST:
            continue

        print(f"{change} {user}")
        desc = p4.describe_changelist(change, shelved=True)[0]
        print(f"{len(desc['depotFile'])} files")
        # if len(desc['depotFile']) > 1000:
        #     print(f"  too many files, skipping for now...")
        #     continue

        desc_path = os.path.join(shelve_dir, '_desc.json')
        write_json_file(desc_path, desc, indent=2)

        for depot_file, tp in zip(desc['depotFile'], desc['type']):
            if tp.startswith('binary'):
                continue

            print(f"  {tp} {depot_file}")
            assert depot_file.startswith('//')
            rel_depot_file = depot_file[2:].split('/', 2)[-1]

            backup_file_path = os.path.join(shelve_dir, rel_depot_file)
            if os.path.exists(backup_file_path):
                continue

            data = p4.run_impl('print', f"{depot_file}@={change}")
            write_text_file(backup_file_path, ''.join(data[1:]))


def backup_commits(p4: PerforceClient, *, output_dir: str):
    data = read_csv(os.path.join(output_dir, 'commits.csv'))

    for p in data:
        change, user = p['change'], p['user']
        # if user.startswith('swarm') or user == 'builder':
        #     continue

        commit_dir = os.path.join(output_dir, 'commits', change)
        if os.path.exists(commit_dir):
            continue

        if change in BROKEN_CHANGELIST:
            continue

        print(f"{change} {user}")
        desc = p4.describe_changelist(change)[0]

        if 'depotFile' not in desc:
            # skip commits without files (e.g. stream changes)
            continue

        print(f"{len(desc['depotFile'])} files")
        # if len(desc['depotFile']) > 1000:
        #     print(f"  too many files, skipping for now...")
        #     continue

        desc_path = os.path.join(commit_dir, '_desc.json')
        write_json_file(desc_path, desc, indent=2)

        for depot_file, tp, rev in zip(desc['depotFile'], desc['type'], desc['rev']):
            if tp.startswith('binary'):
                continue

            if 'common/code/lib_3dpart/src' in depot_file:
                # skip such files
                continue

            print(f"  {tp} {depot_file}")
            assert depot_file.startswith('//')
            rel_depot_file = depot_file[2:].split('/', 2)[-1]

            backup_file_path = os.path.join(commit_dir, rel_depot_file)
            if os.path.exists(backup_file_path):
                continue

            data = p4.run_impl('print', f"{depot_file}#{rev}")
            write_text_file(backup_file_path, ''.join(data[1:]))


def read_csv(path: str):
    with open(path, 'r') as f:
        return list(csv.DictReader(f))


def run(opts):
    p4 = parse_options_and_create_p4(opts, perforce_is_always_enabled=True)

    if opts['write_commits']:
        write_commits(p4, 'submitted', count=1000,
                      output_file=os.path.join(opts['--output-dir'], 'commits.csv'))
        write_commits(p4, 'shelved', count=1000,
                      output_file=os.path.join(opts['--output-dir'], 'shelves.csv'))

    if opts['backup_shelves']:
        backup_shelves(p4, output_dir=opts['--output-dir'])

    if opts['backup_commits']:
        backup_commits(p4, output_dir=opts['--output-dir'])


if __name__ == '__main__':
    run(docopt(__doc__))
