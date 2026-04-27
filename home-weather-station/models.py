class Window:
    def __init__(self, id, side, room, height, size):
        self.id = id
        self.side = side
        self.room = room
        self.height = height
        self.size = size


class IndoorState:
    def __init__(self, temp, humidity):
        self.temp = temp
        self.humidity = humidity


class OutdoorState:
    def __init__(self, temp, humidity, wind_dir, wind_speed):
        self.temp = temp
        self.humidity = humidity
        self.wind_dir = wind_dir
        self.wind_speed = wind_speed