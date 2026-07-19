# 간단한 논리 연산
# 제출 내역
# 문제 설명
# boolean 변수 x1, x2, x3, x4가 매개변수로 주어질 때, 다음의 식의 true/false를 return 하는 solution 함수를 작성해 주세요.

# (x1 ∨ x2) ∧ (x3 ∨ x4)

# ∨과 ∧의 진리표는 다음과 같습니다.
# x	    y	x ∨ y	x ∧ y
# T	    T	T	    T
# T	    F	T	    F
# F	    T	T	    F
#       F	F	    F

def solution(x1: bool, x2: bool, x3: bool, x4: bool):
    if x1 or x2:
        first = True
    else:
        first = False
    
    if x3 or x4:
        second = True
    else:
        second = False

    if first and second == True:
        result = True
    else:
        result = False
    
    return result

# def solution(x1: bool, x2: bool, x3: bool, x4: bool):
#     if x1 or x2:
#         first = True
#     else:
#         first = False
    
#     if x3 or x4:
#         second = True
#     else:
#         second = False

#     if first and second == True:
#         result = True
#     else:
#         result = False
    
#     return result