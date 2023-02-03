def solution(s):
    answer = ''
    k = list(map(int, s.split()))
    ma = max(k)
    mi = min(k)
    answer = str(mi) + " " +  str(ma)
    return answer