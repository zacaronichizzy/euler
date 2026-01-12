import math

def divisors(n):
    divisors = [1]
    bound = int(math.sqrt(n))
    if math.sqrt(n) % 1 == 0:
        divisors.append(bound)
    for i in range(2, bound): 
        q = n / i
        if q == int(q):
            divisors.append(int(i))
            divisors.append(int(q))
    return divisors
divisors(100)
def d(n):
    return sum(divisors(n))
d(100)

sum_list = []
amicables = {}
for n in range(1, 10001):
    sum = d(n)
    if sum in sum_list:
    