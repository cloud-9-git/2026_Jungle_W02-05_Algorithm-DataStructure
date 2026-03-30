# 그리디 - 잃어버린 괄호 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/1541

"""
세준이는 양수와 +, -, 그리고 괄호를 가지고 식을 만들었다. 그리고 나서 세준이는 괄호를 모두 지웠다.
그리고 나서 세준이는 괄호를 적절히 쳐서 이 식의 값을 최소로 만들려고 한다.
괄호를 적절히 쳐서 이 식의 값을 최소로 만드는 프로그램을 작성하시오.

입력
첫째 줄에 식이 주어진다. 식은 ‘0’~‘9’, ‘+’, 그리고 ‘-’만으로 이루어져 있고, 가장 처음과 마지막 문자는 숫자이다.
그리고 연속해서 두 개 이상의 연산자가 나타나지 않고, 5자리보다 많이 연속되는 숫자는 없다.
수는 0으로 시작할 수 있다. 입력으로 주어지는 식의 길이는 50보다 작거나 같다.

출력
첫째 줄에 정답을 출력한다.

예제 입력 1 
55-50+40
예제 출력 1 
-35
예제 입력 2 
10+20+30+40
예제 출력 2 
100
예제 입력 3 
00009-00009
예제 출력 3 
0
"""

sentence = input()

mSplit = sentence.split('-')
group_sums = []

for i in range(0, len(mSplit)):
    group_sums.append(sum(map(int, mSplit[i].split('+'))))

result = group_sums[0]
for i in range(1, len(group_sums)):
    result = result - group_sums[i]

print(result)

'''
import sys

# 입력을 더 빠르게 받기 위해 sys.stdin.readline 사용 (백준 습관)
sentence = sys.stdin.readline().strip()

# '-'를 기준으로 나눈 뒤, 각 그룹의 합을 구합니다.
# 리스트 컴프리헨션을 사용하면 코드가 더 간결해집니다.
groups = [sum(map(int, part.split('+'))) for part in sentence.split('-')]

# 첫 번째 그룹 값에서 나머지 모든 그룹의 합을 빼줍니다.
# 언패킹(*)을 활용해 첫 원소와 나머지를 분리할 수 있습니다.
first_val, *rest_vals = groups
result = first_val - sum(rest_vals)

print(result)
'''