with open('27b_8491.txt', 'r') as FILE:
    N = int(FILE.readline())
    K = int(FILE.readline())
    M = int(FILE.readline())
    numbers = [int(i) for i in FILE.readlines()]
    print("N:", N)

# [Сумма, фриз]
sum_hubs = []
for i in range(len(numbers)):
    for s in range(len(sum_hubs)):
        freeze = sum_hubs[s][1]
        sum_hubs[s][1] = freeze - 1 if freeze else 0
        if sum_hubs[1] == 0:
            shc = sum_hubs[s].copy()
            sum_hubs.append(shc)
            sum_hubs[s] += numbers[i]
            sum_hubs[s][1] = K
    if i < K:
        sum_hubs.append([numbers[i], 0])
    