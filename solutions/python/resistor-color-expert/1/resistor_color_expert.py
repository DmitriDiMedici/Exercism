def resistor_label(colors):
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

    TOLERANCES = {
        "grey": "0.05%",
        "violet": "0.1%",
        "blue": "0.25%",
        "green": "0.5%",
        "brown": "1%",
        "red": "2%",
        "gold": "5%",
        "silver": "10%"
    }

    vals = []
    multiplier = 0
    tolerance = ""

    # Getting values and multiplier
    if len(colors) == 1:
        return "0 ohms"

    if len(colors) == 4:
        vals = [COLORS_AVAILABLE.index(x) for x in colors[:2] if x in COLORS_AVAILABLE]
        multiplier = COLORS_AVAILABLE.index(colors[2])
        tolerance = TOLERANCES.get(colors[3])

    if len(colors) == 5:
        vals = [COLORS_AVAILABLE.index(x) for x in colors[:3] if x in COLORS_AVAILABLE]
        multiplier = COLORS_AVAILABLE.index(colors[3])
        tolerance = TOLERANCES.get(colors[4])


    number = int("".join(map(str, vals))) * (10 ** multiplier)

    # Converting to metric
    metric_str = to_metric(number)
    return f"{metric_str} ±{tolerance}"


def to_metric(value):
    METRIC_PREFIXES = [
        (1_000_000_000, "gigaohms"),
        (1_000_000, "megaohms"),
        (1_000, "kiloohms"),
        (1, "ohms")
    ]

    for factor, unit in METRIC_PREFIXES:
        if value >= factor:
            number = value / factor
            if number.is_integer():
                number = int(number)
            else:
                number = round(number,2)

            return f"{number} {unit}"


