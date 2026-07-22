# 문제 설명
# 정수 배열 arr가 주어집니다.

# arr의 각 원소에 대해
# 값이 50보다 크거나 같은 짝수라면 2로 나누고,
# 50보다 작은 홀수라면 2를 곱하고 다시 1을 더합니다.

# 이러한 작업을 x번 반복한 결과인 배열을 arr(x)라고 표현했을 때,
# arr(x) = arr(x + 1)인 x가 항상 존재합니다.

# 이러한 x 중 가장 작은 값을 return 하는
# solution 함수를 완성해 주세요.

# 단, 두 배열에 대한 "="는 두 배열의 크기가 서로 같으며,
# 같은 인덱스의 원소가 각각 서로 같음을 의미합니다.

# 제한사항
# 1 ≤ arr의 길이 ≤ 1,000,000
# 1 ≤ arr의 원소의 값 ≤ 100

def solution(arr: list[int]):

    arr_changed = arr.copy()
    count = 0

    while True:

        for i in range(len(arr)):
            if arr[i] >= 50 and arr[i] % 2 == 0:
                arr_changed[i] = arr[i] // 2
            elif arr[i] < 50 and arr[i] % 2 == 1:
                arr_changed[i] = arr[i] * 2 + 1

        arr_equal_lst = []

        # arr == arr_changed를 풀어썼다.
        if len(arr) == len(arr_changed):
            for j in range(len(arr)):
                if arr[j] == arr_changed[j]:
                    arr_equal_lst.append(True)
                else:
                    arr_equal_lst.append(False)

            # 리스트가 아니므로 not in을 사용할 수 없다.
            # 모든 원소가 True인지 확인하려면
            # if all(arr_equal_list):
            # 또는 if arr == arr_changed:
            if all(arr_equal_lst):
                return count

        count += 1          
        arr = arr_changed.copy()

# def solution(arr):
#     count = 0

#     while True:
#         arr_changed = []

#         for x in arr:
#             if x >= 50 and x % 2 == 0:
#                 arr_changed.append(x // 2)
#             elif x < 50 and x % 2 == 1:
#                 arr_changed.append(x * 2 + 1)
#             else:
#                 arr_changed.append(x)

#         if arr == arr_changed:
#             return count

#         arr = arr_changed
#         count += 1
    
            
# def solution(arr):
#     count = 0
#     new_arr = []
#     while True:
#         for i in range(len(arr)):
#             if arr[i] >= 50 and arr[i] % 2 == 0:
#                 new_arr.append(arr[i] / 2)
#             elif arr[i] < 50 and arr[i] % 2 == 1:
#                 new_arr.append(arr[i] * 2 + 1)
#             else:
#                 new_arr.append(arr[i])
#         count += 1
#         if arr == new_arr:
#             # arr을 바꾼 것이 new_arr과 같으므로
#             # arr은 count - 1 일때 arr(x) = arr(x + 1)이다. 
#             return count - 1
#         else:
#             arr = new_arr
#             new_arr = []
    