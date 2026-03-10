# 재귀함수 - 하노이 탑 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/1914
import copy

N = int(input())

def tower(n):
    if n == 0:
        return 0
    else:
        return 2 * tower(n-1) + 1
K = tower(N)
print(K)

if N <= 20: 
    def move(n):
        if n == 1:
            return [[1, 3]]
        else:
            copied = copy.deepcopy(move(n-1))
            copied_2 = copy.deepcopy(move(n-1))
            result =[]
            # move(n-1)에서 2->3, 3->2로 바꿈
            for i in range(len(copied)):
                for j in range(2):
                    if copied[i][j] == 2:
                        copied[i][j] = 3
                    elif copied[i][j] == 3:
                        copied[i][j] = 2
            result = result + copied
            # 1, 3으로 보내는 것 추가
            result = result + [[1, 3]]
            # move(n-1)에서 1->2, 2->1로 바꿈
            for i in range(len(copied_2)):
                for j in range(2):
                    if copied_2[i][j] == 1:
                        copied_2[i][j] = 2
                    elif copied_2[i][j] == 2:
                        copied_2[i][j] = 1
            result = result + copied_2
            return result
    process = move(N)
    for i in process:
        print(i[0], i[1])
