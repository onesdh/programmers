def solution(t, p):
    answer = 0
    l_t = len(t)
    l_p = len(p)
    for i in range(l_t-l_p+1) :
        if int(t[i:i+l_p]) <= int(p) :
            answer += 1

    return answer