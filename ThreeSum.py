import random


def sum_three(x):
    tab = []
    x.sort()
    if len(x) < 3:
        return []
    else:
        for i in range(len(x) - 1):
            for j in range(i + 1, len(x)):
                if i != j:
                    for k in range(j + 1, len(x)):
                        if i != k and j != k and x[i] + x[j] + x[k] == 0:
                            tab.append([x[i], x[j], x[k]])
            res = list(set(tuple(sorted(sub)) for sub in tab))
    return res


def optimised_sum_three(x):
    tab = []
    nums.sort()
    for i, a in enumerate(nums):
        if i > 0 and a == nums[i - 1]:
            continue
        left = i + 1
        right = len(nums) - 1
        while left < right:
            three_sum = a + nums[left] + nums[right]
            if three_sum > 0:
                right -= 1
            elif three_sum < 0:
                left += 1
            else:
                tab.append([a, nums[left], nums[right]])
                left += 1
                while nums[left] == nums[left - 1] and left < right:
                    left += 1
    return tab


len_number = random.randint(0, 11)
nums = []
for num in range(len_number):
    num = random.randint(-11, 11)
    nums.append(num)
print(f"Numbers: {nums}")
print(f"Sum of three elements that equals to 0 : {sum_three(nums)}")
print(f"Sum of three (optimised) elements that equals to 0 : {optimised_sum_three(nums)}")
