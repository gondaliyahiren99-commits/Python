"""
all exception derived from the  Exception class 
in pyiuthon there is inbuilt class which nae in Exceptopm
"""
class AgeException(Exception) :
    pass

age = int(input("Enter age"))
if age <18 :
    print("invalid :")
    raise AgeException