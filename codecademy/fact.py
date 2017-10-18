def f(x):
    n = 1
    while x>0:
        n = n * x
        x = x - 1
    return n


def factorial( n ):
   if n <1:   
       #print "%2d! = %d" % (n, n)
       return 1
   else:
       temp = factorial( n - 1 )
       #print "%2d! = %d" % (n, n*temp)
       return n * temp  
       
print (factorial(3))
print (f(3))
