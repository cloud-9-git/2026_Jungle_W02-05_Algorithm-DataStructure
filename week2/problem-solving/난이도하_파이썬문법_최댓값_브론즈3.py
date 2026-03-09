# 파이썬 문법 - 최댓값 (백준 브론즈3)
# 문제 링크: https://www.acmicpc.net/problem/2562
nums = [int(input()) for _ in range(9)]

max_number = 0
max_number_index = 0
for i in range(len(nums)):
    if nums[i] >= max_number:
        max_number = nums[i]
        max_number_index = i +  1

print(max_number)
print(max_number_index)
