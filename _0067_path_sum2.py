# Maximum path sum of triangle with 100 rows

triangle = []
f = open('files/0067_triangle.txt', 'r')
for line in f:
    l = line.strip().split()
    row = [int(x) for x in l]
    triangle.append(row)
print(triangle)

with open('files/0067_triangle.txt', 'r') as file:
    f = file.readlines()
for line in f:
    print(line)