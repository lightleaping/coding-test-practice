# 문제 설명
# 정수 배열 arr와 2차원 정수 배열 queries이 주어집니다.

# queries의 원소는 각각 하나의 query를 나타내며,
# [s, e] 꼴입니다.

# 각 query마다 순서대로 s ≤ i ≤ e인 모든 i에 대해
# arr[i]에 1을 더합니다.

# 위 규칙에 따라 queries를 처리한 이후의 arr를 return 하는
# solution 함수를 완성해 주세요.

# 제한사항
# 1 ≤ arr의 길이 ≤ 1,000
# 0 ≤ arr의 원소 ≤ 1,000,000
# 1 ≤ queries의 길이 ≤ 1,000
# 0 ≤ s ≤ e < arr의 길이

def solution(arr: list[int], queries: list[list[int]]):
    for s, e in queries:
        for i in range(e - s + 1):
            i = s + i
            arr[i] += 1
    return arr

# def solution(arr, queries):
#     for i in queries:
#         plus = i[0]
#         while plus <= i[1]:
#             arr[plus] += 1
#             plus += 1
#     return arr
# 정수 배열 arr와 2차원 정수 배열 queries.
# queries의 원소는 각각 하나의 query를 나타내며, [s, e] 꼴.
# 각 query마다 순서대로 s ≤ i ≤ e인 모든 i에 대해 arr[i]에 1을 더합니다.
# 위 규칙에 따라 queries를 처리한 이후의 arr를 return