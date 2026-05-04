def myfun():
    print('hello good mornig')
def decoraotor(fun):
    def wapper():
        print("5:00")
        print("6:00")
        fun()
        print("get reddy!!")
    return wapper #yha function run nhi ho rha yha wapper function ka address return huva jo name mai save huva 
name=decoraotor(myfun)
name()
name()