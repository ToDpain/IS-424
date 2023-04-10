def find_max(x, y, z):
    """
    This function accepts three numbers as arguments and returns the largest number among them.
    """
    if x >= y and x >= z:
        return x
    elif y >= x and y >= z:
        return y
    else:
        return z

def main():
    """
    This function accepts three numbers from user (as inputs) and calls find_max to display the largest.
    """
    x = float(input("Enter the first number: "))
    y = float(input("Enter the second number: "))
    z = float(input("Enter the third number: "))
    
    max_num = find_max(x, y, z)
    
    print("The largest number is:", max_num)

# call the main function

