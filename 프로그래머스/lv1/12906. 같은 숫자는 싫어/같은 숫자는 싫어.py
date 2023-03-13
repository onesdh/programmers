def solution(arr):
    answer = []
    cnt = 0
    for i in arr :
        if cnt == 0 :
            answer.append(i)
            cnt += 1
        elif i == answer[-1] :
            pass
        else :
            answer.append(i)
    return answer