price = int(input())
if price > 1000:
    print(int(price * 0.9))
elif price > 500 and price <= 1000:
    print(int(price * 0.95))
else:
    print(price)
