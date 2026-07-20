# 문제 설명
# 정수 배열 arr와 2개의 구간이 담긴 배열 intervals가 주어집니다.

# intervals는 항상 [[a1, b1], [a2, b2]]의 꼴로 주어지며
# 각 구간은 닫힌 구간입니다.
# 닫힌 구간은 양 끝값과 그 사이의 값을
# 모두 포함하는 구간을 의미합니다.

# 이때 배열 arr의 첫 번째 구간에 해당하는 배열과
# 두 번째 구간에 해당하는 배열을 앞뒤로 붙여
# 새로운 배열을 만들어 return 하는 solution 함수를 완성해 주세요.

# 제한사항
# 1 ≤ arr의 길이 ≤ 100,000
# 1 ≤ arr의 원소 < 100
# 1 ≤ a1 ≤ b1 < arr의 길이
# 1 ≤ a2 ≤ b2 < arr의 길이

def solution(arr: list[int], intervals: list[list[int]]):
    result = []

    # append(x) : x를 한 개의 요소로 추가
    # extend(x) : x의 요소들을 하나씩 추가
    result.extend(arr[intervals[0][0] : intervals[0][1] + 1])
    result.extend(arr[intervals[1][0] : intervals[1][1] + 1])

    return result

# def solution(arr, intervals):
#     return (arr[intervals[0][0]:intervals[0][1] + 1] + arr[intervals[1][0] : intervals[1][1] + 1])

# def solution(arr, intervals):
#     answer = []
#     for i in range(len(intervals)):
#         start = intervals[i][0]
#         end = intervals[i][1]
#         while (start <= end):
#             answer.append(arr[start])
#             start += 1
#     return answer