# copy content of one file to another file
try:
    fn1=input("enter the source file: ")
    with open(fn1,'r') as rp:
        ds1=input("enter the destination file: ")
        with open(ds1,'a') as wp:
            filedata=rp.read()
            wp.write(filedata + "\n")
            print(" src file {} is copied to {}".format(fn1,ds1))
            # print("content of source file: {}".format(filedata))
            # print("content of dest file: {}".format(ds1))
except FileNotFoundError:
    print("File {} does not exists".format(fn1))

