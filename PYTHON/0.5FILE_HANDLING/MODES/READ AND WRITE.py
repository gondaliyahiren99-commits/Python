with open("helo.txt" , 'r+') as f :
    f.write("My name is Hiren")
    f.seek(0)
    data =f.read()
    print(data)