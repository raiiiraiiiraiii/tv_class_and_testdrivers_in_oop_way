# Import TV class
from TV import TV

# Create the two TV objects
tv1 = TV()
tv2 = TV()

# A function to display the status of both TVs
def show_status(tv1, tv2):
    print(f"\ntv1's channel is {tv1.getChannel()} and volume level is {tv1.getVolumeLevel()}")
    print(f"tv2's channel is {tv2.getChannel()} and volume level is {tv2.getVolumeLevel()}\n")

# A function to validate user's input
def validate(prompt, valid_range = None):
    while True:
        try:
            value = int(input(prompt))
            if valid_range and value not in valid_range:
                print(f"Please enter a value in the range {valid_range}.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter an integer.")

# Display the main options for the program
# Get the user's choice and validate it
# Perform the corresponding action based on the user

# Display the options for controlling the TV
# Get the user's choice and validate it
# Perform the corresponding action based on the user's input

