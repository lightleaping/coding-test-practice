# 문제 설명
# 정수 배열 arr와 2차원 정수 배열 queries이 주어집니다.
# queries의 원소는 각각 하나의 query를 나타내며, [s, e, k] 꼴입니다.

# 각 query마다 순서대로 s ≤ i ≤ e인 모든 i에 대해 k보다 크면서 가장 작은 arr[i]를 찾습니다.

# 각 쿼리의 순서에 맞게 답을 저장한 배열을 반환하는 solution 함수를 완성해 주세요.
# 단, 특정 쿼리의 답이 존재하지 않으면 -1을 저장합니다.

# 제한사항
# 1 ≤ arr의 길이 ≤ 1,000
# 0 ≤ arr의 원소 ≤ 1,000,000
# 1 ≤ queries의 길이 ≤ 1,000
# 0 ≤ s ≤ e < arr의 길이
# 0 ≤ k ≤ 1,000,000

def solution(arr: list[int], queries: list[list[int]]):
    
    min_arr = []

    for query in queries:
        s = query[0]
        e = query[1]
        k = query[2]
        
        arr_bigger_than_k = []

        # e ~ s 둘 다 포함 개수만큼 반복, 코드는 s부터 시작
        for i in range(e - s + 1):
            if k < arr[i + s]:
                arr_bigger_than_k.append(arr[i + s])

        # min() 함수는 주어진 반복 가능한 객체에서 가장 작은 값을 반환하며,
        # 비어 있을 경우 default 인자로 지정한 값을 반환
        min_arr.append(min(arr_bigger_than_k, default=-1))

    return min_arr

# def solution(arr, queries):
#     results = []
    
#     for query in queries:
#         s, e, k = query
        
#         # min_val = float('inf')는 최소값을 찾기 위한 초기값 설정으로,
#         # "처음엔 무한대라고 가정하고, 
#         # 이후 실제 값들과 비교하면서 더 작은 값을 갱신한다"
#         min_val = float('inf')
#         found = False
        
#         for i in range(s, e + 1):
#             if arr[i] > k and arr[i] < min_val:
#                 min_val = arr[i]
#                 found = True
        
#         if found:
#             results.append(min_val)
#         else:
#             results.append(-1)
    
#     return results