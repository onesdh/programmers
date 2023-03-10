def solution(seoul):
    answer = ''
    cnt = -1
    for i in seoul :
        cnt += 1
        if i == "Kim" :
            return "김서방은 {0}에 있다".format(cnt)