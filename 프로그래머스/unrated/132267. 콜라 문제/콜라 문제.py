def solution(a, b, n):
    answer = 0
    while n >= a:
        k = n // a 
        q = n % a
        answer += k * b
        n = q + k * b
    return answer