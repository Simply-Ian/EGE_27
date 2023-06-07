with open('27-A_5239.txt', 'r') as FILE:
    N, M, K = [int(i) for i in FILE.readline().split()]
    points = [int(i) for i in FILE.readlines()]

tails = []
counter = 0
for i in range(K*2 - 1, len(points)):
    prev_sum = sum(points[i - 2*K + 1 : i - K + 1])
    tails.append(prev_sum)
    for t in tails:
        if t + sum(points[i - K + 1 : i+1]) >= M: counter += 1
print(counter)