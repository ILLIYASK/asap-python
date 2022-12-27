# inheritance



# hierarchical inheritance
#
class perant:
    f="father"
    m="mother"
    def parent_details(self):
        print(self.f)
        print(self.m)
class child1(perant):
    c1="abc"
    def printdet(self):
        print(self.c1)
class child2(perant):
    c2="def"
    def prinndet(self):
        print(self.c2)
obj1=child1()
obj2=child2()
obj1.parent_details()
obj1.printdet()
obj2.parent_details()
obj2.prinndet()
