def solution(n):
    ans = 0
    for i in range(0,n+1,2):
        ans+=i
    return ans