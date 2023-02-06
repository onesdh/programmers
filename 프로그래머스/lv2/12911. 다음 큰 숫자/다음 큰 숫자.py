def solution(n):
    answer = 0
    c_bin = bin(n).count("1")
    answer = n +1
    c_b = bin(answer).count("1")
    while c_b != c_bin:
        answer += 1
        c_b = bin(answer).count("1")
    return answer