a=input().upper() #대소문자관계없이 개수 비교해야하니까 모든 단어 대문자로 변경
b=list(set(a))

word=[]
for i in b:
  total=a.count(i)
  word.append(total)
if word.count(max(word))>1:
  print('?')
else :
  print(b[word.index(max(word))])