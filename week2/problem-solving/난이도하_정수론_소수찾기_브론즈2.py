# 정수론 - 소수 찾기 (백준 브론즈2)
# 문제 링크: https://www.acmicpc.net/problem/1978

nums_len = int(input())
nums = list(map(int, input().split()))

primeNum_count = 0

for i in range(nums_len):
    if nums[i] == 0:
        continue
    if nums[i] == 1:
        continue
    if nums[i] == 2:
        primeNum_count += 1
        continue
    if nums[i] % 2 != 0:
            for j in range(3, nums[i], 2):
                if nums[i] % j == 0:
                    break
            else: 
                primeNum_count += 1
print(primeNum_count)
                