class NagativeException(Exception) :
    pass

def scoreCard(score) :
    if score <0 :
        raise NagativeException("invalid :")

try :
    scoreCard(-1)
    
except NagativeException as e :
    print("error message :")