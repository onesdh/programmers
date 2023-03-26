def solution(e):
    answer = 0
    e_ = e*3
    l = []
    a = 0
    i = 0 # index
    k = 0 # 회전수
    c = 1 # 원소합 개수
    while True :
        if k < len(e) : # a생성
            a = e_[i:i+c]
            l.append(sum(a))
            i+=1
            k +=1
        if k == len(e) : # 1회전시 다음 단계 이동
            k = 0
            i = 0
            c +=1
            
        if c == len(e)+1: # 종료
            break

    l = set(l)
    answer = len(l)
    return answer