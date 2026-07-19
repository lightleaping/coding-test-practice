# 문제 설명
# 문자열 my_string과 정수 s, e가 매개변수로 주어질 때,
# my_string에서 인덱스 s부터 인덱스 e까지를 뒤집은 문자열을
# return 하는 solution 함수를 작성해 주세요.

# 제한사항
# my_string은 숫자와 알파벳으로만 이루어져 있습니다.
# 1 ≤ my_string의 길이 ≤ 1,000
# 0 ≤ s ≤ e < my_string의 길이

def solution(my_string: str, s: int, e: int):

    if s != 0:
    # 두 번째 슬라이싱 항목은 코드의 인덱스보다 1 넓어진 정수로 반영된다.
        return my_string[:s] + my_string[e : s - 1 : -1] + my_string[e + 1 : ]

    # s = 0 이면 s - 1 = 0 이 되어 방향이 바뀐다.
    # 제대로 방향을 잡도록 수정.
    else:
        # return my_string[e : : -1]
        return my_string[s : e + 1][::-1]

# def solution(my_string, s, e):
#     if (s != 0):
#         answer = my_string[:s:] + my_string[e:s-1:-1] + my_string[e+1::]
#     else:
#         answer = my_string[:s:] + my_string[e::-1] + my_string[e+1::]
#     return answer