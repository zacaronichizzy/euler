d = 6
m = 1
y = 1901
sun_count = 0
end = False
leap = False
while y < 2001:
    d += 7
    if d > 28:
        end = True
        if m == 2 and not leap:
            d -= 28
        elif d > 29 and m == 2 and leap:
            d -= 29 
        elif d > 30 and m in {4, 6, 9, 11}:
            d -= 30
        elif d > 31 and m in {1, 3, 5, 7, 8, 10, 12}:
            d -= 31
        else:
            end = False
    if d == 1:
        sun_count += 1
    if end:
        if m < 12:
            m += 1
        else:
            m = 1
            y += 1
            leap = y % 4 == 0
    end = False
sun_count
    
            