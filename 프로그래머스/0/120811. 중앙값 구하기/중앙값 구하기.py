def solution(array):
    array.sort()
    new_array = list(reversed(sorted(array)))
    for i in range(len(array)):
        if (array[i]==new_array[i]):
            return array[i]