class indexEroor(Exception) :
    pass
l = [1,2,3]
try : 
    n= int(input("Enter Number :"))
    if l[0]==n :
        raise indexEroor("Error.......! Already 1 store") 
    elif l[1]==n :
        raise indexEroor("Error.......! Already 2 store")
    elif l[0]==n :
        raise indexEroor("Error.......! Already 3 store")

except indexEroor as e:
    print(e)
    
print("ok")