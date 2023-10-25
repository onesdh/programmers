from sys import stdin
N = int(stdin.readline())
arr = []
for _ in range(N):
    arr.append(list(map(int, stdin.readline().split())))

dp = [[0] * N for _ in range(N)]
dp[0][0] = 1

#print(arr)
target = N -1
for i in range(N) :
    for j in range(N) :

        cur = arr[i][j]
        
        if i == target and j == target :
            print(dp[i][j])
            break
        else :        
            if j + cur < N:   # 오른쪽으로 이동하는경우
                dp[i][j + cur] += dp[i][j]

            if i + cur < N:    # 아래로 이동하는 경우
                dp[i + cur][j] += dp[i][j]
