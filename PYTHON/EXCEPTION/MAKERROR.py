class eligibleError(Exception) :
    pass

age = int(input("ENter Age :"))
if age >= 18 :
    print("Eligible")
else :
    raise eligibleError("Eligible not.....")

#===============================================================================================================================

class FailEroor(Exception) :
    pass

marks = int(input("Enter Marks :"))
if marks>35 :
    print("pass")
else :
    raise FailEroor("Thda padh Lo")