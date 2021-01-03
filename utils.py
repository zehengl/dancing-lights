# https://github.com/studioimaginaire/phue/blob/master/examples/rgb_colors.py
def rgb_to_xy(red, green, blue):
    """conversion of RGB colors to CIE1931 XY colors
    Formulas implemented from: https://gist.github.com/popcorn245/30afa0f98eea1c2fd34d
    Args:
        red (float): a number between 0.0 and 1.0 representing red in the RGB space
        green (float): a number between 0.0 and 1.0 representing green in the RGB space
        blue (float): a number between 0.0 and 1.0 representing blue in the RGB space
    Returns:
        xy (list): x and y
    """

    # gamma correction
    red = pow((red + 0.055) / (1.0 + 0.055), 2.4) if red > 0.04045 else (red / 12.92)
    green = (
        pow((green + 0.055) / (1.0 + 0.055), 2.4)
        if green > 0.04045
        else (green / 12.92)
    )
    blue = (
        pow((blue + 0.055) / (1.0 + 0.055), 2.4) if blue > 0.04045 else (blue / 12.92)
    )

    # convert rgb to xyz
    x = red * 0.649926 + green * 0.103455 + blue * 0.197109
    y = red * 0.234327 + green * 0.743075 + blue * 0.022598
    z = green * 0.053077 + blue * 1.035763

    # convert xyz to xy
    x = x / (x + y + z)
    y = y / (x + y + z)

    return [x, y]
