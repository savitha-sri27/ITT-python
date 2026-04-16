import re
import email.utils
n = int(input())
pattern = r'^[a-zA-Z][a-zA-Z0-9._-]*@[a-zA-Z]+\.[a-zA-Z]{1,3}$'

for _ in range(n):
    raw_input = input()
    name, addr = email.utils.parseaddr(raw_input)
    if re.match(pattern, addr):
        print(email.utils.formataddr((name, addr)))
