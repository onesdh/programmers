def solution(food):
    answer = ''
    for i in range(len(food)) :
        answer = answer + str(i) * int(food[i]//2)
    answer_re = answer[::-1]
    answer = answer + str(0) + answer_re


    return answer
