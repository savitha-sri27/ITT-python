import re
import sys

def replace_symbols():
    n = int(input())
    
    for _ in range(n):
        line = sys.stdin.readline().rstrip('\n')
        line = re.sub(r"(?<= )&&(?= )", "and", line)
        line = re.sub(r"(?<= )\|\|(?= )", "or", line)
        
        print(line)

if __name__ == '__main__':
    replace_symbols()
