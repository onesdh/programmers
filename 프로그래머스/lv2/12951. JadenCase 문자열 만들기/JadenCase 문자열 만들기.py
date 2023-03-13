def solution(s):
    answer = ''
    cnt = 1
    for i in s :
        if cnt == 1 and i.isalpha() :
            answer += i.upper()
            cnt += 1
        elif i == " " :
            answer += i
            cnt = 1
        else :
            answer += i.lower()
            cnt+=1
        
    return answer