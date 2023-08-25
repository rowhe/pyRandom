
def write_file():
    list_of_words = ["адын", "дыва", "тыри"]
    filename = "heee.txt"
    with open(filename, "a") as f:
        for word in list_of_words:
            f.write(word + "\n")

def read_file():
    filename = "heee.txt"
    with open(filename) as f:
        for line in f:
            print(line.strip())

write_file()
read_file()