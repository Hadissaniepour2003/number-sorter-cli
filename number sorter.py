ones=[]
twos=[]
threes=[]
totalsum=0
while True:
    num1=int(input("enter a number:"))
    if num1==1:
        ones.append(num1)
    elif num1==2:
        twos.append(num1) 
    elif num1==3:
        threes.append(num1)  
    elif num1==-1:
        break   
    totalsum+=num1   
expression="+".join(map(str,yekha+doha+seha))
jam=ones+twos+threes
print(expression,"=",totalsum)
print(jam)  
      