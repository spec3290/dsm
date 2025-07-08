def solution(num_list):
    oddcnt=0
    evencnt=0
    for i in num_list:
        if i%2==0:
            oddcnt+=1
        elif i%2==1:
            evencnt+=1
    return [oddcnt,evencnt]