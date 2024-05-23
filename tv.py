class TV:
    def __init__(self):
        self.channel = 1
        self.volume_level = 1
        self.on = False

    def turn_on(self):
        self.on = True

    def turn_off(self):
        self.on = False

    def get_channel(self):
        return self.channel

    def set_channel(self, channel):
        if 1 <= channel <= 120:
            self.channel = channel

    def channel_up(self):
        if self.on and self.channel < 120:
            self.channel += 1

    def channel_down(self):
        if self.on and self.channel > 1:
            self.channel -= 1

    def get_volume_level(self):
        return self.volume_level

    def set_volume_level(self, volume_level):
        if 1 <= volume_level <= 7:
            self.volume_level = volume_level

    def volume_level_up(self):
        if self.on and self.volume_level < 7:
            self.volume_level += 1
        elif self.volume_level == 7:
            print("Volume limit reached!")

    def volume_level_down(self):
        if self.on and self.volume_level > 1:
            self.volume_level -= 1