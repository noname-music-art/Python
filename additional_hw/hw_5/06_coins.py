amount = int(input("Input sum : "))
coins = input("Input coins : ")
coins_dict = {}

for coin in sorted(map(int, coins.split(", ")), reverse=True):
    coins_dict[coin] = amount//coin
    amount -= amount//coin * coin

print(coins_dict)

# def lost_time(*values):
#   sum = 0
#   for value in values:
#     sum += value
#   return(sum)
