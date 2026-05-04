def dec(fun):
    #def wapper()
    print("befor")
    fun()
    print("after")
@dec
def myfun():
    print('hello')
myfun()#agar hum wapper function ka use nhi karenge to hum jab yha myfun mai () lgaye ge to erorr aye gi qki humne 
# koi bhi function ka addres return nhi kiya hai jese wapper or fun agar hum fun ka adres pas karenge to hello do 
# bar ayega bichme bhi or niche bhi