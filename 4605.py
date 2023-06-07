with open('27B_4605.txt', 'r') as FILE:
    N = int(FILE.readline())
    raw_points = []
    A = 36
    max_pos = 0
    for i in FILE.readlines():
        pos, amount = [int(j) for j in i.split()]
        amount = (amount + A - 1) // A
        max_pos = max(max_pos, pos)
        raw_points.append((pos, amount))
    print("Data read")
    points = [0] * (max_pos + 1)
    for p in raw_points:
        points[p[0]] = p[1]
    print("Road model built")

cur_sum = 0
for i in range(len(points)): cur_sum += points[i] * i
min_sum = cur_sum
left_sum = points[0]
right_sum = sum(points[1:])

for i in range(1, len(points)):
    cur_sum = cur_sum + left_sum - right_sum
    if points[i] != 0: min_sum = min(min_sum, cur_sum)
    left_sum += points[i]
    right_sum -= points[i]
print(min_sum)