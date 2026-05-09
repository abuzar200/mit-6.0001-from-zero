sq = 81
epsilon = 0.001
step = 0.00001
sqrt = 0.0
count = 0

while abs(sqrt**2 - sq) >= epsilon and sqrt <= sq:
    sqrt += step
    count += 1

print(f"Exhaustive: {sqrt:.3f} in {count} steps")
