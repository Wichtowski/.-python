import random


def max_gap(nums):
    if len(nums) < 2:
        return 0
    else:
        for i in range(0, len(nums)-1):
            if i == 0:
                result = nums[i+1] - nums[i]
            if result < nums[i+1] - nums[i]:
                result = nums[i+1] - nums[i]
            else:
                pass
    return result


y = random.randint(0, 20)
nums = []
for i in range(0, y):
    nums.append(random.randint(0, 100))
nums.sort()
print(nums)
print(max_gap(nums))
