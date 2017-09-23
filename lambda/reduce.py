from functools import reduce
#calculate sum  from 1 to 5
print(reduce((lambda x,y: x+y),range(1,6)))
#15