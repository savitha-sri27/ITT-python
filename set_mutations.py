n = int(input())
storage = set(map(int, input().split()))
num_ops = int(input())

for _ in range(num_ops):
    operation_name, _ = input().split()
    other_set = set(map(int, input().split()))
    getattr(storage, operation_name)(other_set)
print(sum(storage))
