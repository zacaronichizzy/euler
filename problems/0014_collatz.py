# Longest Collatz sequence for initial number under 1,000,000
def collatz(x0):
    x = x0
    seq = [x0]
    while x != 1:
        if x % 2 == 0:
            x = int(x/2)
        else:
            x = 3*x + 1
        seq.append(x)
    return seq
collatz(13)

inits = []
# Only worth considering initial values from 500,000 upwards
for i in range(1000000 // 6 + 1):
    for j in [1, 2, 3, 5, 6]:
        inits.append(6*i + j)
inits = inits[:-1]
print(inits[0])

max_len = [0]
max_seq = []
max_x0 = [0]
used = set()
while len(inits) != 0:
    x0 = inits[0]
    x = x0
    seq = [x0]
    l = 1
    while x != 1:
        if x % 2 == 0:
            x = int(x/2)
        else:
            x = 3*x + 1
        seq.append(x)
        l += 1
        if x < x0:
            print("baaa")
            for i, m in enumerate(max_x0):
                print(i)
                if m > x:
                    m_x = i
                    break
            max_x = max_len[m_x]
            if l + max_x < max_len[-1]:
                print("BAAA")
                break
    l = len(seq)
    if l > max_len[-1]:
        print(f"x0 = {x0}")
        print(f"length = {l}")
        print(f"sequence = {seq}")
        print()
        max_len.append(l)
        max_seq = seq
        max_x0.append(x0)
    for x in seq:
        if x not in used and x % 6 != 4:
            inits.remove(x)
            used.add(x)

######################################################################

def collatz(x0):
    x = x0
    seq = [x0]
    while x != 1:
        if x % 2 == 0:
            x = int(x/2)
        else:
            x = 3*x + 1
        seq.append(x)
    return seq
collatz(13)

inits = []
# Only worth considering initial values from 500,000 upwards
for i in range(500000 // 6 + 1):
    for j in [1, 3, 4, 5]:
        inits.append(500000 + 6*i + j)
inits = inits[:-3]
inits[0]

max_len = 0
max_seq = []
max_x0 = [0]
used = set()
while len(inits) != 0:
    x0 = inits[0]
    seq = collatz(x0)
    l = len(seq)
    if l > max_len:
        print(f"x0 = {x0}")
        print(f"length = {l}")
        print(f"sequence = {seq}")
        print()
        max_len = l
        max_seq = seq
        max_x0 = x0
    for x in seq:
        if x % 6 not in {2, 4} and x < 1000000 and x >= 500000 and x not in used:
            inits.remove(x)
            used.add(x)

######################################################################

known = {}
def collatz_key(n):
    if n == 1:
        return 1
    elif n in known:
        return known[n]
    else:
        if n % 2 == 0:
            r = 1 + collatz_key(int(n/2))
        else:
            r = 2 + collatz_key(int(1.5*n + 0.5))
        known[n] = r
        return r

inits = []
# Only worth considering initial values from 500,000 upwards
for i in range(500000 // 6 + 1):
    for j in [1, 3, 4, 5]:
        inits.append(500000 + 6*i + j)
inits = inits[:-3]
inits[0]

max_len = 0
max_x0 = 0
for x0 in inits:
    l = collatz_key(x0)
    if l > max_len:
        print(f"x0 = {x0}")
        print(f"length = {l}")
        print()
        max_len = l
        max_x0 = x0
    
# Upper bound of 32000000
inits = []
for i in range(16000000 // 6 + 1):
    for j in [1, 2, 3, 5]:
        inits.append(16000000 + 6*i + j)
inits = inits[:-1]
inits[-10:]

max_len = 0
max_x0 = 0
for x0 in inits:
    l = collatz_key(x0)
    if l > max_len:
        print(f"x0 = {x0}")
        print(f"length = {l}")
        print()
        max_len = l
        max_x0 = x0


