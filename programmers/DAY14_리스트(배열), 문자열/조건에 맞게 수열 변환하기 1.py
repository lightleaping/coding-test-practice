# 문제 설명
# 정수 배열 arr가 주어집니다.

# arr의 각 원소에 대해
# 값이 50보다 크거나 같은 짝수라면 2로 나누고,
# 50보다 작은 홀수라면 2를 곱합니다.

# 그 결과인 정수 배열을 return 하는 solution 함수를 완성해 주세요.

# 제한사항
# 1 ≤ arr의 길이 ≤ 1,000,000
# 1 ≤ arr의 원소의 값 ≤ 100

def solution(arr: list[int]):

    result =[]

    for num in arr:
        if num >= 50 and num % 2 == 0:
            result.append(num // 2)
        elif num < 50 and num % 2 == 1:
            result.append(num * 2)
        else:
            result.append(num)
    
    return result

# 조건에 맞지 않는 원소도 추가해야 한다!!!

# def solution(arr):
#     answer = []
#     for num in arr:
#         if num >= 50 and num % 2 == 0:
#             num = num / 2
#         elif (num < 50 and num % 2 == 1):
#             num = num * 2
#         answer.append(num)
#     return answer