def solution(n):
    answer = 0
    k = n**(1/2)
    if k % 1 == 0 :
        return (k+1)**2
    return -1