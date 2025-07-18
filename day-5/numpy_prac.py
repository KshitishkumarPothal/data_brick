import numpy as np

a = np.array([1,2,3])
b = np.array([[1,2],[3,4]])

c = np.zeros((2,3))  # 2 * 3 of zeros
d = np.ones((3, 4)) # 3*4 of ones
print(d)
e = np.eye(3) # 3*3 of identity matrix
print(e)

f = np.full((2,2),7) # 2*2 matrix full with 7
g = np.arange(0,10,2) #[2,4,6,8,10]
h = np.linspace(0,1,5) # 5 value between 0 to 1
print(h)

#Array attribute
arr = np.array([[1,2],[3,4]])
arr.shape # (2,2)
arr.ndim # 2
arr.size # 2
arr.dtype  # data type int64

#indexing and slicing in arr

arr = np.array([[1,2,3],[4,5,6]])
print(arr[0,1])  #2
print(arr[:,1]) #[2 5]
print(arr[1,:]) #[4 5 6]

#mathematical operation

a = np.array([1,2,3,4])
b = np.array([4,5,6,7])
a + b #[5,7,9,11] element wise
a * b #[4,10,18,28]
print(np.dot(a,b)) # 60 dot priduct
print(np.mean(a))
print(np.mean(b))

np.std(b)  # standard davietion
np.sum(a) #sum
np.max(a) # maximum of array

#reshaping and flattering

arr = np.array([[1,2],[3,4]])
print(arr.reshape(4,1))

#Broadcasting (Allowing arithmatic between array)

a = np.array([[1],[2],[3]])
b = np.array([10,20,30])
print(a+b)