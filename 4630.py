with open('27B_4630.txt', 'r') as FILE:
    N, K, M = [int(i) for i in FILE.readline().split(' ')]
    # ====================================================
    V = 9 
    # ====================================================
    points = [0] * K
    for i in range(N):
        index, probs = [int(i) for i in FILE.readline().split(' ')]
        conts = (probs + V - 1) // V
        points[index % K] = conts

cur_sum = sum(points[0 : 2*M + 1])
max_sum = cur_sum if points[M] != 0 else 0
for i in range(M + 1, K + M + 1):
    cur_sum -= points[i - M - 1]
    cur_sum += points[(i + M) % K]
    if points[i % K] != 0: max_sum = max(max_sum, cur_sum)
print(max_sum)