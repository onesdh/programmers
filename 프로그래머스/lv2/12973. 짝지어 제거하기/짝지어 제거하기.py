def solution(s):
    answer = -1
    k = []
    for i in s :
        if len(k) == 0:
            k.append(i)
        elif k[-1] == i :
            k.pop()
        else :
            k.append(i)
    if len(k) == 0 :
        answer = 1
    else :
        answer = 0
    return answer