def solution(n, arr1, arr2):
    answer = []

    ar1 = sol(n, arr1)
    print(ar1)
    ar2 = sol(n, arr2)
    ar = []
    for i in range(n) :
        k = ""
        for j in range(n) :
            a = int(ar1[i][j]) + int(ar2[i][j])
            k += str(a)
        ar.append(k)
    for i in range(n) :
        k = ""
        for j in range(n) :
            if int(ar[i][j]) > 0:
                k += "#"
            else :
                k += " "
        answer.append(k)
    return answer
def sol(n, arr) :
    ans = []
    for i in arr :
        a = bin(i)
        if len(a[2:]) < n :
            k = "0" * (n-len(a[2:])) + a[2:]
            ans.append(k)
        else :
            ans.append(a[2:])
    return ans