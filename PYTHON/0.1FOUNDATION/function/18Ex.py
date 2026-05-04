"""
decoraters :
     
     as we know that fumctin is an object 

     function can accept another fun as peremeter and a function 
     can return another functon as a return value

     what is decoraters :

            DECO IS most powerful topic of function
            whiach is accept any fun as a perameter and make it special fun


    when use:

            when we want to add an extera functionality to fun before calling or after calling
            we can use decoraters.
"""

def myDecorater(myfun): #a accepting fun as a perameter
    def wrapper():#bina wrape function ke bar bar call karne pr repeat nahi hoga
        print("Alar...... 5")
        print("Alar...... 6")
        myfun() #calling actual function
        print("office ")
    return wrapper

@myDecorater
def saygelllo():
    print("good norning :")

saygelllo()
saygelllo()


#=================================
def myDecorater(myfun):
    print("befire fun")
    myfun()
    print("after fun")
    return myfun

@myDecorater
def sayHello():
    print("hello")


sayHello
sayHello
