def solution(n):
    ans = 0
    if n <3 :
        return n %1234567
    else :
        li = [0]*(n+1)
        li[1] = 1
        li[2] = 2
        for i in range(3, n+1) : 
            li[i] = li[i-1] + li[i-2]
    return li[n] % 1234567
