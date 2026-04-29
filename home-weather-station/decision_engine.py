from evaluator import classify_side, apply_wind_override
from modes import decide_mode
from window_engine import assign_roles
from data.windows_layout import WINDOWS


def decide(indoor, outdoor, doors_open):
    side_map = {}

    for side in ["NORTH", "SOUTH", "EAST", "WEST"]:
        cls = classify_side(indoor, outdoor, side)
        cls = apply_wind_override(side, cls, outdoor["wind_dir"])
        side_map[side] = cls

    mode = decide_mode(indoor, outdoor)

    # If doors are closed, we cannot ventilate effectively
    if not doors_open:
        return {
            "mode": "ISOLATE",
            "open": [],
            "close": [w.id for w in WINDOWS],
            "reason": "Doors closed - no airflow path"
        }

    if mode == "ISOLATE":
        return {
            "mode": "ISOLATE",
            "open": [],
            "close": [w.id for w in WINDOWS]
        }

    inlet, exhaust, closed = assign_roles(WINDOWS, side_map)

    # ✅ Remove duplicates safely
    unique_windows = {w.id: w for w in (inlet + exhaust)}

    return {
        "mode": mode,
        "open": list(unique_windows.keys()),
        "close": [w.id for w in closed]
    }