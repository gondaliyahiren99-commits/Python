"""
Regular Expression :
 regx are sequences of characters that from serch patterns. They are primerily used for string matching and manipulation. In python ,
 the re modual provides support for working with regular expressiions, whicch can help serchh, match, replae , split based on patterb
"""


# pyrefly: ignore [missing-import]
import re
# st = "my con is 98754545 and my subject is pyton"
# result = re.search(r"\d+",st)
# print(result)
# print(result.group())


# data = "ram age is 25 hiren age is 23 and karan  age is 15"
# print(data)
# result =re.findall(r"\d +",data)   #lisr
# print(result)


# data = "My subject is python"
# result = re.sub(r"python","flutter",data)
# print(result)

"""
\d ": for digit value
\D  for nondigit value
"""

# data = "python is programin language"
# result = re.findall(r"\D",data)  # har ek character ke liye match karega or  har ek list ka element banega
# print(result)
# print("".join(result))


# data = "My programin is @1 #23"
# result = re.findall(r"\w",data) # symbol ignore kare chhe
# print(result)
# print("".join(result))


# data = "My programin is language"
# result= data.find("progr") # index ki start position dikhayega
# print(result)



# email = "hiren@h.dd"
# re = re.findall(r"\W",email) # for special character
# print(re)


data = "python is programing langued java"
re= re.search(r"programing",data)
print(re)
re= re.match(r"programing",data)
print(re)


"""
serch  : jo puri string ko match karega

match :first element hi check karega agar nahi mila to wo return none karega
"""



