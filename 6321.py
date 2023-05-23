with open('27A_6321.txt', 'r') as FILE:
    N, V, M = [int(i) for i in FILE.readline().split(' ')]
    points = [0] * K
    for i in range(N):
        index, probs = [int(i) for i in FILE.readline().split(' ')]
        conts = (probs + V - 1) // V
        points[index % K] = conts
        
cur_sum = sum(points[0 : 2*M + 1])
max_sum = cur_sum if points[M] != 0 else 0

for i in range(M + 1, N + M):
    cur_sum -= points[i - M - 1]
    cur_sum += points[(i + M) % N]
    if points[i] != 0: max_sum = max(max_sum, cur_sum)
print(max_sum)