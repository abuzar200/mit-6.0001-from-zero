cube = -164
for guess in range(abs(cube) + 1):
    if guess**3 >= abs(cube):
        break
if guess**3 != abs(cube):
    print(f"{cube} is not a perfect cube, please enter a valid cube")
elif cube < 0:
    guess = -guess
print(f"cube root of {cube} is {guess}")
