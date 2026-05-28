"""
multiple inheritance  :

tgere are 2 parent and 1 child its called multiple inherotance 


                        A                    b
                        |                    |
                        |____________________|
                                |
                                |
                                C
"""


class A : 
        def displayA(self) :
                print("A")


class B :
        def displayB(self):
                print("B")

class C(A,B) :
        def displayC(self):
                print("C")
        
obj =C()
obj.displayA()
obj.displayB()
obj.displayC()