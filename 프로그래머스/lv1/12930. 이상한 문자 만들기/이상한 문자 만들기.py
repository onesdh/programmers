def solution(s):
    answer = ''
    s = s.split(" ")
    for i in s :
        for j in range(len(i)) :
            if j % 2 == 0 :
                answer += i[j].upper()
            else :
                answer += i[j].lower()
        answer += " "
    answer = answer [0:len(answer)-1]
    return answer