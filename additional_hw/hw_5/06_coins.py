def get_change(value, coins):
    """
    Return the amount and denominations of coins to get change
    :param value: sum to change
    :param coins: available coins to change
    :return: dictionary keys = coins value, dictionary values = coins nominal
    """
    change_dict = {}

    for coin in sorted(map(int, coins.split(", ")), reverse=True):
        change_dict[coin] = value//coin
        value -= value//coin * coin
    return change_dict


value_to_change = int(input("Input money amount : "))
coins_available = input("Input coins available: ")

print(get_change(value_to_change, coins_available))
