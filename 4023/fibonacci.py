num=int(input("enter the range"))
first=0
second=1
initial=0
for num in range(0,num):
  print(first,end=' ')
  initial=initial+first
  nxt=first+second
  first=second
  second=nxt
print("the fibonacci series")