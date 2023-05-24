"""Недоделанное решение"""
with open('27_test.txt', 'r') as FILE:
    N, M = [int(i) for i in FILE.readline().split()]
    raw_points = FILE.readlines()
    points_len = int(raw_points[-1].split(' ')[0])
    points = [0] * points_len
    start = -1
    for rp in raw_points:
        dist, am = [int(i) for i in rp.split()]
        if start == -1: start = dist
        points[dist - 1] = (am + M - 1) // M

right_sum = sum(points[start:])
left_sum = points[start]
min_cost = 10 ** 10
cur_cost = sum([points[i]*i for i in range(len(points))])
for point in range(start, points_len):
    cur_cost -= right_sum
    cur_cost += left_sum
    min_cost = min(min_cost, cur_cost)
    left_sum += points[point]
    right_sum -= points[point]
print(min_cost)