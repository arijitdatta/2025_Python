from models import Window

WINDOWS = [

    # WEST SIDE (strong intake)

    Window("W1-HALL-W", "WEST", "HALL", "MID", "LARGE"),

   Window("W2-HALL-W", "WEST", "HALL", "MID", "LARGE"),

    Window("W3-Library-W", "WEST", "LIBRARY", "MID", "MEDIUM"),

    # EAST SIDE (exhaust)

    Window("W4-ArijitOffice-E", "EAST", "COVERED_AREA", "MID", "MEDIUM"),
    Window("W5-Kitchen-E", "EAST", "COVERED_AREA", "MID", "SMALL"),


    # SOUTH SIDE

    Window("W6-Bedroom-S", "SOUTH", "BEDROOM", "MID", "MEDIUM"),
    Window("W7-Library-S", "SOUTH", "LIBRARY", "LOW", "MEDIUM"),

   

    # NORTH SIDE (lane, risky)

    Window("W8-ArijitOffice-N", "NORTH", "OFFICE", "MID", "SMALL"),
    Window("W9-Hall-N", "NORTH", "DRAWING_ROOM", "MID", "LARGE"),

]