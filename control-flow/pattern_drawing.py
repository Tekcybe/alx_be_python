size_of_pattern = int(input("Enter the size of the pattern: "))
row = 0
while row < size_of_pattern:
	for col in range(size_of_pattern):
		print("*", end="")
	print()
	row +=1


