# 문자열 - IPv6 (백준 실버1)
# 문제 링크: https://www.acmicpc.net/problem/3107

#contracted ipv6
ipv6 = input()
#contracted ipv6 with replaced double colon
ipv6_split = list(map(str, ipv6.split('::')))
original_ipv6 = ""
x = 0

for i in range(len(ipv6_split)):
    ipv6_split[i] = list(map(str, ipv6_split[i].split(':')))
    for j in range(len(ipv6_split[i])):
        ipv6_split[i][j] = "0" * (4 - len(ipv6_split[i][j])) + str(ipv6_split[i][j])
        x += 1
if '::' in ipv6:
    if ipv6_split[0] == []:
        original_ipv6 = "0000:" * (8-x) + ":".join(ipv6_split[1])
    if ipv6_split[1] == []:
        original_ipv6 = ":".join(ipv6_split[0]) + ":0000" * (8-x)
    if ipv6_split[0] != [] and ipv6_split[1] != []:
        original_ipv6 = ":".join(ipv6_split[0]) + ":0000" * (8-x) + ":" + ":".join(ipv6_split[1])
else:
    original_ipv6 = ":".join(ipv6_split[0])

print(original_ipv6)


