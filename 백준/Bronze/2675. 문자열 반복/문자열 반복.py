nu = int(input())

for i in range(nu):
    n, s = map(str, input().split())
    n = int(n)
    s = list(s)
    for j in range(len(s)):
        print(s[j] * n, end='')
    print()