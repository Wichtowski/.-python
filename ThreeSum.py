import random
def sumThree(nums):
    tab = []
    nums.sort()
    if len(nums) < 3:
        return []
    else:
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if i != j:
                    for k in range(j + 1, len(nums)):
                        if i != k and j != k and nums[i] + nums[j] + nums[k] == 0:
                            tab.append([nums[i], nums[j], nums[k]])
            res = list(set(tuple(sorted(sub)) for sub in tab))

    return res
len_number = random.randint(0, 11)
nums = []
for num in range(len_number):
    num = random.randint(-11, 11)
    nums.append(num)
print(nums)
print(sumThree(nums))
