def solution(brown, yellow):
    answer = []
    listy =[]
    for i in range(1,yellow+1):
        if yellow % i == 0:
            listy.append((i,int(yellow/i)))
    #print(listy)
    for i in listy:
        rest = brown-2*i[0]-2*i[1]
        if rest ==4 and i[0]+2>=i[1]+2:
            # print("{},{}".format(i[0],i[1]))
            # print("row: {}".format(i[0]+2))
            # print("col: {}".format(i[1]+2))
            answer.append(i[0]+2)
            answer.append(i[1]+2)
    return answer
