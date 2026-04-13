import re
t_str = raw_input()
t = int(t_str)

for _ in range(t):
    s = raw_input()
    try:
        re.compile(s)
        print "True"
    except re.error:
        print "False"