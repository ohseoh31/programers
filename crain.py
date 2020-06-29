'''
    https://programmers.co.kr/learn/courses/30/lessons/64061?language=python3
    크레인 인형뽑기 게임
    2019 카카오 개발자 겨울 인턴십

'''

def solution(board, moves):
    answer = 0
    out_list = []
    lineLen = len(board)   # 행
    rowLen = len(board[0]) # 열
    for move in moves:
        for i in range(0,rowLen) :
            if (board[i][move-1] == 0 ):
                continue
            else :
                out_list.append(board[i][move-1])
                out_list = check_outList(out_list)
                board[i][move-1] = 0
                break
    answer = len(out_list)
    return answer

def check_outList(out_list):
    for i in range(len(out_list)):
        if( i+1 == len(out_list)):
            break
        if(out_list[i] == out_list[i+1]):
            del out_list[i]
            del out_list[i]
            break
            
    return out_list


board = [[0,0,0,0,0],
       [0,0,1,0,3],
       [0,2,5,0,1],
       [4,2,4,4,2],
       [3,5,1,3,1]
    ]

moves = [1,5,3,5,1,2,1,4]


solution(board,moves)
