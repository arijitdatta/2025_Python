from evaluator import classify_side, apply_wind_override
from modes import decide_mode
from window_engine import assign_roles
from data.window_layout import WINDOWS


def decide(indoor, outdoor):
    side_map = {}

    for side in ["NORTH", "SOUTH", "EAST", "WEST"]:
        cls = classify_side(indoor, outdoor, side)
        cls = apply_wind_override(side, cls, outdoor["wind_dir"])
        side_map[side] = cls

    mode = decide_mode(indoor, outdoor)

    if mode == "ISOLATE":
        return {"open": [], "close": [w.id for w in WINDOWS]}

    inlet, exhaust, closed = assign_roles(WINDOWS, side_map)

    return {
        "open": [w.id for w in inlet + exhaust],
        "close": [w.id for w in closed],
        "mode": mode
    }