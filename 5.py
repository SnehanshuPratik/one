import numpy as np

arr=np.array(
    [1,2,4]
)

print(arr,type(arr))
print("shape of array ",arr.shape)

arr2d=np.array([
    [2,3],
    [5,6]
])
print(arr2d,arr2d.shape)

print(
    arr2d[0,0],arr2d[0,1]                       #print object at row 0 column 0 and object at row 0 column 1
)
print(
    arr2d[1,0],arr2d[1,1]
)
print(
    arr2d[1,1],arr2d[0,1]
)
arr3d=np.array([
    [
        [1,2,3],
        [5,6,6],
        [7,3,9]
    ],
    [
        [8,9,6],
        [5,6,3],
        [4,4,5]
    ],
    [
        [8,2,1],
        [0,2,3],
        [5,6,9]
    ]
])
print(arr3d)
print(arr3d[0,0])
print(arr3d[0,0,0])

print(arr2d)
arr2d[0]=[1,4]
print(arr2d)

zeros=np.zeros((4,5))
print(zeros)

ones=np.ones((3,))
print(ones)

ones=np.ones((3,0))
print(ones)

ones=np.ones((3,1))
print(ones)

ones=np.ones((1,3))
print(ones)

ones=np.ones((3,3,3))
print(ones)
consts=np.full((3,3),9)
print(consts)





