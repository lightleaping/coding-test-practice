# 문제 설명
# 정수 리스트 num_list가 주어집니다.
# 가장 첫 번째 원소를 1번 원소라고 할 때,
# 홀수 번째 원소들의 합과 짝수 번째 원소들의 합 중 큰 값을
# return 하도록 solution 함수를 완성해주세요.
# 두 값이 같을 경우 그 값을 return합니다.

# 제한사항
# 5 ≤ num_list의 길이 ≤ 50
# -9 ≤ num_list의 원소 ≤ 9

def solution(num_list: list[int]):
    odd_list = num_list[::2]
    even_list = num_list[1::2]

    sum_odd = 0
    sum_even = 0

    for odd in odd_list:
        sum_odd += odd

    for even in even_list:
        sum_even += even
    
    # max( , ) 가능.
    if sum_odd > sum_even:
        return sum_odd
    else:
        return sum_even
    

# def solution(num_list):
#     odd = sum(num_list[0::2])
#     even = sum(num_list[1::2])
#     if odd >= even:
#         answer = odd
#     else: answer = even
#     return answer

# list[int] 에 sum()을 하면 list 내부 int의 합이 반환된다.

# 정수 리스트 num_list가 주어집니다.

# 가장 첫 번째 원소를 1번 원소라고 할 때,
# => 인덱스 0인 원소가 1번 원소

# 홀수 번째 원소들의 합과 짝수 번째 원소들의 합 중 큰 값
# 두 값이 같을 경우 그 값을 return합니다.

# => 짝수 인덱스(0, 2, ..)가 홀수 번째 원소,
# 홀수 인덱스(1, 3, ..)가 짝수 번째 원소

# => 리스트 슬라이싱, odd = sum(num_list[0::2]),
# even = sum(num_list[1::2])

# if odd >= even:
# answer = odd
# else: answer = even
    
