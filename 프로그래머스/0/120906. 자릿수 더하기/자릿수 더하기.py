def solution(n):
    u = str(n)
    v = 0
    for i in range(len(u)):
        v+=int(u[i])

    return v