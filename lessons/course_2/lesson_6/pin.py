def check_pin(pin):
    """
    Check that PIN is 4 digits
    :param pin: digits
    :return: False or True
    """
    if not pin.isdigit():
        return False
    if len(pin) != 4:
        return False
    return True


