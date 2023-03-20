def solution(strings, n):
    answer = []
    ar = []
    for i in strings :
        ar.append(i[n]+i)
        

    ar.sort()
    for i in ar :
        answer.append(i[1:])
    return answer