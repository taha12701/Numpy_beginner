import numpy as np

# d={'1':'A'}
# a=np.array([
#   [1,2,3],
#   [4,d,6],
#   [7,8,9], 
# ])
# dtype=np.float32)

# print(a.dtype)
# print(type(a[1][0]))
# print(a[1][1])

# a=np.array([[1,2,3],
#            [4,5,6],
#            [7,8,9]], dtype="<U8")

# print(a.dtype)
# print(a[1][2])



d={'name': 'Taha', 'age':24}

c=np.array([
  [1,2,1],
  [3,4,d],
  [2,5,0]
], dtype="<U4")

print(c.dtype)
print(c.shape)
print(c.ndim)
print(c[1][0])

