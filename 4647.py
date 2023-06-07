with open('27B_4647.txt', 'r') as FILE:
    N, M = [int(i) for i in FILE.readline().split()]
    A = 6
    raw_points = [(int(i) + A - 1) // A for i in FILE.readlines()]

points = []
for i in range(M, len(raw_points) - M):
    points.append(sum(raw_points[i - M : i + M + 1]))

max_prev = 0
max_sum = 0
for i in range(len(points)):
    if i >= 2*M + 1:
        max_prev = max(max_prev, points[i - (2*M + 1)])
    max_sum = max(max_sum, points[i] + max_prev)
print(max_sum)
    