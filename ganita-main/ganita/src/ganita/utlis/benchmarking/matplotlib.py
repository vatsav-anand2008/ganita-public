import matplotlib.pyplot as plt
import numpy as np

xvals=[]
yvals=[]
plotlowbound=float(input("Enter lower bound of graph domain: "))
plotupperbound=float(input("Enter upper bound of graph domain: "))
x=plotlowbound
while x<=plotupperbound:
    xvals.append(x)
    x+=(plotupperbound-plotlowbound)/100
for x in xvals:
    yvals.append(x**2)
fig=plt.subplot()
fig.plot(xvals,yvals)
plt.show()