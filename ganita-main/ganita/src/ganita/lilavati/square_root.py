def squareRoot(num):
    numlength=len(num)
    root=''
    n=1
    #to find if the first 1 or 2 digits should be used at the start
    if numlength%2==0:
        n=2
    difference=int(num[:n])
    #subtracting the square from the first digits
    for x in range(1,10):
        if difference-x**2>=0 and difference-(x+1)**2<0:
            root+=str(x)
            difference-=x**2
            n+=1
            break
    #starting main iteration
    difference=int(str(difference)+num[n-1:n])
    while n<numlength:
        #to stop if the number of digits iterated through is at least the length of the original number
        '''if n>=numlength:
            break'''
        x=1
        #first sub-iteration of the loop to check the greatest multiplier that can be used with the existing root to subtract from the current difference
        while difference>=2*int(root)*x and x<10 and int(str(difference)+num[n:n+1])-20*int(root)*x-x**2>=0:
            x+=1
        x-=1
        difference-=2*int(root)*x
        n+=1
        #subtracting the square of the determined multiplier after pulling the next digit
        difference=int(str(difference)+num[n-1:n])
        #print(difference)
        root+=str(x)
        difference-=x**2
        n+=1
        #pulls the next digit for the next set of iterations
        difference=int(str(difference)+num[n-1:n])
    return root