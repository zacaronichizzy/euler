import math

def get_digit(n, i):
    return n // 10**i % 10

get_digit(987654321, 5)

def digit_sum(n):
    no_digits = int(math.log10(n)) + 1
    sum = 0
    for i in range(no_digits):
        sum += get_digit(n, i)
    return sum

x = 2**1000
digit_sum(x)

#############

# Elegant:
sum = 0
for n in str(2**1000):
    sum += int(n)
sum