import numpy as np


#reshape the array
a=np.array([
  [1,2,3,4,5],
  [6,7,8,9,0],
  [11,12,13,14,15],
  [16,17,18,19,20]])

print(a)
# print(a.shape)
# print(a.reshape((5,4)))
# print(a.reshape((2,10)))
# print(a.reshape((5,2,2)))
# print(a.flatten())

# var1=a.flatten()
# var1=a.ravel()
# var1[2]=100
# print(var1)
# print(a)


# var = [v for v in a.flat]
# print(var)

#transpose

# print(a.transpose())
# print(a.T)

#swap axis

print(a.swapaxes(0,1))
