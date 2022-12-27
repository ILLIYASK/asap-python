# inheritance

# multiple inheritance

class father:
    f="father"
    def printdet(self):
        print(self.f)
class mother:
    m="mother"
    def printdet(self):
        print(self.m)
class child(father,mother):
    c="child"
    def printdet(self):
        father.printdet(self)
        mother.printdet(self)
        print(self.c)

obj=child()
obj.printdet()


