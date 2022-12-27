# inheritance



# multi level inheritance
#
class grandparent:
    gf="grandfather"
    gm="grandmother"

    def printdel(self):
        print(self.gf,self.gm)
class parent(grandparent):
    f="father"
    m="mother"

    def printdel(self):
        print(self.f,self.m)
class child(parent):
    c="child"
    def printdel(self):
        grandparent.printdel(self)
        parent.printdel(self)
        print(self.c)


obj=child()

obj.printdel()
