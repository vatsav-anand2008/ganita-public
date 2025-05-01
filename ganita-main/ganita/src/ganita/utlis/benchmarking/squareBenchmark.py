import matplotlib.pyplot as plt
from time import time

#fig=plt.subplot()
plt.xlabel('Number of digits')
plt.ylabel('Time to Run')

def lilavatiSquare(num):
  arr=[]
  digit=''
  for x in num:
    arr.append([])
  for x in num:
    if int(x)**2<10:
      arr[0].append('0')
      arr[0].append(str(int(x)**2))
    else:
      arr[0].append(str(int(x)**2)[0])
      arr[0].append(str(int(x)**2)[1])
  for i,x in enumerate(arr):
    if i!=0:
      for j in range(len(arr)-i):
        if 2*int(num[j])*int(num[j+i])>=100 and len(digit)>0:
          enddigit=int(digit[-1:])
          enddigit+=1
          digit=digit[:len(digit)-1]
          digit+=str(enddigit)
          if 2*int(num[j])*int(num[j+i])<110:
            digit+='0'+str(2*int(num[j])*int(num[j+i])-100)
          else:
            digit+=str(2*int(num[j])*int(num[j+i])-100)
        elif 2*int(num[j])*int(num[j+i])<10:
          digit+='0'+str(2*int(num[j])*int(num[j+i]))
        else:
          digit+=str(2*int(num[j])*int(num[j+i]))
      k=0
      zerocount=0
      frontzeroes=0
      for j in digit:
        if j=='0':
          zerocount+=1
        else:
          break
      '''while digit[-1]=='0':
        digit=digit[:-1]'''
      while len((digit))<2*len(num):
        if k==0:
          digit+='0'
          k=1
        elif k==1:
          if frontzeroes+zerocount<=i:
            frontzeroes+=1
            digit='0'+digit
          k=0
      for k in digit:
        x.append(k)
      digit=''
  sum=''
  for x in reversed(range(0,2*len(num))):
    digitsum=0
    for i in range(len(arr)):
      digitsum+=int(arr[i][x])
    while digitsum>9:
      carryover=str(int(arr[0][x-1])+1)
      arr[0][x-1]=carryover
      digitsum-=10
    sum=str(digitsum)+sum
  if sum[0]=='0':
    sum=sum[1:]

def karatsuba_square(n):
    if n < 10:
        return n * n
    
    m = len(str(n))
    m2 = m // 2
    
    high, low = divmod(n, 10**m2)
    
    z0 = karatsuba_square(low)
    z2 = karatsuba_square(high)
    z1 = karatsuba_square(high + low) - z2 - z0
    
    return (z2 * 10**(2*m2)) + (z1 * 10**m2) + z0


xVals=[]
yVals=[]
for x in range(200,4000,100):
    startTime=time()
    square=lilavatiSquare(str(10**x))
    yVals.append(time()-startTime)
    xVals.append(x+1)
    print(x)

plt.plot(xVals,yVals,label='Lilavati')
xVals=[]
yVals=[]

for x in range(200,4000,100):
    startTime=time()
    square=karatsuba_square((10**x))
    yVals.append(time()-startTime)
    xVals.append(x+1)
    print(x)

plt.plot(xVals,yVals,label='Karatsuba')
xVals=[]
yVals=[]

for x in range(200,4000,100):
    startTime=time()
    square=(10**x)**2
    yVals.append(time()-startTime)
    xVals.append(x+1)
    print(x)

plt.plot(xVals,yVals,label='Exponentiation')
xVals=[]
yVals=[]

plt.legend()
plt.show()