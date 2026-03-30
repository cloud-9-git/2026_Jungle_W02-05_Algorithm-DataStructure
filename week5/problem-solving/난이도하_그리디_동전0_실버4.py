# 그리디 - 동전 0 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/11047
'''
문제
준규가 가지고 있는 동전은 총 N종류이고, 각각의 동전을 매우 많이 가지고 있다.
동전을 적절히 사용해서 그 가치의 합을 K로 만들려고 한다. 이때 필요한 동전 개수의 최솟값을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N과 K가 주어진다. (1 ≤ N ≤ 10, 1 ≤ K ≤ 100,000,000)
둘째 줄부터 N개의 줄에 동전의 가치 Ai가 오름차순으로 주어진다. (1 ≤ Ai ≤ 1,000,000, A1 = 1, i ≥ 2인 경우에 Ai는 Ai-1의 배수)

출력
첫째 줄에 K원을 만드는데 필요한 동전 개수의 최솟값을 출력한다.

예제 입력 1 
10 4200
1
5
10
50
100
500
1000
5000
10000
50000
예제 출력 1 
6
예제 입력 2 
10 4790
1
5
10
50
100
500
1000
5000
10000
50000
예제 출력 2 
12
'''

import sys
input = sys.stdin.read().split()

# 첫 번째 값은 n, 두 번째 값은 k
n = int(input[0])
k = int(input[1])

# 그 이후의 값들은 동전 리스트 (이미 오름차순으로 제공됨)
coins = list(map(int, input[2:]))

# 큰 동전부터 계산하기 위해 내림차순 정렬
coins.sort(reverse=True)

def countCoins(k, coins):
    cnt = 0
    change = k
    for coin in coins:
        cnt = cnt + (change // coin)
        change = change % coin
        if change == 0:
            break
    return cnt

print(countCoins(k, coins))

'''
for coin in coins:
    # q는 몫(개수), r은 나머지(남은 돈)
    q, r = divmod(change, coin)
    cnt += q
    change = r
    if change == 0:
        break
'''