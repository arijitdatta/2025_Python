def assign_roles(windows, side_map):
    inlet = []
    exhaust = []
    closed = []

    # Separate windows by classification
    good_windows = [w for w in windows if side_map[w.side] == "GOOD"]
    neutral_windows = [w for w in windows if side_map[w.side] == "NEUTRAL"]
    bad_windows = [w for w in windows if side_map[w.side] in ["BAD", "BLOCKED"]]

    # ✅ Step 1: Choose INLET (limit count)
    if good_windows:
        inlet = good_windows[:2]   # max 2 inlet windows
    elif neutral_windows:
        inlet = neutral_windows[:1]  # fallback minimal opening

    # Helper: opposite side
    def opposite(side):
        return {
            "NORTH": "SOUTH",
            "SOUTH": "NORTH",
            "EAST": "WEST",
            "WEST": "EAST"
        }[side]

    # ✅ Step 2: Choose ONE exhaust window
    exhaust_side = None
    if inlet:
        exhaust_side = opposite(inlet[0].side)

    for w in windows:
        if exhaust_side and w.side == exhaust_side:
            exhaust.append(w)
            break   # Only one exhaust window

    # ✅ Step 3: Everything else CLOSED
    for w in windows:
        if w not in inlet and w not in exhaust:
            closed.append(w)

    return inlet, exhaust, closed