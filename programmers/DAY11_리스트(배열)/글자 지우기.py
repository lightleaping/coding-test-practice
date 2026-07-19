# 문제 설명
# 문자열 my_string과 정수 배열 indices가 주어질 때,
# my_string에서 indices의 원소에 해당하는
# 인덱스의 글자를 지우고 이어 붙인 문자열을
# return 하는 solution 함수를 작성해 주세요.

# 제한사항
# 1 ≤ indices의 길이 < my_string의 길이 ≤ 100
# my_string은 영소문자로만 이루어져 있습니다
# 0 ≤ indices의 원소 < my_string의 길이
# indices의 원소는 모두 서로 다릅니다.

def solution(my_string: str, indices: list[int]):
    
    indices_reverse_sorted = sorted(indices, reverse=True)
    list_my_string = list(my_string)

    for i in indices_reverse_sorted:
        del list_my_string[i]
    
    return ''.join(list_my_string)

# remove()는 인덱스가 아니라 값을 기준으로 삭제,
# 가장 앞에 있는 해당 값을 삭제한다.

## 방법 1. 삭제할 인덱스를 건너뛰기
## 방법 2. 리스트에서 인덱스로 삭제하기,
# del => 뒤에서부터 삭제해야 한다.

# 1.
# for i, ch in enumerate(my_string):
#   if i not in indices:
#       result += ch

# TypeError: 'str' object doesn't support item deletion

# def solution(my_string, indices):
#     answer = ''
#     for i in range(len(my_string)):
#         if i not in indices:
#             answer += my_string[i]
#     return answer