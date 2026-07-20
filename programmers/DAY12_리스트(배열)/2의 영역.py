# 문제 설명
# 정수 배열 arr가 주어집니다.
# 배열 안의 2가 모두 포함된 가장 작은 연속된 부분 배열을
# return 하는 solution 함수를 완성해 주세요.

# 단, arr에 2가 없는 경우 [-1]을 return 합니다.

# 제한사항
# 1 ≤ arr의 길이 ≤ 100,000
# 1 ≤ arr의 원소 ≤ 10

def solution(arr:list[int]):
    
    lst_index = []

    for i in range(len(arr)):
        if arr[i] == 2:
            lst_index.append(i)
    
    if lst_index == []:
        return [-1]
    
    return arr[lst_index[0] : lst_index[-1] + 1]

# def solution(arr):
#     answer = []
#     where = []
#     for i in range(len(arr)):
#         if arr[i] == 2:
#             where.append(i)
#     if len(where) == 1:
#         answer.append(2)
#     elif len(where) >= 2:
#         for j in range(where[0], where[-1] + 1):
#             answer.append(arr[j])
#     elif where == []:
#         answer.append(-1)
#     return answer