# Maximum path sum of triangle with 100 rows

triangle = []
f = open('files/0067_triangle.txt', 'r')
for line in f:
    l = line.strip().split()
    row = [int(x) for x in l]
    triangle.append(row)

N = len(triangle)
for i in range(N-2, -1, -1):
    n = len(triangle[i])
    for j in range(n):
        triangle[i][j] += max(triangle[i+1][j:j+2])
    print(triangle[i])
print("done")

