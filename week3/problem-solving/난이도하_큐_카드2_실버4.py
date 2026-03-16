# 큐 - 카드2 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/2164
from collections import deque

N = int(input())

cards = deque(range(1, N+1))

while len(cards) > 1:
    cards.popleft()
    cards.append(cards.popleft())

print(cards[0])
