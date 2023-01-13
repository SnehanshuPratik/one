import numpy as np

arr=np.array([
    [3,6,3,8],
    [8,1,0,2],
    [8,7,0,1]
])
print(arr[:2])
print(arr[:2,1:3])
print(arr[2:3,:2])

print (arr)
bool_idx=[arr>3]
print(bool_idx)

x=np.array([
    [6,7],
    [3,5]
])
y=np.array([
    [8,3],
    [8,1]
])
print(x,y)
print(x+y)
print(np.add(x,y))
print(np.multiply(x,y))
print(np.divide(x,y))
print(np.subtract(x,y))
print(np.sqrt(x))
v=np.array([4,3])
w=np.array([5,6])

print(v.dot(w))
print(np.dot(v,w))

print(x)
print(x.T)
u=np.array([
    [5,6,2],
    [3,2,1],
    [7,9,4]
])
print(u)
print(u.T)
print("sum of all elements of u: ",np.sum(u))
print("sum of each column: ",np.sum(u,axis=0))
print("sum of each rows: ",np.sum(u,axis=1))
