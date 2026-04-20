cube = 27
epsilon = 0.01
low = 0
high = cube
num_guesses = 0
guess = (high + low) / 2
while abs(guess**3 - cube) >= epsilon:  # ← fix here
    if guess**3 < cube:
        low = guess
    else:
        high = guess
    guess = (high + low) / 2
    num_guesses += 1
print(num_guesses, "guesses")
print(guess, "is close to the cube root of", cube)
