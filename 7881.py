from queue import Queue

with open('27A_7881.txt', 'r') as FILE:
    N = int(FILE.readline())
    K = int(FILE.readline())
    numbers = [int(i) for i in FILE.readlines()]

A = 100
k_37 = [0] * A
k_1 = [0] * A
counter = 0
queue = Queue()
for index in range(len(numbers) + K):
    try:
        num = numbers[index]
        queue.put(num)
        if num % 37 == 0: k_37[num % A] += 1
        else: k_1[num % A] += 1
    except IndexError: pass

    if index >= K:
        s_num = queue.get()
        if s_num % 37 == 0:
            counter += k_1[s_num % A]
            k_37[s_num % A] -= 1
        else:
            counter += k_37[s_num % A]
            k_1[s_num % A] -= 1
print(counter)