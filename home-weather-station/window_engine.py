from evaluator import deg_to_direction


def assign_roles(windows, side_map, wind_deg):
    inlet = []
    exhaust = []
    closed = []

    wind_dir = deg_to_direction(wind_deg)

    # Classify windows
    good_windows = [w for w in windows if side_map[w.side] == "GOOD"]
    neutral_windows = [w for w in windows if side_map[w.side] == "NEUTRAL"]
    weak_windows = [w for w in windows if side_map[w.side] == "WEAK"]

    # ✅ Step 1: Choose INLET (wind-driven)
    wind_windows = [w for w in good_windows if w.side == wind_dir]

    if wind_windows:
        inlet = wind_windows[:1]  # strong directional airflow
    elif good_windows:
        inlet = good_windows[:1]
    elif neutral_windows:
        inlet = neutral_windows[:1]
    elif weak_windows:
        inlet = weak_windows[:1]

    # Helper: opposite side
    def opposite(side):
        return {
            "NORTH": "SOUTH",
            "SOUTH": "NORTH",
            "EAST": "WEST",
            "WEST": "EAST"
        }[side]

    # ✅ Step 2: Choose ONE exhaust (opposite side)
    exhaust_side = None
    if inlet:
        exhaust_side = opposite(inlet[0].side)

    for w in windows:
        if exhaust_side and w.side == exhaust_side:
            exhaust.append(w)
            break  # only ONE exhaust

    # ✅ Step 3: Everything else CLOSED
    for w in windows:
        if w not in inlet and w not in exhaust:
            closed.append(w)

    return inlet, exhaust, closed