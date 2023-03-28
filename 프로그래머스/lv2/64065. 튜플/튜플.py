def solution(s):
    answer = []
    s = s.strip("{""}").split("},{")
    s = sorted(s, key=len)
    for i in range(len(s)):
        q = s[i].split(",")
        for j in q :
            if int(j) in answer :
                pass
            else :
                answer.append(int(j))
            

    return answer
