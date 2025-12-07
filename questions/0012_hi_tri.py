def divisors(x):
    if x == 1:
        return {1}
    i = 2
    divs = {1, x}
    while x != i:
        if x % i == 0:
            r = x // i
            divs = divs | divisors(i) | divisors(r)
        i += 1
    return divs

def tri(n):
    return int(n * (n+1) / 2)

max_no = 0
max_divs = set()
n = 0
while max_no <= 500:
    n += 1
    x = tri(n)
    divs = divisors(x)
    if len(divs) > max_no:
        max_no = len(divs)
        print(max_no)
        max_divs = divs
        print(max_divs)

#######################################################

def prime_fact(x):
    if x == 1:
        return []
    if x % 2 == 0:
        i = 2
    elif x % 3 == 0:
        i = 3
    else:
        i = 5
        while i < x**0.5:
            if x % i == 0:
                break
            if i % 3 == 1:
                i += 4
            else:
                i += 2
    if i > x**0.5:
        return [x]
    r = int(x / i)
    return [i] + prime_fact(r)
prime_fact(100)

def no_of_factors(x):
    fact = prime_fact(x)
    count = 1
    for p in set(fact):
        p_list = [f for f in fact if f == p]
        count *= len(p_list) + 1
    return count
no_of_factors(9)

max = 0
n = 0
while max <= 500:
    n += 1
    if n % 2 == 0:
        n_facts = no_of_factors(int(n/2)) * no_of_factors(n+1)
    else:
        n_facts = no_of_factors(n) * no_of_factors(int(n+1)/2)
    if n_facts > max:
        print(n_facts)
        print(tri(n))
        print()
        max = n_facts
# Can improve by reusing no. of divisors of n+1 component for next n component

        



    




