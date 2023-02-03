def solution(k, score):
    answer = []
    award = []
    for i in score :
        award.append(i)
        award.sort()
        award.reverse()
        if len(award) > k :
            del award[k]
        answer.append(award[-1])
    return answer
