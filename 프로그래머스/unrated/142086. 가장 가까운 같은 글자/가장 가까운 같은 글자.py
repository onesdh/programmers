def solution(s):
    answer = []
    dic = dict()
    for i, letter in enumerate(s) :
        if letter not in dic :
            answer.append(-1)
            dic[letter] = i
        else :
            print(i, dic[letter])
            answer.append(i-dic[letter])
            dic[letter] = i
    return answer