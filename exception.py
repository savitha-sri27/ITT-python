t = int(input())

for _ in range(t):
    try:
        line = input().split()
        a = int(line[0])
        b = int(line[1])
        
        print(a // b)
        
    except ZeroDivisionError:
       
        print("Error Code: integer division or modulo by zero")
    except ValueError as e:
        print("Error Code:", e)