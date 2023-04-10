# Initialize the list
lst = []

# Get user input for 10 values
for i in range(10):
    val = int(input("Enter a number: "))
    lst.append(val)

# Initialize a variable to store the largest value
largest = lst[0]

# Loop through the list and compare each value to the largest value
for num in lst:
    if num > largest:
        largest = num

# Display the largest value
print("The largest number is:", largest)
