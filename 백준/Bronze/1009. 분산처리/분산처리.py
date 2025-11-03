import sys
# 입력의 효율성을 위해 sys.stdin.read 사용
input = sys.stdin.read

def solve_simple():
    """
    T개의 테스트 케이스를 입력받아, a^b의 일의 자릿수(컴퓨터 번호)를 출력합니다.
    """
    data = input().split()
    if not data:
        return
        
    T = int(data[0])
    results = []
    
    # 1. T번 반복하며 a와 b를 입력받음
    for i in range(1, T * 2, 2):
        try:
            a = int(data[i])
            b = int(data[i+1])
        except IndexError:
            break

        # 2. 밑(base) 정리: a의 일의 자리만 사용
        base = a % 10
        
        # 3. base가 0인 경우: 결과는 항상 10번 컴퓨터
        if base == 0:
            results.append(10)
            continue
        
        # 4. 지수(exponent) 정리: 최대 주기 4 활용
        # b를 4로 나눈 나머지가 0이면 4 (주기의 마지막)로 설정
        exponent = b % 4
        if exponent == 0:
            exponent = 4
        
        # 5. 거듭제곱의 일의 자리 계산
        # result = (base ** exponent) % 10
        result = 1
        for _ in range(exponent):
            result = (result * base) % 10

        # 6. 최종 컴퓨터 번호 결정
        # 일의 자리는 1~9이므로, 그대로 컴퓨터 번호가 됨
        results.append(result)

    # 모든 결과를 한 번에 출력
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

solve_simple()