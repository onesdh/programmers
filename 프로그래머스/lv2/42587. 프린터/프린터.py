"""1. 인쇄 대기목록의 가장 앞에 있는 문서(J)를 대기목록에서 꺼냅니다.
2. 나머지 인쇄 대기목록에서 J보다 중요도가 높은 문서가 한 개라도 존재하면 
J를 대기목록의 가장 마지막에 넣습니다.
3. 그렇지 않으면 J를 인쇄합니다."""
def solution(priorities, location):
    answer = 0
    lo = [i for i in range(len(priorities))]
    pr = priorities
    print(pr)
    i = 0
    while True :
        if pr[i] < max(pr[i+1:]) :
            pr.append(pr.pop(i))
            lo.append(lo.pop(i))

        else :
            i += 1
        if pr == sorted(pr, reverse = True) :
            break
    print(pr, lo)
            
    return lo.index(location) + 1