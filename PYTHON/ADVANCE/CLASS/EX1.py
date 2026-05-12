class ExceotErrorsEroor(Exception) :
    pass
class Sample:
    #data member 
    id = 10
    sub = "python"
try :
#object 
    obj =Sample() 
    print(obj.id)
    print(obj.su)

except:
   raise ExceotErrorsEroor("Object part in Error................!")

