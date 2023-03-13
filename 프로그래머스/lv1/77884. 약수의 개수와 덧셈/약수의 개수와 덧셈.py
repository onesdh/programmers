def solution(left, right):
    answer = 0
    for i in range(left, right+1) :
        if sol(i) % 2 == 0 :
            answer += i
        else :
            answer -= i
    return answer

def sol(num) :
    cnt = 0
    for i in range(1, int(num**(1/2))+1) :
        if num == i**2 :
            cnt+=1
        elif num % i == 0 :
            cnt +=2
    return cnt