
def main():
    # Prompt user for input
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").lower()
    time_bound = input("Is it time-bound? (yes/no): ").lower()

    # Process the task based on priority
    match priority:
        case 'high':
            priority_msg = "high priority"
        case 'medium':
            priority_msg = "medium priority"
        case 'low':
            priority_msg = "low priority"
        case _:
            print("Invalid priority entered. Exiting.")
            return

    # Determine if the task is time-bound and create the reminder message
    if time_bound == 'yes':
        time_msg = "requires immediate attention today!"
    else:
        time_msg = "Consider completing it when you have free time."

    # Print the final reminder
    print(f"Reminder: '{task}' is a {priority_msg} task that {time_msg}")

if __name__ == "__main__":
    main()

