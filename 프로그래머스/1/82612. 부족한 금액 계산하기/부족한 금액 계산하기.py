def solution(price, money, count):
    cost = 0
    answer=0
    for i in range(1,count+1) :
        cost += price*i
        
    if money > cost :
        answer = 0
    else :
        answer = cost-money
    return answer