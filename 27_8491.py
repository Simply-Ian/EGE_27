with open('27b_8491.txt', 'r') as FILE:
    N = int(FILE.readline())
    K = int(FILE.readline())
    M = int(FILE.readline())
    numbers = [int(i) for i in FILE.readlines()]
    print("N:", N)

numbers = list(zip(range(len(numbers)), numbers))
numbers.sort(key=lambda x: x[1], reverse=True)
counter = 0
indices = []
max_sum = 0
progress = 0
while counter < M:
    cur = numbers.pop(0)
    if all(abs(i - cur[0]) >= K for i in indices):
        max_sum += cur[1]
        indices.append(cur[0])
        counter += 1
    progress += 1
    if progress % 10_000 == 0: print("Progress", progress)
print(max_sum)