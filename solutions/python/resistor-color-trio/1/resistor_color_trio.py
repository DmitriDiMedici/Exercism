def label(colors):
    COLORS_AVAILABLE = [
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

    METRIC_PREFIXES = {
        0: "ohms",
        3: "kiloohms",
        6: "megaohms",
        9: "gigaohms"
    }

    # Ignore extra colors
    if len(colors) > 3:
        colors = colors[:-1]
    
    # Adding zeros
    vals = [COLORS_AVAILABLE.index(x) for x in colors[:2] if x in COLORS_AVAILABLE]
    multiplier = COLORS_AVAILABLE.index(colors[2])
    number = int("".join(map(str, vals))) * (10 ** multiplier)
    
    # Converting to metric 
    zeros = len(str(number)) - len(str(number).rstrip("0"))
    metric_zeros = (zeros // 3) * 3

    if metric_zeros == 0:
        return f"{number} ohms"

    cropped = int(number / (10 ** metric_zeros))
    unit = METRIC_PREFIXES.get(metric_zeros, "ohms")

    return f"{cropped} {unit}"

