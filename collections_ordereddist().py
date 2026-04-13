from collections import OrderedDict
n = int(input())
item_dict = OrderedDict()

for _ in range(n):
    data = input().split()
    item_name = " ".join(data[:-1])
    price = int(data[-1])
    item_dict[item_name] = item_dict.get(item_name, 0) + price
for item, net_price in item_dict.items():
    print(item, net_price)
