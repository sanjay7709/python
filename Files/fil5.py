# program to write address of different people in addr.info file

# with open("addr.info", "w") as wp:
#     wp.write("Guido van \n")
#     wp.write("34- indlan\n")
#     wp.write("pysf\n")
#     wp.write("netherlands\n")
# print("address added successfully")

# lst=[10,"nag",43.65,"python"]
# tpl=(20,"san",78.65,"veloo")
# s={"hello",89,"red",908.7}
# d={"hel":40,"tree":90.5}
# with open("addr.info", "a") as wp:
#     wp.writelines(str(lst)+"\n")
#     wp.writelines(str(tpl)+"\n")
#     wp.writelines(str(s)+"\n")
#     wp.writelines(str(d)+"\n")
# print("address added successfully")
import sys
with open("hyd.data","a") as fp:
    print("Enter the lines of text and quit to stop")
    while(True):
        svdata=input()
        if(svdata.lower() == "quit"):
            sys.exit()
        else:
            fp.write(svdata + "\n")
    print("\n Data written successfully")