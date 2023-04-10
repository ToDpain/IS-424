num = int(input("Enter a positive integer: "))
sum = 0

for i in range(1, num+1):
    sum += i

print("The sum of integers from 1 to", num, "is", sum)
