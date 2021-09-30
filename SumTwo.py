import random
def sumTwo(nums):  
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return i, j
len_number = random.randint(0, 11)
target = random.randint(-5, 11)
nums = []
for num in range(len_number):
    num = random.randint(-11, 11)
    nums.append(num)
print(f"Numbers: {nums} and target {target}")
print(f"Solution: {sumTwo(nums)}")
