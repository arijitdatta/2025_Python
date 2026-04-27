def decide_mode(indoor, outdoor):
    # Ventilate only if outdoor is better
    if outdoor["temp"] < indoor["temp"] or outdoor["humidity"] < indoor["humidity"]:
        return "VENTILATE"

    return "ISOLATE"