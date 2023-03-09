def solution(a, b):
    l = [a, b]
    l.sort()
    answer = 0
    for i in range(l[0], l[1]+1, 1) :
        answer += i
    return answer