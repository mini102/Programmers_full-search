import numpy as np

def solution(answers):
    answer = []
    listy = []
    first = [1, 2, 3, 4, 5]
    second = [2, 1, 2, 3, 2, 4, 2, 5]
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    n =len(answers)
    
    while len(first)!=n:
        first += first
        if len(first)>n:
            first = first[:n]
            break
            
    while len(second)!=n:
        second += second
        if len(second)>n:
            second = second[:n]
            break
            
    while len(third)!=n:
        third += third
        if len(third)>n:
            third = third[:n]
            break
            
    first = np.array(first)
    second = np.array(second)
    third = np.array(third)
    
    answers = np.array(answers)
    first = first - answers
    second = second - answers
    third = third - answers
    
    listy.append(list(first).count(0))
    listy.append(list(second).count(0))
    listy.append(list(third).count(0))
    
    # print(listy)
    for idx,i in enumerate(listy):
        if i == max(listy):
            answer.append(idx+1)
    
    return answer
