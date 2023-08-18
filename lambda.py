x=lambda a: a+5
print(x(5))

grt=lambda x,y:x if(x>y) else y
print(grt(2,5))

lst=[22,41,3]
a=list(map(lambda x: x+5,lst))
print(a)

lst=[1,2,3]
sqr=list(map(lambda y: y*y,lst))
print(sqr)

fib=[0,1,1,2,3,5,13,21,34]
f=list(filter(lambda x:x%2,fib))
print(f)

from functools import reduce
lst=[1,2,3,4,5,6,7]
x=reduce(lambda x,y:x+y,lst)
print(x)

from functools import reduce
lst=[1,2,3,9,5,6,7]
x=reduce(lambda x,y:x if(x>y) else y,lst)
print(x)




