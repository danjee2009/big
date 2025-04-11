import random as rd
t='hi'
print(t[0])
hli=list(map(int,input('1~100사이 공백 기준 입력').split()))
print(hli)



bli=[]
count=0
loli=range(100)

    
    
bli=rd.sample(loli,7)

for i in range(len(hli)):
    if hli[i]==bli[i]:
        count+=1

print(bli,hli)
print(count)
