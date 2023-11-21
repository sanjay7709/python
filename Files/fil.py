# Non persistent applications
''' We accept the data from keyboard ---> main memory, process and display it on monitor'''
# persistent applications
'''we accept the data from keyboard ,  files/database ---> main memory , process and display it on monitor 
and store the data in files/database'''
'''
file -- collection of records , resides in secondary memory
All objects data of main memory becomes file of secondary memory

NOTE: 
To view the files data we use >>  type <file-name>


Stream--> Flow of data b/w main memory and the file of secondary memory is called stream
Types of Files
a) Text Files --> digits, symbols, alphabets, only
            ---> Denoted by letter 't'
            --> default a file is taken as .txt
            --> ex - .doc,.py,.cpp,.xls,.txt...etc
b) Binary files
    --> binary format (0's and 1's)
    --> machine readable , denoted by 'b'
    ---> ex -- images(.jpg, .png)
            -- videos (.mp4)
            -- audio (.mp3)
            --pdf (text +images)

Files purpose -- To achieve Data persistency
'''
# operations on files
# ==========================
'''
1) Write Operation
    To transfer temp data from main memory into file of secondary memory
    steps
    ---------
        1. choose the file name
        2. open file name in write mode
        3. perform cycle of write ops 
    While we are performing write ops we get some exceptions they are:
        a) FileExistsError
        b) IOError
2) Read operation
    To read data from  file of secondary memory into main memory
    steps 
    ---------
        1. choose the file name
        2. open file name in read mode
        3. perform cycle of read ops 
    While we are performing read ops we get some exceptions they are:
        a) FileNotFoundError
        b) EOFError
'''

# File operation modes
# ==============================
''''
We have 7 file openining modes 
1. r --> read
  >>  This mode is used for opening file in read mode
  >> default file opening mode
2. w
  >>  This mode is used for opening file always in write mode newly
  >> if file exists already then data gets overwritten
3. a
    >> This mode is used for opening file in append mode 
    >> here new data will be written to the file from beginning
    >> if open existing file , new data added at the end 
4. r+
  >>  This mode is used for opening file in read mode
  >> r+ --> read and write ops both 
5. w+
  >>  This mode is used for opening file always in write mode newly
  >> w+ here file is opened in write mode and we can read also
  >> w+ --> write and read ops both 
6. a+
  >>  This mode is used for opening file in append mode newly
  >> a+ here file is opened in append/write mode and we can read also
  >> a+ --> append and read ops both

7. x
  >> This mode is used for opening any new file in write mode exclusively
  >> if file already exists and if we open in X- mode it throws exception : FileExistsError

'''

# Number of approaches to open the files
# =============================================
'''
1) by using open()
    syntax: varname=open("Filename","Filemode")
    varname --is an object of class <class,'_TextIOWrapper'>,it acts as a file pointer
    with this approach we need to manual close the file using close()

2) by using with open() as ""
        >> auto closability property
'''

# writing to the files
'''
1) write()
    -- writing any tpe of data to file in form of str
    synt: filepointer.write(str,data)
2) writelines()
    synt: filepinter.writelines(iterable_obj)
    iterable obj must be of str type only
'''

# reading the files
'''
1) read()
    --  var = filepointer.read()
2) read(no of chars)
    >> reading specified no of chars from given file
    -- var= filepointer.read(no of chars)
3) readline():
    >> redaing one line at a time
    -- var = filepointer.readline()
'''














