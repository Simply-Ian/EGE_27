with open('27B_5644.txt', 'r') as FILE:
    N = int(FILE.readline())
    nums = [int(i) for i in FILE.readlines()]

right_sum = sum(nums[1:])
left_sum = nums[0]
max_cost = cur_cost = sum([nums[i]*i for i in range(len(nums))])
for point in range(1, len(nums)):
    cur_cost -= right_sum
    cur_cost += left_sum
    max_cost = max(max_cost, cur_cost)
    left_sum += nums[point]
    right_sum -= nums[point]
print(max_cost)