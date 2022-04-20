def remove_from_string(string, *symbols_to_remove):

    for symbol in symbols_to_remove:
        string = string.replace(symbol, "")
    return string

