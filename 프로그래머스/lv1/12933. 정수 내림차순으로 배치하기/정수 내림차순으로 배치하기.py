

def solution(n):
    n = str(n)
    answer = "".join(sorted(n))
    answer = answer[::-1]
    return int(answer)