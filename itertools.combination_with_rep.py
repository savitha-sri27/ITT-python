from itertools import combinations_with_replacement
s, k = input().split()
combos = combinations_with_replacement(sorted(s), int(k))
for c in combos:
    print(''.join(c))
