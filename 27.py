with open('27b.txt', 'r') as FILE:
    N = int(FILE.readline())
    K = int(FILE.readline())
    numbers = [int(i) for i in FILE.readlines()]

m_by_7 = [0, 0]
m_by_1 = [0, 0]
counter = 0
for index in range(len(numbers)):
    if index >= K:
        research_num = numbers[index - K]
        if research_num % 7 == 0:
            m_by_7[research_num % 2] += 1
        else:
            m_by_1[research_num % 2] += 1

    num = numbers[index]
    if num % 7 == 0:
        counter += m_by_1[num % 2]
    counter += m_by_7[num % 2]

print(counter)