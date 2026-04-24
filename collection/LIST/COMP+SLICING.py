l1=["python","java","php","f;utter"]

l2=[]

# for sub in l1:
#     l1.append(sub[::3])

# print(l1)

#with comprehention
l2=[sub[::3] for sub in l1]    #agar hum dusri list print na karke wahi list me append karenege to wo automatic purani val remove karega
print(l1)
print(l2)


