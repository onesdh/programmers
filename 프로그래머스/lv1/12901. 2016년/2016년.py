def solution(a, b):
    answer = ''
    days = 0
    week = {1 : "FRI", 2 : "SAT", 3 : "SUN", 4 : "MON", 5 : "TUE", 6 : "WED", 0 : "THU" }
    month = {1: 31, 2:29, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    for i in range(1, a):
        days += month[i]
    days += b 
    answer = week[days % 7]
        
    return answer