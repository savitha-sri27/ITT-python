from itertools import permutations

s, k = input().split()

perms = list(permutations(sorted(s), int(k)))

for p in perms:
    print(''.join(p))