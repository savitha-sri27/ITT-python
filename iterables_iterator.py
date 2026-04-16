import math
from itertools import combinations

def solve():
    n = int(input())
    letters = input().split()
    k = int(input())
    total_a = letters.count('a')
    not_a = n - total_a
    total_combinations = math.comb(n, k)
    favorable_combinations = math.comb(not_a, k)
    prob_no_a = favorable_combinations / total_combinations
    

    print(f"{1 - prob_no_a:.4f}")

if __name__ == '__main__':
    solve()
