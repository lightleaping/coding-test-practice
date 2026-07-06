# 문제 설명
# 정수 l과 r이 주어졌을 때,
# l 이상 r이하의 정수 중에서
# 숫자 "0"과 "5"로만 이루어진 모든 정수를
# 오름차순으로 저장한 배열을 return 하는 solution 함수를 완성해 주세요.

# 만약 그러한 정수가 없다면, -1이 담긴 배열을 return 합니다.

# 제한사항
# 1 ≤ l ≤ r ≤ 1,000,000

def solution(l: int, r: int):

    result =[]

    for digit in range(l, r + 1):

        # "0" 또는 "5"라는 한 자리 문자열이
        # "05" 안에 포함되어 있는지를 확인합니다.
        # 즉, str(digit)이 "0"이거나 "5"일 때
        # 조건이 참(True)이 됩니다.
        # 즉, if str(digit) in '05': 는
        # digit이 "0" 또는 "5"일 때만 참이 됩니다.
        #
        #  "숫자 안에 0과 5만 포함된 경우"라면
        if all(ch in '05' for ch in str(digit)):
            result.append(digit)

    # result는 리스트로 초기화했기 때문에 None이 될 수 없습니다.
    # 비어 있는지 확인하려면 if not result: 로 써야 합니다.
    if not result:
        return [-1]
    
    # 파이썬에서 배열을 오름차순으로.
    # 방법 1: sort() 메서드 (원본 배열 자체를 정렬)
    # 방법 2: sorted() 함수 (새로운 정렬된 배열 반환)
    #
    # result.sort()는 리스트를 정렬하지만 반환값은 None입니다.
    return sorted(result)

# def is_valid(number):
#     for digit in str(number):
#         if digit not in '05':
#             return False
#     return True

# def solution(l, r):
#     result = []
    
#     for num in range(l, r + 1):
#         if is_valid(num):
#             result.append(num)
    
#     if not result:
#         return [-1]
    
#     return result