import math
import re

def num_digits(n):
    if n == 0:
        no_digits = 1
    else:
        no_digits = int(math.log10(n)) + 1
    return no_digits

def get_digit(n, i):
    return n // 10**i % 10

def digit(n):
    d = get_digit(n, 0)
    words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    return words[d-1]

def teen(n):
    d = get_digit(n, 0)
    words = ["ten", "eleven", "twelve", "thir", "four", "fif", "six", "seven", "eigh", "nine"]
    if d <= 2:
        return words[d]
    else:
        return words[d] + "teen"

def tens(n):
    d = get_digit(n, 1)
    words = ["twen", "thir", "for", "fif", "six", "seven", "eigh", "nine"]
    return words[d-2] + "ty"

def hundred(n):
    no_digits = num_digits(n)
    d = []
    for i in range(no_digits):
        d.append(get_digit(n, i))
    name = ""
    if no_digits == 3:
        name += digit(d[2]) + " hundred"
        if d[1] != 0 or d[0] != 0:
            name += " and "
    if no_digits > 1 and d[1] == 1:
        name += teen(n)
    else:
        if no_digits > 1 and d[1] != 0:
            name += tens(n)
            if d[0] != 0:
                name += "-"
        if d[0] != 0:
            name += digit(d[0])
    return name

def thousand(i):
    pref = ["m", "b", "tr", "quadr", "quint", "sext", "sept", "oct", "non"]
    if i == 1:
        return "thousand"
    else:
        return pref[i-2] + "illion"
    
def big_pref(i):
    pref = ["", "un", "duo", "tre", "quattuor", "quin", "sex", "septen", "octo", "novem"]
    return pref[(i-1) % 10]

def big_num(i):
    pref = ["vi", "tri", "quadra", "quinqua", "sexa", "septua", "octo", "nona"]
    if i < 21:
        return big_pref(i) + "decillion"
    else:
        return big_pref(i) + pref[(i-1) // 10] + "gintillion"
    
def get_hundred(n, i):
    return n // 1000**i % 1000
    
def number_name(n):
    no_digits = num_digits(n)
    t = (no_digits - 1) // 3
    name = ""
    for i in range(t, -1, -1):
        h = get_hundred(n, i)
        if h != 0:
            if i != t:
                name += " "
            if i != 0:
                name += hundred(h) + " "
                if i < 11:
                    name += thousand(i)
                else:
                    name += big_num(i)
                if i > 1:
                    name += ","
            else:
                if t != 0:
                    name += "and "
                name += hundred(h)
    return name

def name_count(n, other = False):
    name = number_name(n)
    if other == False:
        name = re.sub("[ ,-]", "", name)
    return len(name)

total = 0
for n in range(1, 1001):
    total += name_count(n)
total