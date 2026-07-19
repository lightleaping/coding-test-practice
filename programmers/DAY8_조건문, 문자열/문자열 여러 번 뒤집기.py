# 문제 설명
# 문자열 my_string과 이차원 정수 배열 queries가 매개변수로 주어집니다.
# queries의 원소는 [s, e] 형태로,
# my_string의 인덱스 s부터 인덱스 e까지를 뒤집으라는 의미입니다.
# my_string에 queries의 명령을 순서대로 처리한 후의 문자열을 return 하는
# solution 함수를 작성해 주세요.

# 제한사항
# my_string은 영소문자로만 이루어져 있습니다.
# 1 ≤ my_string의 길이 ≤ 1,000
# queries의 원소는 [s, e]의 형태로 0 ≤ s ≤ e < my_string의 길이를 만족합니다.
# 1 ≤ queries의 길이 ≤ 1,000

def solution(my_string: str, queries: list[list[int]]):
    list_my_string = list(my_string)

    # queries의 각 원소는 [s, e] 형태이므로 바로 언패킹할 수 있다.
    # 아래와 같이 작성해도 동일하다.
    # for query in queries:
    #   s, e = query
    for s, e in queries:

        # 구간을 뒤집으려면 역순 슬라이싱을 사용한다.
        # list_my_string[s : e + 1][::-1]

        # 혹은 list_my_string[e : s - 1 : -1]
        # 그러나 이때 s = 0 인 경우 e = 7, s - 1 = -1로 포함되지 않는 종료 경계가 동일하여
        # 빈 문자열이 반환된다.
        list_my_string[s : e + 1] = list_my_string[s : e + 1][::-1]

    return ''.join(list_my_string)

# for s, e in query: 라고 하면 각각 (s, e)로 언패킹하려고 해서 오류 발생
# 문자열은 불변 객체이기 때문에 문자열의 일부를 바꿀 수 없다.

# 뮨저욜울 수정해야 하는 문제에서는 list()로 변환한 후 작업하고
# 마지막에 ''.join()으로 다시 문자열을 만드는 방법이 가장 간단하다.

# def solution(my_string, queries):
    
#     for i in queries:
#         s = i[0]
#         e = i[1]
#         my_string = my_string[0:s] + my_string[s:e+1][::-1] + my_string[e+1:]
        
#     return my_string