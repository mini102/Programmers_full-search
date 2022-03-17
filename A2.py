from itertools import permutations

def solution(numbers):
    answer = 0
    # print(list(numbers))
    listy = []
    ans = []
    #print(len(numbers))
    for i in range(1,len(numbers)+1):
        listy.append(list(map(''.join, permutations(list(numbers),i))))
    
    listy = list(set([int(element) for array in listy for element in array]))
    #print(listy)

    for n in listy:
        if n > 1:
            for i in range(2, n): #n은 소수 판별하고자 하는 수
                if n % i == 0:
                    ans.append(n) #소수아님
                    break
        else:
              ans.append(n)    
    #print(ans)
    return len(listy)-len(ans)
