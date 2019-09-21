import random
a=random.randint(0,9)
b=0
print(a)
while a!=b:

    b=input()
    
    if a>int(b):
        print("small")
    elif a<int(b) :
        print("big")
    else :
        print("bingo")
    
