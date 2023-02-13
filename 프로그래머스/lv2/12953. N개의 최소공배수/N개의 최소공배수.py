def sol(n) :
    for i in range(2, n+1) :
        if n % i == 0 :
            return i


def solution(arr):
    answer = 1
    arr.sort(reverse = True)
    mx = max(arr)
    while True :
        k = sol(arr[0])
        for j in range(len(arr)) :
            if arr[j]%k == 0 :
                arr[j] = int(arr[j] / k)
        answer *= k
        #print(answer)
        arr.sort(reverse = True)
        if sum(arr) == len(arr) :
            return answer
