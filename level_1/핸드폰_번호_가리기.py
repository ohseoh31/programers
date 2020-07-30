
#s는 길이 4 이상, 20이하인 문자열입니다.
def solution(phone_number):
    
    answer = ''
    if (len(phone_number) >= 4 and len(phone_number) <=20):    
        for i in range(len(phone_number)-4):
            answer = answer +'*' 
        answer = answer + phone_number[-4:]
    return answer

phone_num = "01033334444"

solution(phone_num)

