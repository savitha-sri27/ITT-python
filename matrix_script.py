import re


n, m = map(int, input().split())


matrix = [input() for _ in range(n)]


decoded_string = "".join(["".join(column) for column in zip(*matrix)])

pattern = r'(?<=[a-zA-Z0-9])[^a-zA-Z0-9]+(?=[a-zA-Z0-9])'
final_output = re.sub(pattern, ' ', decoded_string)

print(final_output)
