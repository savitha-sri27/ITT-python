def custom_sort(char):
    if char.islower():
        return (0, char)
    elif char.isupper():
        return (1, char)
    elif char.isdigit():
        if int(char) % 2 != 0:
            return (2, char)
        else:
            return (3, char)

if __name__ == '__main__':
    s = input()
    result = "".join(sorted(s, key=custom_sort))
    print(result)
