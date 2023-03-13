def solution(s):
    answer = []
    cnt = 0
    re_cnt = 0
    while s != "1" :
        cnt += s.count("0")
        s = "1"*(len(s) - s.count("0"))
        s = bin(len(s))[2:]
        re_cnt += 1
    answer = [re_cnt, cnt]
    return answer