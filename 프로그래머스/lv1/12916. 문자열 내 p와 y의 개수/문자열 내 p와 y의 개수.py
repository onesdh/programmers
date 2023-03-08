def solution(s):
    answer = True
    s = s.lower()
    p_cnt, y_cnt = 0, 0
    for i in s :
        if i == "p" :
            p_cnt += 1
        elif i == "y" :
            y_cnt += 1

    if p_cnt == y_cnt :
        answer = True
    else :
        answer = False
    return answer