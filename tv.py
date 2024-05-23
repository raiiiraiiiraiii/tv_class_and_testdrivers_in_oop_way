#Add Pseudocode

# Create TV class

# Define the TV class
class TV:

# Initialize the TV with default values
    def __init__(self):
        self.channel = 1
        self.volume_level = 1
        self.on = False

# Create method to turn on the TV
    def turn_On(self):
        self.on = True
# Create method to turn off the TV
    def turn_Off(self):
        self.on = False

# Create method to get the current channel
    def get_Channel(self):
        return self.channel
# Create method to set the channel within the range of 1 to 120
    def set_Channel(self, channel):
        if 1 <= channel <= 120:
            self.channel = channel
# Create method to increase the channel by 1, if the TV is on and the channel is less than 120
    def channel_Up(self):
        if self.on and self.channel < 120:
            self.channel += 1
# Create method to decrease the channel by 1, if the TV is on and the channel is greater than 1
    def channel_Down(self):
        if self.on and self.channel > 1:
            self.channel -= 1

# Create method to get the current volume level
    def get_Volume_Level(self):
        return self.volume_level
# Create method to set the volume level within the range of 1 to 7
    def set_Volume_Level(self, volume_level):
        if 1 <= volume_level<= 7:
            self.volume_level = volume_level
# Method to increase the volume by 1, if the TV is on and the volume is less than 7
    def Volume_Level_up(self):
        if self.on and self.volume_level < 7:
            self.volume_level += 1
        elif self.volume_level == 7:
            print("Volume limit reached!")
# Method to decrease the volume by 1, if the TV is on and the volume is greater than 1
    def Volume_Level_down(self):
        if self.on and self.volume_level > 1:
            self.volume_level -= 1





