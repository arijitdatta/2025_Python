def decide_mode(indoor, outdoor):

    temp_diff = outdoor["temp"] - indoor["temp"]

    hum_diff = outdoor["humidity"] - indoor["humidity"]

    # ✅ Strong humidity advantage (very important in humid climates)

    if hum_diff <= -10:

        return "VENTILATE"

    # ✅ Moderate humidity advantage + tolerable temp increase

    if hum_diff <= -5 and temp_diff <= 2:

        return "VENTILATE"

    # ✅ Temperature advantage without humidity penalty

    if temp_diff < -0.5 and hum_diff <= 2:

        return "VENTILATE"

    return "ISOLATE"