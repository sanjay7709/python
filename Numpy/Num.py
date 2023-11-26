'''
    Numpy
    =========

It is used perform complex mathematical operations

module: numpy
>>> pip install numpy

ndarray
=======
>. in numpy the data is always stored in the form of objects whose value is ndarray
>> ndarray is a class to hold the array of values in the form of object 
>> an obj of nd array always takes leeser memory space when compared to lists

>> on the object of ndarray we can perform vector operations where as in list it is not possible

Storing the object in numpy
============================
>> to store we must create an obj of ndarray
>> creating an obj of ndarray we have 7- approaches
    --> 1. array()
            varname=numpy.array(object,dtype)
    --> 2. arange()
            varname=numpy.arange(start,stop,step)
    --->3. reshape() 
    >>> to convert 2d and 3d dimensional we use reshape
            varname=obj.reshape()
     --> 4.linspace()
    ---> 5. Zeros()
    >>> This Function is used for building ZERO matrix either with 1-Dim 2-Dim- nDim
    -->6. ones()
    -->7.full()
    --> eye()
    -->identity()
Eaxmple:
a=np.zeros(12)
>>> a
array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.])
>>> a.shape
(12,)
>>> a.reshape(3,4)
array([[0., 0., 0., 0.],
       [0., 0., 0., 0.],
       [0., 0., 0., 0.]])
>>> a.reshape(2,3,2)
array([[[0., 0.],
        [0., 0.],
        [0., 0.]],

       [[0., 0.],
        [0., 0.],
        [0., 0.]]])
>>> a.reshape(3,2,2)
array([[[0., 0.],
        [0., 0.]],

       [[0., 0.],
        [0., 0.]],

       [[0., 0.],
        [0., 0.]]])
>>> a.reshape(4,3)
array([[0., 0., 0.],
       [0., 0., 0.],
       [0., 0., 0.],
       [0., 0., 0.]])
>>> a.reshape(2,6)
array([[0., 0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0., 0.]])
>>> a.reshape(6,2)
array([[0., 0.],
       [0., 0.],
       [0., 0.],
       [0., 0.],
       [0., 0.],
       [0., 0.]])
>>>

'''

l=[[1,0,0],[0,1,0],[0,0,1]]
for x in l:
    print(x)

# x=1
# y=1
# z=1
# n=2
# l=[[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if(i+j+k)==n]
# print(l)

