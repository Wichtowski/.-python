import random
def sum_three(nums):
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


len_number = random.randint(0, 11)
nums = []
for num in range(len_number):
    num = random.randint(-11, 11)
    nums.append(num)
print(f"Numbers: {nums}")
print(f"Sum of three element that sums to 0 : {sum_three(nums)}")
