# 문제 설명
# 영어 알파벳으로 이루어진 문자열 str이 주어집니다. 각 알파벳을 대문자는 소문자로 소문자는 대문자로 변환해서 출력하는 코드를 작성해 보세요.

# 제한사항
# 1 ≤ str의 길이 ≤ 20
# str은 알파벳으로 이루어진 문자열입니다.

s = input()

result = ""

for i in s:
    if i.upper() == i:
        result += i.lower()
    else:
        result += i.upper()
    
print(result)

# s = input()
# s = str.swapcase()
# print(s)

# for i in len(s)가 아니라
# for i in range(len(s)) 또는 for i in s를 사용해야 한다.
# TypeError: 'int' object is not iterable

# 문자열 메서드 호출 시 괄호 사용