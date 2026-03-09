# 문자열 - 단어 공부 (백준 브론즈1)
# 문제 링크: https://www.acmicpc.net/problem/1157

word = input()
upper_word = word.upper()

seen = {}
result = []

for char in upper_word:
    if char not in seen:
        seen[char] = 1
        continue
    elif char in seen:
        seen[char] = seen[char] + 1
max_count = max(seen.values())

for key, value in seen.items():
    if value == max_count:
        result.append(key)

if len(result) == 1:
    print(result[0])
else:
    print('?')
        

