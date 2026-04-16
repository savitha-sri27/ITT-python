import re
n = int(input())
pattern = r'(?<=[: ])#([0-9a-fA-F]{6}|[0-9a-fA-F]{3})(?=[;,) ])'

for _ in range(n):
    line = input()
    matches = re.findall(pattern, line)   
    if matches:
        for m in matches:
            print(f"#{m}")
