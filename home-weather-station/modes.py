def decide_mode(indoor, outdoor):
    temp_diff = outdoor["temp"] - indoor["temp"]
    hum_diff = outdoor["humidity"] - indoor["humidity"]

    # Only ventilate if clearly beneficial
    if temp_diff < -0.5 and hum_diff <= 0:
        return "VENTILATE"

    return "ISOLATE"