# factorial
def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n - 1)


# add code of counting how many iterations to reach the answer

x = int(input("enter the value of n: "))
result = fact(x)
print(result)


# fibonacci
def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


# here also "adding " number of iterations

x = int(input("enter the value of n: "))
result = fib(x)
print(result)


# palindrome
def ispallindrome(s):
    def to_chars(s):
        s = s.lower()
        ans = ""
        for c in s:
            if c in "abcdefghijklmnopqrstuvwxyz":
                ans = ans + c
        return ans

    def is_pal(s):
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and is_pal(s[1:-1])

    return is_pal(s)


print(ispallindrome("racecar"))
