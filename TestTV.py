# Import TV class
from tv import TV

# Create the two TV objects
tv1 = TV()
tv2 = TV()

# A function to display the status of both TVs
def show_status(tv1, tv2):
    print(f"\ntv1's channel is {tv1.get_channel()} and volume level is {tv1.get_volume_level()}")
    print(f"tv2's channel is {tv2.get_channel()} and volume level is {tv2.get_volume_level()}\n")

# A function to validate user's input
def validate(prompt, valid_range=None):
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
def control_tv(tv, tv_label):
    while True:
        print(f"\nControlling {tv_label}:")
        print("1. Increase channel by 1")
        print("2. Decrease channel by 1")
        print("3. Set Channel (1-120)")
        print("4. Increase volume by 1")
        print("5. Decrease volume by 1")
        print("6. Set Volume (1-7)")
        print("7. Back to TV selection")

        # Get the user's choice and validate it
        choice = validate("Enter your choice: ", range(1, 8))

        # Perform the corresponding action based on the user
        if choice == 1:
            tv.channel_up()
        elif choice == 2:
            tv.channel_down()
        elif choice == 3:
            channel = validate("Enter the channel (1-120): ", range(1, 121))
            tv.set_channel(channel)
        elif choice == 4:
            tv.volume_level_up()
        elif choice == 5:
            tv.volume_level_down()
        elif choice == 6:
            volume = validate("Enter the volume level (1-7): ", range(1, 8))
            tv.set_volume_level(volume)
        elif choice == 7:
            break

        show_status(tv1, tv2)


def main():
    # Display the options for controlling the TV
    while True:
        print("\nOptions:")
        print("1. Turn on TV1")
        print("2. Turn on TV2")
        print("3. Show the two TV status")
        print("4. Exit the program")

        # Get the user's choice and validate it
        choice = validate("Enter your choice: ", range(1, 5))

        # Perform the corresponding action based on the user's input
        if choice == 1:
            tv1.turn_on()
            print("TV1 turned on")
            control_tv(tv1, "TV1")
        elif choice == 2:
            tv2.turn_on()
            print("TV2 turned on")
            control_tv(tv2, "TV2")
        elif choice == 3:
            show_status(tv1, tv2)
        elif choice == 4:
            print("TVs are turning off...")
            tv1.turn_off()
            tv2.turn_off()
            break


if __name__ == "__main__":
    main()