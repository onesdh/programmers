def solution(nums):
    answer = 0
    l = []
    for i in range(len(nums)) :
        for j in range(i+1, len(nums)) :
            for q in range(j+1, len(nums)):
                l.append(nums[i] + nums[j] + nums[q])
    for i in l :
        if sol(i) == 2 :
            print(i)
            answer += 1
    
    

    return answer

def sol(num) :
    cnt = 0
    for i in range(1, int(num**(1/2))+1) :
        if num == i**2 :
            cnt+=1
        elif num % i == 0 :
            cnt +=2
    return cnt
