def value(colors):
    if len(colors) > 2:
        colors = colors[:-1]
    vals = [color_stripes().index(x) for x in colors if x in color_stripes()]
    number = "".join(map(str, vals))
    return int(number)


def color_stripes():
    colors_available = [
        "black",
        "brown",
        "red",
        "orange",
        "yellow",
        "green",
        "blue",
        "violet",
        "grey",
        "white",
    ]
    return colors_available

