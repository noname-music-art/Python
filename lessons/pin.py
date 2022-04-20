def check_pin(pin):
    if pin.isdigit() and len(pin) == 4:
        return True
    else:
        return False
