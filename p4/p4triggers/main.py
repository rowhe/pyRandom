
import sys
import re

hostsfile = "hosts.txt"
logins = re.compile(r'est-.*')


def main(*args):
    user = sys.argv[1]
    print(f"Variable 1 is {user}", type(user))
    clientip = sys.argv[2]
    print(f"Variable 2 is {clientip}", type(clientip))

    if logins.match(user) and clientip in hosts():
        sys.stdout.write(f"Hello {user}\n")
        sys.stdout.write(f"User host is {clientip}\n")
        sys.exit(0)
    else:
        sys.stdout.write(f"{user} or {clientip} NOT in list\n")
        sys.exit(0)


def hosts():
    with open(hostsfile) as f:
        host_list = []
        for line in f:
            line = line.strip()
            host_list.append(line)
        # print(host_list)
    return host_list


hosts()
main(sys.argv)
