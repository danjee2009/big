

a,b=map(int, input().split())

board=[]

for i in range (a):
  board.append([])
  for j in range(b):
    board[i].append(0)


num=int(input())

length=[]
w=[]
x=[]
y=[]

for i in range(num):
  le,vh,wx,wy=map(int,input().split())
  length.append(le)
  w.append(vh)
  x.append(wx)
  y.append(wy)
  
print(length, w, x,y)


for j in range(num):
  for i in range(0,length[i]+1):
    board[y[i]][x[i]]=1
    if w[i]==0:
      x[i]+=1
    elif w==1:
      y[i]-=1


for i in range(a):
  for j in range(b):
    print(board[i][j], end=' ')
  print()

