from itertools import product

def solve():
   
    k, m = map(int, input().split())
    
    
    lists = []
    for _ in range(k):
        row = list(map(int, input().split()))[1:]
        lists.append([x**2 for x in row])
    max_val = 0
    for combination in product(*lists):
        current_sum = sum(combination) % m
        if current_sum > max_val:
            max_val = current_sum
            
    print(max_val)

if __name__ == "__main__":
    solve()
