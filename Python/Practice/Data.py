import numpy as np
import random

data = '# The is a fictitious data made by whom at 2018/12/xx\n# The each column, resp., represents x, 2x+3+error term, x^2-x+1+error term.'

x=np.arange(0.0,3.0,0.1)
y=list(2*e+3+random.uniform(-0.5,0.5) for e in x)
z=list(e**2-e+1+random.uniform(-1,1) for e in x)
for a,b,c in zip(x,y,z):
  data += '\n' + str(a) + ', ' + str(b) + ', ' + str(c)

myfile=open('sample.csv','w')
myfile.write(data + '\n')
myfile.flush()
myfile.close() 