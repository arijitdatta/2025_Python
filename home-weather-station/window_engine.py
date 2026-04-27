def assign_roles(windows, side_map):
    inlet = []
    exhaust = []
    closed = []

    for w in windows:
        side_status = side_map[w.side]

        if side_status == "GOOD":
            inlet.append(w)

        elif side_status == "NEUTRAL":
            exhaust.append(w)

        else:
            closed.append(w)

    return inlet, exhaust, closed