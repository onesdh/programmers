def solution(n):
    l = list(str(n))
    l = map(int, l)
    l_sum = sum(l)
    if n % l_sum == 0 :
        return True
    return False 