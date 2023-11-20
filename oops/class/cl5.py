#static method
class human:
    @staticmethod
    def dispdata(obj):
        print(obj.__dict__)
        print("*"*50)
        for k,v in obj.__dict__.items():
            print("\t{} {}".format(k,v))
        print("*"*50)
e1=human()
e1.sno=14
e1.sname="san"
e1.marks=54
t1=human()
t1.name="des"
t1.age=43
human.dispdata(e1)
human.dispdata(t1)
