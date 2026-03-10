# 정수론 - 골드바흐의 추측 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/9020
import math

T = int(input())
testCase = [int(input()) for _ in range(T)]

def find_prime_number(num):
    if num == 0:
        return False
    elif num == 1:
        return False
    elif num == 2:
        return True
    elif num == 3:
        return True
    elif num % 2 != 0:
            for j in range(3, num, 2):
                if num % j == 0:
                    return False
            else:
                return True 
    else:
        return False

for number in testCase:
    i = int(number / 2)
    if i % 2 != 0 or i == 2:
        while i >= 2:
            if (find_prime_number(i)) and (find_prime_number(number - i)):
                print(str(i) + " " + str(number - int(i)))
                break
            i -= 2
    else:
        i -= 1
        while i >= 2:
            if (find_prime_number(i)) and (find_prime_number(number - i)):
                print(str(i) + " " + str(number - int(i)))
                break
            i -= 2
 