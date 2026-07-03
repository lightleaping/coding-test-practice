# 문제 설명
# 영어 알파벳으로 이루어진 문자열 str이 주어집니다. 각 알파벳을 대문자는 소문자로 소문자는 대문자로 변환해서 출력하는 코드를 작성해 보세요.

# 제한사항
# 1 ≤ str의 길이 ≤ 20
# str은 알파벳으로 이루어진 문자열입니다.

str = input()

result = ""

for i in str:
    if i.upper() == i:
        result += i.lower()
    else:
        result += i.upper()
    
print(result)

# str = input()
# str = str.swapcase()
# print(str)

# for i in len(str)가 아니라
# for i in range(len(str)) 또는 for i in str를 사용해야 한다.
# TypeError: 'int' object is not iterable

# 문자열 메서드 호출 시 괄호 사용