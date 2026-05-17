#!/usr/bin/env python3


from datetime import datetime

# Ask the user for the password
answer = input("Speak, friend, and enter: ")

# Check if the answer is correct
if answer.lower() == "mellon":

    print("\nWelcome, friend.")

    try:
        # Open the activity file and read the last activity
        with open("activity.txt", "r") as file:
            last_activity = file.read()

        print("Last activity:", last_activity)

    except FileNotFoundError:
        # If file does not exist yet
        print("No previous activity found.")

    # Get current date and time
    current_time = datetime.now()

    # Save current activity to the file
    with open("activity.txt", "w") as file:
        file.write(str(current_time))

    print("Current activity saved.")
    print("The time saved was:", current_time)

else:
    print("\nYou shall not pass, Sauron!")
