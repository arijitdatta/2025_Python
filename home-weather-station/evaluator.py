def deg_to_direction(deg):
    if deg >= 315 or deg < 45:
        return "NORTH"
    elif deg >= 45 and deg < 135:
        return "EAST"
    elif deg >= 135 and deg < 225:
        return "SOUTH"
    else:
        return "WEST"


def classify_side(indoor, outdoor, side):
    temp_diff = outdoor["temp"] - indoor["temp"]
    hum_diff = outdoor["humidity"] - indoor["humidity"]

    # BAD air
    if temp_diff > 1 and hum_diff >= 0:
        return "BAD"

    # GOOD air
    if temp_diff < -1 or hum_diff < -5:
        return "GOOD"

    return "NEUTRAL"


def apply_wind_override(side, classification, wind_deg):
    wind_dir = deg_to_direction(wind_deg)

    if side == wind_dir and classification == "BAD":
        return "BLOCKED"

    return classification