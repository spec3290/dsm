def solution(numbers):
    avg = 0
    for i in numbers:
        avg+=i
    return avg/len(numbers)