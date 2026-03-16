# 해시 테이블 - 민균이의 비밀번호 (백준 브론즈1)
# 문제 링크: https://www.acmicpc.net/problem/9933
N = int(input())
words = [list(map(str, input())) for _ in range(N)]

def find_password(words):
    for word in words:
        reversed_word = word[::-1]
        if reversed_word in words:
            print(len(word), word[len(word)//2])
            return
            
find_password(words)