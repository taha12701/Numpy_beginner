import numpy as np

# a1=([
#   [1,2,3],
#   [4,5,6]
# ])

# a2=([
#   [5,6,7],
#   [8,9,10]
# ])

# a=np.stack([a1,a2],axis=0)
# print(a)
# print(a.ndim)
# a=np.concatenate((a1,a2),axis=0)
# a=np.concatenate((a1,a2,a3),axis=1)


a=np.array([
  [1,2,3,4,5,6],
  [3,4,5,8,0,0],
  [5,7,9,2,1,1],
  [0,0,0,4,1,0]
])

print(np.split(a,2,axis=1))