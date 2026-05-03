# leet code problem for recursion and dictionaries
# Given a list of integers nums and a target integer target, return the indices of the two numbers that add up to the target.
# You may assume that each input has exactly one solution, and you may not use the same element twice.
def add(nums, t):
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == t:
                return [i, j]
    return "not found"


t = 9
nums = [2, 7, 11, 15]
addition = add(nums, t)
print(addition)
# not in the format of leet code, cuz i dint study class yet
