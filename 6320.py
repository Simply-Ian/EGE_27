with open('27B_6320.txt', 'r') as FILE:
    N, M = [int(i) for i in FILE.readline().split(' ')]
    points = [int(i) for i in FILE.readlines()]
max_sum = cur_sum = sum(points[0 : 2*M + 1])
for i in range(M + 1, N + M):
    cur_sum -= points[i-M-1]
    cur_sum += points[(i + M) % N]
    max_sum = max(max_sum, cur_sum)
print(max_sum)