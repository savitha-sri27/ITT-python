import sys

def solve():

    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])

    table = []
    for i in range(n):
        start = 2 + (i * m)
        row = list(map(int, input_data[start : start + m]))
        table.append(row)

    k = int(input_data[-1])

    table.sort(key=lambda x: x[k])
    

    for row in table:
        print(*(row))

if __name__ == "__main__":
    solve()
