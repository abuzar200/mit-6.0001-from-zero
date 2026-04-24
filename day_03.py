def is_even(z):
    return z % 2 == 0


for i in range(0, 20):
    if is_even(i):
        print(i, "even")
    else:
        print(i, "odd")
