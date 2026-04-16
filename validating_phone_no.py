import re
n = int(input())

for _ in range(n):
    s = input()
    if re.match(r'^[789]\d{9}$', s):
        print("YES")
    else:
        print("NO")
