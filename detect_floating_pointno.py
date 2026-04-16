import re
for _ in range(int(input())):
    s = input()
    try:
        is_float = float(s)
        print('.' in s and s[-1] != '.')
    except ValueError:
        print(False)
