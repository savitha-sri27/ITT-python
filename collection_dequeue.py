from collections import deque
d = deque()
n = int(input())

for _ in range(n):
    input_data = input().split()
    command = input_data[0]
    if len(input_data) > 1:
        getattr(d, command)(input_data[1])
    else:
        getattr(d, command)()
print(*(d))
