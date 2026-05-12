"""
.

using of encapsulation we can prevent data from outside the world.
in a simle language we can sau that encapsulation provide data hiding data security 



**************there  are mainely 3 visiblility modes*******************


        1) private :
                private : privarte is a visibility mode in python using __(double undrscore) in prefix
                we can make that member is private
        2) public :
                by default all class member are public we can acess anywhere from outside the claass

        3) protected :
                in python  protected  which is indicate by  _(single underscore)
                but in python its not working strickly .

        
"""

class Sample :
    def __init__(self) :
        self.name = "Anjali"
        self.__subject = "Python"

obj = Sample()

print(obj.name)
print(obj.__subject)