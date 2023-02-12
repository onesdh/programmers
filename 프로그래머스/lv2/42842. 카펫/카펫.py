def solution(brown, yellow):
    num = []
    sum = brown + yellow
    for i in range(1, yellow+1) :
        if yellow % i == 0 :
            num.append(i)

    for i in range(yellow) :
        y_x = num[len(num)//2 - i]
        if (y_x+2)*(sum//(y_x+2)) == sum and y_x+2 >=sum//(y_x+2):     
            return [y_x+2, sum//(y_x+2)]   