def solution(d, budget):
    answer = 0
    total=0
    d.sort()
    for i in d :
        total+=i
        if total <= budget :
            answer+=1
        
    return answer