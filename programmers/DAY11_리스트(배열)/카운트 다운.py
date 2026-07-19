# 문제 설명
# 정수 start_num와 end_num가 주어질 때,
# start_num에서 end_num까지 1씩 감소하는 수들을
# 차례로 담은 리스트를 return하도록 solution 함수를 완성해주세요.

# 제한사항
# 0 ≤ end_num ≤ start_num ≤ 50

def solution(start_num: int, end_num: int):
    
    lst = list()
    for i in range(end_num - start_num):
        lst.append(end_num - i)
    
    return lst

# def solution(start_num, end_num):
#     answer = []
#     ns = start_num
#     num = 0
#     while(num < start_num - end_num + 1):
#         answer.append(ns)
#         ns -= 1
#         num += 1
#     return answer
    
# while if 수 계산 방법