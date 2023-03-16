def solution(sizes):
    answer = 0
    total_mx = 0
    total_mn = 0
    for i in sizes :
        mx = max(i)
        mn = min(i)
        total_mx = max(total_mx, mx)
        total_mn = max(total_mn, mn)
    answer = total_mx * total_mn
    return answer