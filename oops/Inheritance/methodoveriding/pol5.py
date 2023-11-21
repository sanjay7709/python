# by using polymorphism displaying multiple objects
# object level polymorphism
#==============================

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

ind=india()
us=usa()
for obj in (ind,us):
    obj.country()
    obj.lang()
    