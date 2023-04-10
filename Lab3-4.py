def is_vowel(c):
    """
    Returns True if a given character is a vowel (either uppercase or lowercase), and False otherwise.
    """
    vowels = 'AEIOUaeiou'
    return c in vowels

def main():
    """
    Asks the user for a string input and counts the number of vowels in that string.
    """
    string = input('Enter a string: ')
    vowel_count = 0
    for c in string:
        if is_vowel(c):
            vowel_count += 1
    print('Number of vowels in the string:', vowel_count)

# call the main function   
main()
