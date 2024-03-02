from random import randint

N = 10
nums = list()

for i in range(N):
    nums.append(randint(0, 100))

print(nums)
print(sorted(nums))

# for i in range(N):
#     basis = i
#     for j in range(i+1, N):
#         if nums[j] < nums[basis]:
#             basis = j 

#     nums[basis], nums[i] = nums[i], nums[basis]

# print(nums)

# for i in range(N):
#     for j in range(0, N-1-i):
#         if nums[j] > nums[j+1]:
#             nums[j], nums[j+1] = nums[j+1], nums[j]

# print(nums)

