def solution(angle):
    if(angle<90):
        return 1
    elif(90<angle and angle<180):
        return 3
    elif(angle==90):
        return 2
    else:
        return 4
    