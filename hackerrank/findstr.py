def count(string,sub_string):
    # c=0
    # s1=len(sub_string)
    # for i in range(len(string)):
    #     if (string[i:i+s1]==sub_string):
    #         c+=1
    # return c
    c=0
    x=-1
    while(x<len(string)):
        z=string.find(sub_string,x+1)
        if(z==-1):
            break
        c+=1
        x=z 
    print(c)           

count("ABCDCDC","CDC")