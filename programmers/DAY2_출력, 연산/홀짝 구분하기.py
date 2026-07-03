# 문제 설명
# 자연수 n이 입력으로 주어졌을 때 만약 n이 짝수이면 "n is even"을,
# 홀수이면 "n is odd"를 출력하는 코드를 작성해 보세요.

# 제한사항
# 1 ≤ n ≤ 1,000

n = int(input())

if n % 2 == 0:
    print(n, "is even")
else:
    print(n, "is odd")

# TypeError: unsupported operand type(s) for //: 'str' and 'int'
#
# input()으로 입력을 받으면 문자열이다.
# // 몫 계산, % 나머지 계싼