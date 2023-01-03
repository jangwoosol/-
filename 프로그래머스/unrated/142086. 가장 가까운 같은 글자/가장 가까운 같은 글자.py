def solution(s):
    answer = []
    word={}
    for i,j in enumerate(list(s)):
        if j not in word:
            answer.append(-1)
            word[j]=i
        else:
            answer.append(i-word[j])
            word[j]=i        
    return answer