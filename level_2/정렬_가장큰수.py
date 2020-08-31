
import itertools

# pool = ['A', 'B', 'C']
#  # 3개의 원소로 수열 만들기

# def solution(numbers):

#     ''' 순열과 조합의 개념을 이용 '''

#     number_strs = []
#     for number in numbers:
#         number_strs.append(str(number))

#     answer = list(map(''.join, itertools.permutations(number_strs)))
#     answer.sort()
#     print (answer[-1])
#     return (answer[-1])
    # return (max(answer))


def solution(numbers): 
    numbers = list(map(str, numbers))
    print (numbers)
    for number in numbers:

        print(type(number))

    # for i in range(len(numbers)):
    #     numbers[i]
    # print (numbers)
    # print( lambda numbers: numbers*3)
    # numbers.sort(key=lambda x: x*3, reverse=True)
    # return (str(int(''.join(numbers))))
    # return

numbers = [6, 10, 2]

numbers = [1000, 100, 10, 1]

solution(numbers)


