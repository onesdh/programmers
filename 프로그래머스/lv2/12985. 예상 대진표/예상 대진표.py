def solution(n,a,b):
    answer = 1
    # k = [a, b]
    # m = min(k)
    # if m % 2 == 1 and abs(a-b) == 1 :
    #     return answer

    while (a+1)//2 != (b+1)//2 :
        answer += 1
        a, b = (a+1)//2, (b+1)//2
    return answer