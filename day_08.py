# fib using memoization
def fib(n):
    # will implement count in here, in futher coding says
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def fib_eff(n, d):
    # will implement count in here, in futher coding says
    if n in d:
        return d[n]
    else:
        ans = fib_eff(n - 1, d) + fib_eff(n - 2, d)
        d[n] = ans
        return ans


d = {1: 1, 2: 1}
no = 34
print(fib(no))
print(fib_eff(no, d))
