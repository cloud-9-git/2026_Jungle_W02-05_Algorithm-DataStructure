# 문자열 - 문자열 반복 (백준 브론즈2)
# 문제 링크: https://www.acmicpc.net/problem/2675

T = int(input())
testCase = [list(map(str, input().split())) for _ in range(T)]


def print_number(i, R, S):
    if i == len(S):
        return
    print(S[i] * int(R), end="")
    print_number(i+1, R, S)

for j in range(len(testCase)):
    print_number(0, testCase[j][0], testCase[j][1])
    print("")
