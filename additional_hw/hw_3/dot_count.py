def pixel_count(x_res, y_res, density=1):
    """
    Function calculate ammount of pixel.

    :param x_res: number of dots in width
    :param y_res: number of dots in height
    :param density: points density
    :return: ammount of pixel
    """

    return x_res*y_res*density
