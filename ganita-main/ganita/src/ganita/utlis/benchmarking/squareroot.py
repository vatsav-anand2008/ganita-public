import matplotlib.pyplot as plt
from time import time
import sys
import os
sys.set_int_max_str_digits(20000)
import decimal
import random
import math
import csv
import gmpy2

decimal.getcontext().prec=100

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))
from ganita.lilavati.square_root import squareRoot

def squareroot(num):
    try:
        num=str(num)
        if '.' in num or '-' in num:
            num=float(num)
            if num-math.fabs(math.floor(num))==0:
                num=int(num)
                return square_root(num)
            elif num<0:
                raise ValueError("negative number not supported")
            
        
        num=int(num)
        duplicate=num
        length_num=len(str(num))
        root_num_double=""  #to store the final answer in string form
        
        
        if length_num%2==1:
            for i in range (length_num):
                
                '''distinguished in 3 steps 
                    1.to obtain the MSB
                    2.follow the process of subtraction using 2*x*y and the other digits
                    3.follow the process of subtraction using y*y and the other digits'''
                digit=int(duplicate/math.pow(10,length_num-i-1))
                #to obtain MSB and perform suitable operations on it
                
                if(i==0):
                    j=1
                    while (j*j<=digit):
                        j+=1
                    
                    j-=1
                    duplicate=duplicate-(j*j)*math.pow(10,length_num-i-1)
                    root_num_double+=str(j)
                    continue
                
                #follow step 2
                elif(i%2==1):
                    k=1
                    while(2*(int(root_num_double))*k<=digit):
                        if(digit-2*(int(root_num_double))*k>=0):
                            k+=1
                            continue
                    while True:
                        k-=1
                        Even_number=2*(int(root_num_double))*k
                        duplicate1=duplicate-Even_number*math.pow(10,length_num-i-1)
                        digit1=int(duplicate1/math.pow(10,length_num-i-2))
                        break
                        
                    while((k*k)>digit1):
                        k-=1
                        Even_number=2*(int(root_num_double))*k
                        duplicate1=duplicate-Even_number*math.pow(10,length_num-i-1)
                        digit1=int(duplicate1/math.pow(10,length_num-i-2))
                        
                    duplicate=duplicate1
                
                #follow step 3
                else:
                    duplicate=duplicate-(k*k)*math.pow(10,length_num-i-1)
                    root_num_double+=str(k)
                    continue
        
        #algo for the number whose length in even
        else:
            for i in range (length_num-1):
                digit=int(duplicate/math.pow(10,length_num-i-2))
                #print(digit)
                if(i==0):
                    digit1=int(duplicate/math.pow(10,length_num-i-2))
                    j=1
                    while (j*j<=digit1):
                        j+=1
                    
                    j-=1
                    duplicate=duplicate-(j*j)*math.pow(10,length_num-i-2)
                    #print(duplicate)
                    root_num_double+=str(j)
                    continue
                
                
                elif(i%2==1):
                    k=1
                    while(2*(int(root_num_double))*k<=digit):
                        if(digit-2*(int(root_num_double))*k>=0):
                            k+=1
                            continue
                    while True:
                        k-=1
                        Even_number=2*(int(root_num_double))*k
                        duplicate1=duplicate-Even_number*math.pow(10,length_num-i-2)
                        digit1=int(duplicate1/math.pow(10,length_num-i-3))
                        #print(k)
                        break
                        
                    while((k*k)>digit1):
                        k-=1
                        Even_number=2*(int(root_num_double))*k
                        duplicate1=duplicate-Even_number*math.pow(10,length_num-i-2)
                        digit1=int(duplicate1/math.pow(10,length_num-i-3))
                        
                    duplicate=duplicate1
                
                else:
                    #print(k)
                    duplicate=duplicate-(k*k)*math.pow(10,length_num-i-2)
                    root_num_double+=str(k)
                    continue
        
                
        return float(root_num_double)

    except ValueError as e:
        return f"Error: {e}"
    



minDigits=0
maxDigits=1001
step=10

with open('square_root.csv','w',newline='') as rootcsv,open('square_root_fail.csv','w',newline='') as failcsv:
    rootwriter=csv.writer(rootcsv)
    failwriter=csv.writer(failcsv)
    rootwriter.writerow(['Digits','Method','Time'])
    failwriter.writerow(['Digits', 'Method', 'Error'])
    for x in range(minDigits, maxDigits, step):
        try:
            startTime=time()
            result=squareroot(10**x)
            elapsed=time()-startTime
            rootwriter.writerow([x,'Given algorithm',elapsed])
        except Exception as e:
            failwriter.writerow([x,'Given algorithm',str(e)])

    for x in range(minDigits, maxDigits, step):
        try:
            startTime=time()
            result=squareRoot(str(10**x))
            elapsed=time()-startTime
            rootwriter.writerow([x,'My algorithm',elapsed])
        except Exception as e:
            failwriter.writerow([x,'My algorithm',str(e)])

    '''for x in range(minDigits, maxDigits, step):
        try:
            startTime=time()
            result=math.sqrt(10**x)
            elapsed=time()-startTime
            rootwriter.writerow([x,'math.sqrt()',elapsed])
        except Exception as e:
            failwriter.writerow([x,'math.sqrt()',str(e)])'''

print('Benchmark done')

'''xVals=[]
yVals=[]
for x in range(1,5000,2):
    #numDigits=random.randint(0,10000)
    startTime=time()
    squareroot=squareRoot(str(10**x))
    yVals.append(time()-startTime)
    xVals.append(x+1)
    print(x)

plt.xlabel('# of Digits')
plt.ylabel('Time Elapsed(sec)')
plt.plot(xVals,yVals,label='Lilavati')
xVals=[]
yVals=[]

for x in range(1,5000,2):
    #numDigits=random.randint(0,10000)
    startTime=time()
    num1=decimal.Decimal('1e'+str(x))
    squareroot=num1.sqrt()
    yVals.append(time()-startTime)
    xVals.append(x+1)
    print(x)

plt.plot(xVals,yVals,label='Decimal module')
plt.show()'''