def solution(s, n):
    answer = ''
    up = "abcdefghijklmnopqrstuvwxyz".upper()
    low = "abcdefghijklmnopqrstuvwxyz"
    for i in s :
        if i in up :
            idx = up.find(i)
            answer += up[(idx+n)%26]
        elif i == " " :
            answer += " "
        else :
            idx = low.find(i)
            answer += low[(idx+n)%26]
    return answer