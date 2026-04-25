# using tubles to find quotient and remainder
def quotient_and_remainder(x, y):
    q = x // y
    r = x % y
    return (q, r)


(q, r) = quotient_and_remainder(26, 5)
print(f" The quotient is {q} and the remainder is {r}")
