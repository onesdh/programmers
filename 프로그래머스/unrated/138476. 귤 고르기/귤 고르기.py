
def solution(k, tangerine):
    answer = 0
    tangerine.sort()
    ar = []
    sum = 0
    j = 0
    for i in range(len(tangerine)) :
        if i == 0 :
            j +=1
            if i == len(tangerine)-1:
                ar.append(j)
        elif tangerine[i] == tangerine[i-1] :
            j +=1
            if i == len(tangerine)-1:
                ar.append(j)
        elif tangerine[i] != tangerine[i-1] :
            ar.append(j)
            j =1
            if i == len(tangerine)-1:
                ar.append(j)
    ar.sort(reverse = True)
    while sum < k :
        sum += ar[answer]
        answer += 1
    return answer
        
        