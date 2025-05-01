import matplotlib.pyplot as plt
import time
def cubeRoot(num):
    numlength=len(num)
    root=''
    n=1
    
    if numlength%3==0:
        n=3
    elif numlength==2:
        n=2
    else:
        n=1
    difference=int(num[:n])
    
    for x in range(1,10):
        if difference-x**3>=0 and difference-(x+1)**3<0:
            root+=str(x)
            difference-=x**3
            n+=1
            break
    
    difference=int(str(difference)+num[n-1:n])
    while n<numlength:
        
        '''if n>=numlength:
            break'''
        x=0
        
        while x<10 and int(str(difference)+num[n:n+2])-300*x*int(root)**2-30*int(root)*x**2-x**3>=0:
            x+=1
        if x>0:
            x-=1
        difference-=3*x+int(root)**2
        n+=1

        
        difference=int(str(difference)+num[n-1:n])
        
        root+=str(x)
        difference-=3*int(root)*x**2
        n+=1
        difference=int(str(difference)+num[n-1:n])
        
        #root+=str(x)
        difference-=x**3
        n+=1
        
        difference=int(str(difference)+num[n-1:n])
    return [root,difference]

#number=input('Number: ')
#cbrt=cubeRoot(number)
#print(cbrt[0],cbrt[1])
xVals=[]
yVals=[]
for x in range(100000):
    xVals.append(x)
    startTime=time.time()
    result=cubeRoot(str(x))
    yVals.append(time.time()-startTime)

plt.xlabel('# of Digits')
plt.ylabel('Time Elapsed')
plt.plot(xVals,yVals)
plt.show()