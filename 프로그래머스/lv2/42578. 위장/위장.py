from collections import defaultdict
def solution(clothes):
    answer = 1
    dic = defaultdict(list)
    
    for i in range(len(clothes)) :
        j = " ".join(clothes[i])
        li = list(map(str, j.split(" ")))
        dic[li[1]].append(li[0])
    if len(dic.keys()) == 1 :
        answer = len(clothes)
    else :
        for i in dic :
            answer *= (len(dic[i]) + 1)
        answer -= 1
    return answer

