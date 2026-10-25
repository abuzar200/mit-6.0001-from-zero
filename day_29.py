# revising from zero again
# approximation search
cube = 64
epsilon =0.0001
increment = 0.01
guess =0.0
num_guesses = 0
while abs(guess**3-cube)>=epsilon and guess <= cube:
    guess +=increment
    num_guesses +=1
print(num_guesses, "is the number of guesses")
if abs(guess**3-cube) >= epsilon:
    print("Failed to find the cube root of ",cube)
else:
    print("cube root of,", cube , "is close to ", guess )
