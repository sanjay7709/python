im=input("enter the image name: ")
try:
    with open(im,"rb") as wp:
        cm=input("enter image 2: ")
        with open(cm,"ab") as ab:
         fd=wp.read()
         ab.write(fd)
except FileNotFoundError:
   print("file does not exists")


n=int(input("enter the value: "))
l=[int(x) for x in range(1,n+1) ]
print(l)