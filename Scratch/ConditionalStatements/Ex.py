# 'price' has already been created

# Write your code here
price = 250
if price >= 300:
    discount = price * 30 / 100
elif 200 <= price < 300:
    discount = price * 20 / 100
elif 100 <= price < 200:
    discount = price * 10 / 100
elif price < 100:
    discount = price * 5 / 100
elif price < 0:
    discount = 0

price -= discount
print(price)
price = 250

if price >= 300:
    price *= 0.7  # (1 - 0.3)
elif price >= 200:
    price *= 0.8  # (1 - 0.2)
elif price >= 100:
    price *= 0.9  # (1 - 0.1)
elif 100 > price >= 0:
    price *= 0.95  # (1 - 0.05)
else:
    price

print(price)

