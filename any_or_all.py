n = int(input())
numbers = input().split()
print(all(int(i) > 0 for i in numbers) and any(i == i[::-1] for i in numbers))
