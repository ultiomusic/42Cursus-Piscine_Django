def print_line(line: str):
    nodes = line.split(",")
    for node in nodes:
        print(node)

def read_number():
    n = open("numbers.txt", 'r')
    for line in n.readlines():
        print_line(line.strip())
    n.close()

if __name__ == '__main__':
    read_number()