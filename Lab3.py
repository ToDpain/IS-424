employee_dict = {}

while True:
    name = input("Enter the name of the employee: ")
    if name == "no":
        break
    salary = int(input("Enter the salary of the employee: "))
    employee_dict[name] = salary

print("Employee dictionary:", employee_dict)
