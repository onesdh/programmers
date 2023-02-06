def solution(n):
    fi = [0, 1]
    for i in range(2, n+1) :
        fi.append((fi[i-2] + fi[i-1])%1234567)
    return fi[-1]
