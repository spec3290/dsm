def solution(num_list):
    answer = 0;
    a = [x for x in num_list if x%2==1]
    b = [x for x in num_list if x%2==0]
    a = map(str, a)
    b = map(str, b)
    a = "".join(a)
    b = "".join(b)
    return int(a)+int(b)