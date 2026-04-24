url="http ://ww.google.com"
if url.startswith("http ://") or url.startswith("https : //"):
    if url.endswith("google.com") or url.endswith(".in"):
        print("valid")
    else:
        print("end is not valid :")

else:
    print("not start with http protocol :")