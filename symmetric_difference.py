
m = int(input())
set_a = set(map(int, input().split()))

n = int(input())
set_b = set(map(int, input().split()))
sym_diff = set_a.symmetric_difference(set_b)
for val in sorted(sym_diff):
    print(val)
