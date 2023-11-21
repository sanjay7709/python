# by using polymorphism displaying multiple objects using static method

class india:
    def country(self):
        print("india is developing country")
    def lang(self):
        print("indians can speak multple lang ")

class usa:
    def country(self):
        print("usa is developed country")
    def lang(self):
        print("usa people can speak english lang ")

class showinfo:
    @staticmethod
    def disp(obj):
        obj.country()
        obj.lang()
        

ind=india()
us=usa()
showinfo.disp(ind)
showinfo.disp(us)