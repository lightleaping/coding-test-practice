# 문제 설명
# 알파벳으로 이루어진 문자열 myString과 pat이 주어집니다.
# myString의 연속된 부분 문자열 중
# pat이 존재하면 1을 그렇지 않으면 0을
# return 하는 solution 함수를 완성해 주세요.

# 단, 알파벳 대문자와 소문자는 구분하지 않습니다.

# 제한사항
# 1 ≤ myString의 길이 ≤ 100,000
# 1 ≤ pat의 길이 ≤ 300
# myString과 pat은 모두 알파벳으로 이루어진 문자열입니다.

def solution(myString: str, pat: str):
    if pat.lower() in myString.lower():
        return 1
    else:
        return 0
    
# def solution(myString, pat):
#     answer = 0
#     pat = pat.upper()
#     myString = myString.upper()
#     if pat in myString:
#         answer = 1
#     return answer

# 대소문자를 구분하지 않으므로 대문자, 혹은 소문자로 통일시켜 확인해야 한다.
# 문자열을 함수로 변환시킨 후에는 결과를 변수에 다시 저장해야 한다.