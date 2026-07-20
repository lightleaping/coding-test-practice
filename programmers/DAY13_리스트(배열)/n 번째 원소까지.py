# 문제 설명
# 정수 리스트 num_list와 정수 n이 주어질 때,
# num_list의 첫 번째 원소부터 n 번째 원소까지의 모든 원소를
# 담은 리스트를 return하도록 solution 함수를 완성해주세요.

# 제한사항
# 2 ≤ num_list의 길이 ≤ 30
# 1 ≤ num_list의 원소 ≤ 9
# 1 ≤ n ≤ num_list의 길이 ___

def solution(num_list: list[int], n: int):
    return num_list[:n]

# n 번째 원소까지: 인덱스는 n - 1,
# 슬라이싱 두 번째 원소 - 1 인덱스까지이므로
# n 번째 원소까지 = n

# def solution(num_list, n):
#     answer = []    
#     for i in range(n):
#         answer.append(num_list[i])
#     return answer