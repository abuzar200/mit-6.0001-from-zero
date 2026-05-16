def calculate_discount(price, percent):
    """returns calculated discount"""
    return price * (1 - percent / 100)


def apply_gst(price, rate=18):
    """returns the gst applied amount"""
    return price * (1 - rate / 100)


def final_price(base, discount):
    after_discount = calculate_discount(base, discount)
    return apply_gst(after_discount)


total = 1000


# def broken_add(amount):
#     total = total + amount
#     return total


def correct_add(amount):
    global total
    total = total + amount
    return total


print(final_price(2000, 10))
