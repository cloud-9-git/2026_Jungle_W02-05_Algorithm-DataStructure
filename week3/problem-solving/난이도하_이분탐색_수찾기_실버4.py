# 이분탐색 - 수 찾기 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/1920
N = int(input())
numbs = list(map(int, input().split()))
M = int(input())
checks = list(map(int, input().split()))

numbs.sort()

def check_numb(numbs, check, left, right):

    if left > right:
        return 0
    mid = (left+right) // 2
    if check == numbs[mid]:
        return 1
    elif check < numbs[mid]:
        return check_numb(numbs, check, left, mid - 1)
    else:
        return check_numb(numbs, check, mid + 1, right)

for check in checks:
    print(check_numb(numbs, check, 0, len(numbs)-1))

