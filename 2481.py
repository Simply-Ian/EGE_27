with open("27B_2481.txt", 'r') as FILE:
    N = int(FILE.readline())
    numbers = [int(i) for i in FILE.readlines()]
A = 17
k = [0] * A
for n in numbers:
    k1 = k.copy()
    for i in range(A):
        compl_rem = (k[i] + n) % A
        k1[compl_rem] = max(k[i] + n , k1[compl_rem])
    k = k1.copy()
print(k[0])