def solution(number):
    answer = 0
    li = []
    lu = []
    for i in range(0, len(number)) :
        for j in range(i+1, len(number)) :
            for q in range(j+1, len(number)) :
                if number[i] + number[j] + number[q] == 0 :
                    n = [number[i] ,number[j] , number[q]]
                    n.sort()
                    li.append(n)
    # for i in li :
    #     if i in lu :
    #         pass 
    #     else :
    #         lu.append(i)
    answer = len(li)
    return answer