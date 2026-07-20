# 문제 설명
# 정수 리스트 num_list와 정수 n이 주어질 때,
# num_list의 첫 번째 원소부터 마지막 원소까지
# n개 간격으로 저장되어있는 원소들을
# 차례로 담은 리스트를 return하도록
# solution 함수를 완성해주세요.

# 제한사항
# 5 ≤ num_list의 길이 ≤ 20
# 1 ≤ num_list의 원소 ≤ 9
# 1 ≤ n ≤ 4

def solution(num_list: list[int], n: int):
    return num_list[::n]

# 인덱스는 0부터 시작하므로, 0, n, 2n, ...

# def solution(num_list, n):
#     answer = []
#     for i in range(len(num_list)):
#         if n * i > len(num_list) - 1:
#             break
#         answer.append(num_list[n * i])
#     return answer