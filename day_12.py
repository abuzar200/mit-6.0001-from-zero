# lecture 7, Exception and input
try:
    a = int(input("Enter a number : "))
    b = int(input("Enter another number : "))
    print(f"{a} divided by {b}: ", a / b)
except ValueError:
    print("could not convert to number")
except ZeroDivisionError:
    print("can't devide by zero")
except:
    print("error")
else:
    print(f"{a} divided by {b} =", a / b)
finally:
    print("Program finished")
