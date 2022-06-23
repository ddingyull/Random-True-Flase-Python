#랜덤숫자로 수학문제 만들기 
import random

a=random.randint(1,40)
b=random.randint(1,40)

print(a,'+',b,'=')
x=input()
c=int(x)

if a+b==c:
    print('*n_n*')
else:
    print('*ㅜㅜ*')
#스스로문제 for구문을 이용해서 랜덤 수학문제가 3번 반복
import random


for x in range(3):
    a=random.randint(1,30)
    b=random.randint(1,30)
    if x==0:
        print(a,'+',b,'=')
        y=input()
        c=int(y)
    
    if x==1:
        print(a,'+',b,'=')
        y=input()
        c=int(y)
    
    else:
        print(a,'+',b,'=')
        y=input()
        c=int(y)
