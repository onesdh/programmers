def solution(answers):
    answer = []
    a_1 = [1, 2, 3, 4, 5]
    a_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    a_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    c_1 = 0
    c_2 = 0
    c_3 = 0
    while True :
        if len(answers) > len(a_1) :
            a_1 += a_1
        elif len(answers) > len(a_2) :
            a_2 += a_2
        elif len(answers) > len(a_3) :
            a_3 += a_3
        if len(answers) <= len(a_1) and len(answers) <= len(a_2) and len(answers) <= len(a_3) :
            break
    print(a_3, answers)
    for i in range(len(answers)) :
        print(answers[i], a_3[i])
        if answers[i] == a_1[i] :
            c_1 += 1
        if answers[i] == a_2[i] :
            c_2 += 1
        if answers[i] == a_3[i] :
            c_3 += 1
            print(answers[i], a_3[i])
    ar = [c_1, c_2, c_3]
    print(ar)
    mx = max(ar)
    for i in range(len(ar)) :
        if mx == ar[i] :
            answer.append(i+1)
    return answer