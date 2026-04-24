#fun with peramere and fun with return type

def isPalindrome(str):
    if str==str[::-1]:
        return "yes"
    else:
        return "Not"
result=isPalindrome("mom")
print(result)

result=isPalindrome("eli")
print(result)