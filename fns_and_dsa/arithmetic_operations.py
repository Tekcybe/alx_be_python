def perform_operation(num1, num2, operation):
	operation = operation.lower()
	if operation == "add":
		return num1 + num2
	elif operation == "subtract":
		return num1 - num2
	elif operation == "multiply":
		return num1 * num2
	elif operation == "divide":
		if num1 or num2 == 0:
			return "Error: Cannot divide by 0"
		return num1 / numb2
	else:
		return "Error: Unsupported operation"
