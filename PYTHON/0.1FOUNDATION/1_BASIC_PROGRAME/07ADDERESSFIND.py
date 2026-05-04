"""

id() : return address of specific variable

"""

name = "python"
print(id(name[0]))

"""
    agar ek bar ek string ya koi char store he to usko 
    python ne bar bar dusri memory nahi milegi
    wo usi ka refrence use karega
"""
if id("p")==id(name[0]):
    print("true")
else:
    print("false")

    # true

name1="param"
if id("p")==id(name[0]):
    print("true")
else:
    print("false")

    # true
