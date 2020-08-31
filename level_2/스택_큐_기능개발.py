
def solution(progresses, speeds):
    answer = []
    count = 0
    flag = 0
    
    while(True):
        
        if (flag == 1):
            break

        if (len(progresses)!=0 and progresses[0] >= 100):
            count = count + 1

            progresses.pop(0)
            speeds.pop(0)

        else:

            if count  >= 1 :
                answer.append(count)
                if (len(progresses) == 0):
                    flag = 1
                count = 0

            for i in range(len(progresses)):
                progresses[i] += speeds[i]

    return answer

progresses  = [93,30,55]
speeds = [1,30,5]



#[2,1]

solution(progresses, speeds)