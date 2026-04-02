import string

def print_rangoli(size):
    alphabet = string.ascii_lowercase
    lines = []
    for i in range(size):
        s = "-".join(alphabet[size-1:size-i-1:-1] + alphabet[size-i-1:size])
        lines.append(s.center(4 * size - 3, "-"))
    result = "\n".join(lines + lines[:-1][::-1])
    print(result)
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)