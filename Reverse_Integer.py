import random


def reverse(x) -> int:
    y = []
    i = ""
    if -2 ** 31 < x < 2 ** 31:
        for letter in str(x):
            y.append(letter)
        if y[0] == "-":
            y.pop(0)
            i += "-"
        y = y[::-1]
        for letter in range(0, len(y) - 1):
            if y[0] == "0":
                y.pop(0)
        for letter in y:
            i += str(letter)
        i = int(i)
        if i > 2 ** 31 - 1 or i < -2 ** 31:
            i = 0
        return i
    else:
        i = 0
        return i


x = random.randint(-999, 999)
print(x)
print(reverse(x))
