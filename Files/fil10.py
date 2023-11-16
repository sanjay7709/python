# program to read lines, chars, words

fn=input("enter the filename: ")
try:
    with open(fn,'r') as fp:
        fd=fp.readlines()
        print("*"*50)
        print("Content of list")
        print("*"*50)
        for line in fd:
            print(line,end="")
        else:
            print("*"*50)
            nc,nw,nl=0,0,0
            fp.seek(0)
            #fd1=fp.read()
            for l in fd:
                nl=nl+1
                nw=nw+len(l.split())
                nc=nc+len(l)
            else:
                # for c in fd1:
                #     nc=nc+1
                # else:
                #     fp.seek(0)
                #     fd2=fp.readline()
                #     for w in fd2:
                #         nw=nw+1
                #     else:
                        print("no of lines = {}".format(nl))
                        print("no of chars = {}".format(nc))
                        print("no of words = {}".format(nw))
except FileNotFoundError:
    print("File does not exists")