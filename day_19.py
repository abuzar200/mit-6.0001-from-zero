alphabets = "abcdefghijklmnopqrstuvwxyz"

word = input("enter a word i wil cheer for you ! Word:")
times = int(input("Enter the enthusiasm(1-10)"))

for char in word:
    if char in alphabets:
        print("Give me a " + char + "!" + " " + char)
    else:
        print("Give me a " + char + "!" + " " + char)
print("what does that spell?")
for i in range(times):
    print(word, "!!!")
