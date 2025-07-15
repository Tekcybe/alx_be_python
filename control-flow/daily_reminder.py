task = input("Enter your task: ")
task_priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time bound? (yes/no): ").lower()
match task_priority:
	case "high":
		if time_bound == "yes":
			print(f"Reminder: {task} is a high priority task that requires immediate attention today!")
		elif time_bound == "no":
			print(f"Note: {task} is a low priority task. Consider completing it when you have free time.")
	case "medium":
		if time_bound == "yes":
			print(f"Reminder: {task} is a medium priority task that does not require immediate action but work on it as quick as possible.")
		elif time_bound == "no":
			print(f"Note : {task} is a medium priority task. Consider completing it at your free time.")
	case "low":
		if time_bound == "yes":
			print(f"Reminder: {task} is a low priority task ,but work on it as quick as possible.")
		elif time_bound == "no":
			print(f"Note: {task} is a low level task. Consider completing it at your free time.")

