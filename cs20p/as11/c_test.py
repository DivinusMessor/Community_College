import numpy

n = numpy.array([1,2,3,4])
eval("numpy."+n.__repr__()) # what does this give us?
print(n.__repr__()) # we get array([1, 2, 3, 4])
print(n) # something strange we get "[1 2 3 4]"
nn = eval("numpy."+n.__repr__()) # what does this give us? 


#Outpur
'''
array([1, 2, 3, 4])
[1 2 3 4]
'''