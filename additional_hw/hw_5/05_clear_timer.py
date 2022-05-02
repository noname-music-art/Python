def clear_timer(seconds):
    """
    Get time in seconds and return as hours, minutes and seconds.
    Not return 0 hours and 0 minutes

    :param seconds: int
    :return: string (... h ... m ... s)
    """

    result = []
    hours = seconds // 3600
    minutes = (seconds // 60) % 60
    seconds = seconds % 60

    if hours:
        result.append(f'{hours}h ')
    if minutes:
        result.append(f'{minutes}m ')
    result.append(f'{seconds}s ')
    return "".join(result)


time = int(input("Input time in seconds"))
print(clear_timer(time))
