a=[1,1,1,1]
b=[1,2,3,4]
c=[1,1,1,1]
l=list(map(lambda x,y,z:x+y+z,a,b,c))
print(l)
print( )

fruit=["mango","apple","orange","kiwi"]
f=list(filter(lambda x:'g' in x,fruit))
print(f)
print( )

fruit=["mango","apple","orange","kiwi"]
f=list(filter(lambda x:'g' not in x,fruit))
print(f)
