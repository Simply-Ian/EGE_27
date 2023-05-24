with open('27B_4116.txt', 'r') as FILE:
    N, K = [int(i) for i in FILE.readline().split(' ')]
    nums = [int(i) for i in FILE.readlines()]

tail = 0
head = 0
cur_len = 0
cur_sum = 0
max_len = 0
while head < len(nums):
    cur_sum += nums[head]
    while cur_sum > K:
        cur_sum -= nums[tail]
        tail += 1
    max_len = max(max_len, head - tail + 1)
    head += 1
print(max_len)