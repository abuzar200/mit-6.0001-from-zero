def bisection_srch(n, low, high, tries=0):
    if low > high:
        return None, tries
    mid = (low + high) // 2
    if mid == n:
        return mid, tries
    elif mid < n:
        return bisection_srch(n, mid + 1, high, tries + 1)
    else:
        return bisection_srch(n, low, mid - 1, tries + 1)


number = 34
low = 1
high = 100
result, tries = bisection_srch(number, low, high)
print(result, tries)
