fact = 1
for i in range(2, 101):
    fact *= i
fact = str(fact)
sum = 0
for x in fact:
    sum += int(x)
sum
