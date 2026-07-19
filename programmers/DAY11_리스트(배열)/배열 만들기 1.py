# 문제 설명
# 정수 n과 k가 주어졌을 때,
# 1 이상 n이하의 정수 중에서 k의 배수를 오름차순으로 저장한 배열을
# return 하는 solution 함수를 완성해 주세요.

# 제한사항
# 1 ≤ n ≤ 1,000,000
# 1 ≤ k ≤ min(1,000, n)

def solution(n: int, k: int):
    
    result = []
    
    for i in range(n):
        if (i + 1) % k == 0:
            result.append(i + 1)
    result.sort()

    return result

# def solution(n, k):
#     answer = []
#     num = 1
#     while (num <= n):
#         if num % k == 0:
#             answer.append(num)
#         num += 1
#     return answer