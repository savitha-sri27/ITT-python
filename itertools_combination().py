from itertools import combinations
s, k = input().split()
k = int(k)
sorted_s = sorted(s)
for i in range(1, k + 1):
    current_combinations = list(combinations(sorted_s, i))
    for combo in current_combinations:
        print("".join(combo))