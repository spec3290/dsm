n, m, k = map(int, input().split())
team = min(n//2, m)

remaining = n+m-team*3

while k>remaining :
    team-=1
    remaining+=3

print(team)
    