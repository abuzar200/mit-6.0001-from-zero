"""Source: L1, L2. Tests whether you know exactly what Python does, not approximately.
A1. What is the difference between = and ==? Write one example of each where swapping them breaks the program.

answer- "=" is an assignment operator while"==" is a comparison operator.

A2. Without running it, write exactly what this prints and why:
pythonx = 5
y = x
x = x + 1
print(x, y)
answer- (6, 5)
A3. What does // do differently from /? When does it matter in real code?
answer- "//" picks out only the integer value on division, discarding the remainder."/" does regualr divion giving out floating point numbers.
A4. Write a while loop that prints every odd number from 1 to 19. Then rewrite it as a for loop. What's the difference in how they think?
answer-"""

# while loop
i = 0
while i < 20:
    if i % 2 == 0:
        i += 1
        continue
    else:
        print(i)
        i += 1
# for loop
for i in range(1, 20):
    if i % 2 == 0:
        continue
    else:
        print(i)

"""
SECTION B — Functions and Decomposition (10 min)
Source: L4. This is where most people collapse.
B1. Write a function is_divisible(x, y) that returns True if x is divisible by y. Then use it inside another function count_divisibles(n, y) that counts how many numbers from 1 to n are divisible by y. Call it with n=20, y=3.
answer- """


def is_divisible(x, y):
    return x % y == 0


def count_divisibles(n, y):
    count = 0
    for i in range(1, n + 1):
        if is_divisible(i, y):
            count = count + 1
    return count


result = count_divisibles(20, 3)
print(result)
"""
B2. What is scope? Write an example where a variable inside a function does NOT affect a variable of the same name outside it. Explain why in one sentence.
answer- scope is a where a variable is visible and accessible, which performs a particular defined action by execution of code inside it.
"""


# example -
x = 5  # global


def change_x():
    x = 100  # local, different x
    print(x)  # prints 100


change_x()
print(x)  # still prints 5 — global unchanged


"""
B3. What is the difference between return and print inside a function? Write a broken function that uses print where it should use return, and explain why it fails.
answer- print - doesnt store the value it only displays it u can see it but you cant use it , while return you can use the value and see it to. a return function returns or hand you the value, even if its not used the function by default return none.
"""


# example
def dis_divisible(x, y):
    if x % y == 0:
        print(f"{x} is divisible by {y}")
    else:
        print(
            f"{x}is not divisible by {y}"
        )  # this entire code can be written as return x % y ==0


"""SECTION C — Data Structures (10 min)
Source: L5, L6. Mutability is the trap.
C1. What is the difference between a list and a tuple? Give one situation where you must use a tuple and one where you must use a list.
answer-a list- can store anything even a list inside a list,is mutable you can add or remove a element inside a list. tuple tuple is an immutable ordered sequence it can hold anything a list holds, just can't be changed after creation.
C2. Without running it, what does this print?
python a = [1, 2, 3]
b = a
b.append(4)
print(a)
Why? What would you change to make a unaffected?
answer- [1,2,3,4] , itis called alias,and its for a single list change that affects the otherlists if there is connection to bith lists.
C3. Write a dictionary that maps three student names to their CGPA. Then write a loop that prints only the students with CGPA above 7.5.
answer-
"""
students = {"jyle": 4.6, "kinglud": 9.3, "ana": 7.5}
for name, gpa in students.items():
    if gpa > 7.5:
        print(name)


""" C4. What is aliasing? Why is it dangerous? One example
answe-its for a single list change that affects the otherlists if there is connection to bith lists. , it is dangarous because the other lists prints same thing as the initial list,
example-
"""

my_list = [1, 2, 3]
b = my_list
b.append(4)
print(my_list)
