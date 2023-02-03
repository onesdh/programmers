def solution(s):
    answer = True
    cnt = 0
    for i in s :
        if i == "(" :
            cnt += 1
        elif i == ")" :
            cnt -= 1
        if cnt == -1 :
            return False
    if cnt == 0 and s[0] != ")" and s[-1] != "(" :
        pass
    else :
        answer = False
    return answer