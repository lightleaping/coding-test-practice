# 문제 설명
# 양의 정수 n이 매개변수로 주어질 때,
# n이 홀수라면 n 이하의 홀수인 모든 양의 정수의 합을 return 하고
# n이 짝수라면 n 이하의 짝수인 모든 양의 정수의 제곱의 합을
# return 하는 solution 함수를 작성해 주세요.

# 제한사항
# 1 ≤ n ≤ 100

def solution(n: int):
    if n % 2 == 1:
        odd = 1
        odd_sum = 0
        while True:
            if odd > n:
                break
            odd_sum += odd
            odd += 2
        result = odd_sum

    else:
        even = 2
        even_sum = 0
        while True:
            if even > n:
                break
            even_sum += even ** 2
            even += 2
        result = even_sum

    return result

# def solution(n):
#     answer = 0
#     if n % 2 == 1:
#         num = 1
#         while True:
#             answer += num
#             if num == n:
#                 break
#             num += 2
#     else:
#         num = 2
#         while True:
#             answer += num ** 2
#             if num == n:
#                 break
#             num += 2
#     return answer