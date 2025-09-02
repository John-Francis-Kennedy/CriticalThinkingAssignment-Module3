# Part 2: Alarm Clock

# Ask user for current time and hours to wait
current_time = int(input("Enter the current time (0-23): "))
hours_to_wait = int(input("Enter the number of hours to wait: "))

# Calculate new time
alarm_time = (current_time + hours_to_wait) % 24

# Display result
print(f"\nThe alarm will go off at {alarm_time}:00 on a 24-hour clock.")
