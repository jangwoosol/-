a = int(input())
for i in range(a):
    num, sentence = input().split()
    text=''
    for i in sentence:
      text+=int(num)*i
    print(text)