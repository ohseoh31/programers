

# 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어 수


# fail_per = no_clear_player / clear_player

# 전체 스테이지의 개수 N

# 게임을 이용하는 사용자가 현재 멈춰있는 스테이지의 번호가 담긴 배열 stages가 매개변수로 주어질 때

# 실패율이 높은 스테이지부터 내림차순으로 스테이지의 번호가 담겨있는 배열을 return 하도록 solution 함수를 완성하라.

# stages에는 1 이상 N + 1 이하의 자연수가 담겨있다. 각 자연수는 사용자가 현재 도전 중인 스테이지의 번호를 나타낸다.

# 단, N + 1 은 마지막 스테이지(N 번째 스테이지) 까지 클리어 한 사용자를 나타낸다.

import functools
from collections import Counter as mset
def solution(N, stages):

    fail_per = []
    answer = []

    stage_dic = {}
    for stage in range(1,N+2):
        stage_dic[stage] = 0

    for stage in stages:
        stage_dic[stage] +=1

    for i in range(N):
        no_clear_player_count = 0
        clear_player_count = 0
        for key in stage_dic.keys():

            # print (key)
            if key == i + 1 :
                no_clear_player_count += stage_dic[key]
            if key >= i + 1:
                clear_player_count += stage_dic[key]
        
       
        if clear_player_count !=0:
            fail_per.append([i+1,no_clear_player_count/clear_player_count])

        elif clear_player_count == 0: 
            fail_per.append([i+1,0.0])


    fail_per = bubble_sort(fail_per)
    for grade in fail_per:
        answer.append(grade[0])
    print (answer)
    return(answer)

def bubble_sort(arr):
    for i in range(len(arr) - 1, 0, -1):
        for j in range(i):
            if arr[j][1] < arr[j + 1][1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return (arr)



# 만약 실패율이 같은 스테이지가 있다면 작은 번호의 스테이지가 먼저 오도록 하면 된다.
# 스테이지에 도달한 유저가 없는 경우 해당 스테이지의 실패율은 0 으로 정의한다.

N = 5 
stages = [2, 1, 2, 6, 2, 4, 3, 3]
N = 4
stages = [4,4,4,4,4]
# result = [3,4,2,1,5]

solution(N, stages)