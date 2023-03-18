def solution(array, commands):
    answer = []
    for i in range(len(commands)) :
        ar = []
        ar = array[commands[i][0]-1:commands[i][1]]
        ar.sort()
        answer.append(ar[commands[i][2]-1])
    return answer