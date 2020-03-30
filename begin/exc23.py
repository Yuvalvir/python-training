prices = {"banana": 10, "bread": 7, "cheese": 20, "apple": 8, "juice": 15}
shopping_cart = {"banana": 2, "bread": 3, "cheese:": 1}
pricess = prices.values()
total = 0
cart = shopping_cart.values()
for i in cart:
    for x in pricess:
        total += x * i
        break
print(total)
