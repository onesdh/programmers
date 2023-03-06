def sol(num) :
    cnt = 0
    for i in range(1, int(num**(1/2))+1) :
        if num == i**2 :
            cnt+=1
        elif num % i == 0 :
            cnt +=2
    return cnt


def solution(number, limit, power):
    answer = 0

    for i in range(1, number+1) :
        k = sol(i)
        if limit < k :
            answer += power
        else :
            answer += k

    return answer

  
