# 배열 - 평균은 넘겠지 (백준 브론즈1)
# 문제 링크: https://www.acmicpc.net/problem/4344

C = int(input())
testCase = [list(map(int, input().split())) for _ in range(C)]

for i in range(len(testCase)):
    sum_score = 0
    avg_score = 0
    over_agv_student = 0
    for j in range(1, len(testCase[i])):
        sum_score = sum_score + testCase[i][j]
    avg_score = sum_score / testCase[i][0]
    for j in range(1, len(testCase[i])):
        if testCase[i][j] > avg_score:
            over_agv_student += 1
    percent = f"{(over_agv_student / testCase[i][0] * 100): .3f}"
    print(percent+"%")
