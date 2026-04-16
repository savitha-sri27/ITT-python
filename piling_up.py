from collections import deque

def can_stack(cubes):

    d = deque(cubes)
 
    last_picked = float('inf')
    
    while d:
        if d[0] >= d[-1]:
            current = d.popleft()
        else:
            current = d.pop()
            

        if current > last_picked:
            return "No"
        
        last_picked = current
        
    return "Yes"

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        cubes = list(map(int, input().split()))
        print(can_stack(cubes))
