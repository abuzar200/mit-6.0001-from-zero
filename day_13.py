# Given an integer x, recursively returns whether x is palindrome or not


def ispalindrome(x):
    x = str(x)
    if len(x) <= 1:
        return "palindrome"
    elif x[0] == x[-1]:
        return ispalindrome(x[1:-1])
    else:
        return "not a palindrome"


userin = input("Enter a number to know if its a palindrome: ")
print(ispalindrome(userin))
