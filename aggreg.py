import numpy as np


a=np.array([
  [1,2,3,4,5,6],
  [3,4,5,8,0,0],
  [5,7,9,2,1,1],
  [0,0,0,4,1,0]
])

# print(a.min())
# print(a.max())
# print(a.mean())
# print(a.std())
# print(np.median(a))

# number=np.random.randint(0,100, size=(2,3,4))

# numbers = np.random.binomial(10, p=0.5, size=(5,10))
# print(numbers)

numbers = np.random.normal(loc=170, scale=15, size=(5,10))
print(numbers)