# pickling and Unpickling
# object Serialization or object deserialization

# pickling
# =================
'''
process of dumping entire iterable object data into file of secondary memory using pickling
pickle participates in write operations

steps:
    1) import pickle module
    2) open file in write mode
    3) create an object with collection of values(iterable_object)
    4) Syntax :  pickle.dump(object,filepointer)
    5)NOTE : Pickling always takes files in Binary format
'''
# unpickling
#======================

''''
To read or transfer entire record from file of secondary memory if we use read(), readline() then they read record
line by line and time consuming process hence we need to use the concept of unpickling 
with single read ops we can read entire records of file of secondary memeory into object of main memory

steps:
    1) import pickle module
    2) open file in read mode
    3) use load() of pickle module to read entire record content from file of secondary memeory 
        into object of main memory
    4) Syntax :  pickle.load(object,filepointer)
    5)NOTE : UnPickling always takes files in Binary format

'''