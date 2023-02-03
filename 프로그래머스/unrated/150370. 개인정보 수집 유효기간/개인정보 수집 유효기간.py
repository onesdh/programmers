def solution(today, terms, privacies) :
    answer = []
    
    #today  
    year , month , day = map(int, today.split('.'))
    today_term = (year*12*28) + (month*28) + day
    
    #terms
    term_ = dict()
    for te in terms :
        te = te.split()
        term_[te[0]] = int(te[1])*28



    #privacies
    for i in range(len(privacies)) :
        date, term = privacies[i].split()
        year_ , month_ , day_ = map(int, date.split('.'))
        privacies_term = (year_*12*28) + (month_*28) + day_
        if privacies_term + term_[term] <= today_term :
            answer.append(i+1)
            
    return answer