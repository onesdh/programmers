def solution(nums):
    answer = 0
    k = []
    for i in nums :
        if i not in k :
            k.append(i)
    answer = min(len(k), len(nums)//2)
    return answer