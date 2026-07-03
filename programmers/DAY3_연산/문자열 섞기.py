# 문제 설명
# 길이가 같은 두 문자열 str1과 str2가 주어집니다.

# 두 문자열의 각 문자가 앞에서부터 서로 번갈아가면서
# 한 번씩 등장하는 문자열을 만들어 return 하는 solution 함수를 완성해 주세요.

# 제한사항
# 1 ≤ str1의 길이 = str2의 길이 ≤ 10
# str1과 str2는 알파벳 소문자로 이루어진 문자열입니다.

def solution(str1: str, str2: str) -> str:
    result = []
    for i in range(len(str1)):
        result.append(str1[i])
        result.append(str2[i])
    return "".join(result)

# def solution(str1, str2):  
#     answer = str1[0]+str2[0]
#     if len(str1) != 1:    
#         n = 1
#         while True:
#             answer += str1[n] + str2[n]
#             n = n + 1
#             if n == len(str1):
#                 break
#     return answer