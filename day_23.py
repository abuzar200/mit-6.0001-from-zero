# function as an arguments


def func_a(x):
    return x


def func_b(y):
    return y


def func_c(z):
    return z


x = 0
y = 0
while x < 45 and y < 45:
    print(func_a(x) * func_b(y))
    x += 1
    y += 1
