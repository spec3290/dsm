def solution(sides):
    sides.sort()
    if sides[2] < sides[1]+sides[0]:
        return 1
    elif sides[2] >= sides[1]+sides[0]:
        return 2