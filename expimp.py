import numpy as np

a=np.array([
  [1,2,3,4]
])

# a=np.load("myarray.npy")
# print(a)
# np.save("myarray.npy",a)

np.savetxt("myarray.csv",a,delimiter=',')
a=np.load("myarray.npy")
print(a)
