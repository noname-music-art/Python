amount = int(input("Input sum : "))
coins = input("Input coins : ")
coins_dict = {}

for coin in sorted(map(int, coins.split(", ")), reverse=True):
    coins_dict[coin] = amount//coin
    amount -= amount//coin * coin

print(coins_dict)
