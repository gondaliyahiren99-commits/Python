import os
"""
mkdir() : when we want to creat directory
"""
print(os.getcwd())
print("success ")
"""
makedirs(): creat multiple directory nested directories
"""
os.makedirs("hi/123/1234")
count=len(os.listdir())
print(count)
print("succes  ")
