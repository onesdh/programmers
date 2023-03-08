def solution(x, n):
    answer = []
    for i in range(0,n, 1) :
        answer.append(x+i*x)
    return answer