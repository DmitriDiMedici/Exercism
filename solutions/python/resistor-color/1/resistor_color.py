def color_code(color):
    value = [0,1,2,3,4,5,6,7,8,9]
    paired = dict(zip(colors(), value))
    return paired[color]



def colors():
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
