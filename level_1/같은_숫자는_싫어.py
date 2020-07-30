
def solution(arr):
    answers = []
    if (len(arr) <= 1000000):
        for num in arr :
            answers.append(num)
            
            if (len(answers) < 2):
                    continue
            #print (answers[len(answers)-1])
            #print (answers[len(answers)-2])
            if (answers[len(answers)-1] == answers[len(answers)-2]):
                del answers[len(answers)-1]
    print (answers)
    return answers

arr = [1,1,3,3,0,1,1]
solution(arr)
