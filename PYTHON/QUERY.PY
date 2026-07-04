# # # #FID ALL INDEX OF F and append in list

# # # l1=[]
# # # name="abcfefsfaggdgvhhjjhdj"
# # # print(name.find("f",+6))
# # # ind=0
# # # for i in name:
# # #     ind=i.find("f",+ind)
# # # #     l1.append(ind)
    

# # # # print(l1)




# # # # print("=====================================")
# # # # [name1],[num1],[name2],[num2]
# # # # [name1,num2,name2,num1]


# # # # s1="Hiren age 24 and brother age is 30"

# # # # for i in range(len(s1)):
# # # #     if ord(s1[i])>=48 and ord(s1[i])<=57:
# # # #         print(s1[i],end="")
# # # #     elif ord(s1[i])>=58 and ord(s1[i])<=47:
# # # #         print(s1[i],end="")
# # # #     else:

# # # # name=[]
# # # # num=[]
# # # # l1=[]
# # # # l1.extend(("Hiren","python","java",1,2,14,18,))
# # # # print(l1)

# # # # l1.append("hello!")
# # # # print(l1)

# # # # l1.insert(2,"C")
# # # # print(l1)
# # # # for i in l1:
# # # #     if type(i)==str:
# # # #       name.append(i)
# # # #     else:
# # # #         num.append(i)
        
# # # # print(l1)
# # # # print(name)
# # # # print(num)

# # # # username=input("Enter UserName :")
# # # # Name,Surname=username.split(" ")
# # # # print(username)
# # # # print(Name)
# # # # if username.isalpha:
# # # #   print("YEs")
# # # # print(Surname)

# # # # num="7hjdbbjb"
# # # # flag=1
# # # # for i in range(len(num)):

# # # #   if num[i].isalpha:
# # # #     flag=0
# # # #     break
# # # #   else:
# # # #     print("NoT")
# # # # if flag==1:
# # # #   print("Valid")



# # # # #====================================================
# # # # s1="Hiren is 15243 and Ketan more than 45012 "
# # # # print(len(s1))
# # # # num=""
# # # # name=""
# # # # for var in range(len(s1)):
# # # #     if ord(s1[var])>=48 and ord(s1[var])<=57:
# # # #         num




# # # num=12
# # # name='hiren'
# # # name1='ramesh'
# # # num2=45

# # # #output=['hiren][ramesh][1245]
# # # print(f"{name}".split(),end=" ")
# # # print(f"{str(num)+ str(num2)}".split(" "),end="")
# # # print(f"{name1}".split(),end=" ")
# # # print("\n")

# # # name1="mohammed"
# # # name2="mustved"
# # # number1=12
# # # number2=23

# # # print(f"{name1.split()}",end="")
# # # print(f"{number1}{number2}".split(),end="")
# # # print(f"{name2.split()}")
# # # num=int(input("Enter Name :"))
# # # for i in range(2,num):
# # #     for j in range(2,num-1):
# # #         flag=1
# # #         if i%j==0:
# # #             flag=0
# # #             break
# # #     if flag!=0:
# # #         print(i)

# # # L2=[]
# # # L1=[15,25,14,18,75,94,85,35]

# # # for i in L1:
# # #     sum=0
# # #     while i>0:
# # #         r=i%10       
# # #         sum+=r
# # #         i//=10
# # #         print(i)
    
# # #     L2.append(sum)
# # # print(L2)


# # # li=[1,2,3,4,5,6,7]
# # # def sq(x):
# # #     return x*x


# # # sq_list=list(map(sq,li))
# # # print(sq_list)


# # # l2=list(map(lambda num : f"{num}=even" if num%2==0 else f"{num}=odd",li))
# # # print(l2)


# # # num=lambda x : f"{x} is positive " if x>0 else f"" 
# # # print(num(-34))


# # # l1=["java","python","php","css"]
# # # l2=[]
# # # for i in l1:
# # #     for j in i:
# # #         if 
       
# # #         if 
# # # print(l2)
# # # l1="i am hiren " 
# # # l2=[]
# # # for i in l1:
# # #     if i== " ":
# # #         continue
# # #     if i not in l2:
# # #         l2.extend([i,l1.count(i)])
# # # ['i', 2, 'a', 1, 'm', 1, 'h', 1, 'r', 1, 'e', 1, 'n', 1]
# # # print(l2)

# # # [12,15,[24,27,28,26],[27,26,32,[35,36,40,48]]]# to flatten list
# # # di={'name':'hiren','course':'python','brnch':'TopsTech','language':'english'}
# # # di2={}

# # # for k,v in di.items():
# # #     if len(v)<6:
# # #         continue
# # #     else:
# # #         di2[k]=v
# # # print(di2)   without new dic can posible


# # # l1 = [5,6,78,45,21,84,36,75,93,34]
# # # print(l1)

# # # l2 =sorted(l1)
# # # print(l2)

# # # t1 = 12,25,21,64,12
# # # print(t1)
# # # print(type(t1))


# # # l1 =["hiren" , 25 , "python" , 3.14 ]
# # # #['hren', 2, 'pthon', 314]

# # # l2=list(map(lambda a : int(a) if a.isnumeric() else a , map(lambda a : a[0]+a[2:],(map(lambda a :str(a) , l1)))))
# # # print(l2)
# # # l3 =[j for i in l1 for j in range(len(str(i))) if str(i)[1] !=j]

# # # print(l3)

# # # set1 = {1,2,3,4,5,6,7,8,9}
# # # set2={i for i in set1 if i%2==0}
# # # print(set2)

# # # di = {
# # #     "Name" : "Hiren" ,
# # #     "course" : "Python" ,
# # #     "Language" : "English"
# # #     }
# # # di1=  { k : v for k, v in di.items() if len(v)>5 }
# # # print(di1)



# # n="15 * 2 * 2".split()
# # status = True 
# # i=1
# # t =1
# # ok= 0
# # if '*' in n :
# #     while status:   
# #         if i < len(n)- ok:
# #             if i==1:
# #                 s_ind = n.index('*')
# #                 mul = int(n[s_ind-1]) *int(n[s_ind+1])
# #                 t = mul
# #                 i+=1
# #             else :
# #                 s_ind = n.index('*')+1
# #                 s_ind = n.index('*',s_ind)
# #                 ok = s_ind
# #                 t  *= int(n[s_ind+1])
# #                 i+=1
                
# #         else : 
# #             print(t)
# #             status= False
# # print(t)



# # n= 6
# # for i in range(1,6):
# #     for j in range(1,n-i):
# #         print(" ",end=" ")
# #     for k in range(1,i):
# #         print(" * ",end=" ")
# #     print("\n")

# # for i  in range(1,6):
# #     for j in range(1,6):
# #         if i==1 or i==5  or j==5 or j==1 or j==4:
# #             print(" * ",end ="")
# #         else:
# #             print("   ",end="")0o
# #     print("\n") 
# # n=6
# # for i in range(5,0,-1):
# #     for  j in range(1,n-i):
# #         print( " ",end =" ")
# #     for k in range(1,i):
# #         print(" * ",end=" ")
# #     print("\n")
# import random
# import time

# print("=" * 80)
# print("🎉 WELCOME TO KBC GAME 🎉".center(80))
# print("=" * 80)

# money = 0

# questions = [
#     {
#         "question": "Who is the Prime Minister of India?",
#         "options": {
#             "A": "Narendra Modi",
#             "B": "Salman Khan",
#             "C": "Virat Kohli",
#             "D": "Akshay Kumar"
#         },
#         "answer": "A"
#     },

#     {
#         "question": "Which language is used for AI and Data Science?",
#         "options": {
#             "A": "HTML",
#             "B": "Python",
#             "C": "CSS",
#             "D": "MS Word"
#         },
#         "answer": "B"
#     },

#     {
#         "question": "How many days are there in a week?",
#         "options": {
#             "A": "5",
#             "B": "6",
#             "C": "7",
#             "D": "8"
#         },
#         "answer": "C"
#     },

#     {
#         "question": "Which planet is known as the Red Planet?",
#         "options": {
#             "A": "Earth",
#             "B": "Mars",
#             "C": "Jupiter",
#             "D": "Venus"
#         },
#         "answer": "B"
#     },

#     {
#         "question": "Who invented the Computer?",
#         "options": {
#             "A": "Charles Babbage",
#             "B": "Newton",
#             "C": "Einstein",
#             "D": "Elon Musk"
#         },
#         "answer": "A"
#     }
# ]

# prize_money = [1000, 5000, 10000, 50000, 100000]

# lifelines = {
#     "50-50": True,
#     "Audience Poll": True,
#     "Phone Friend": True
# }

# for index, q in enumerate(questions):

#     print("\n" + "=" * 80)
#     print(f"Question {index + 1} for ₹{prize_money[index]}")
#     print("=" * 80)

#     print(q["question"])
#     print()

#     for key, value in q["options"].items():
#         print(f"{key}. {value}")

#     print("\nAvailable Lifelines:")
#     for k, v in lifelines.items():
#         if v:
#             print(f"👉 {k}")

#     use = input("\nDo you want lifeline? (yes/no): ").lower()

#     if use == "yes":

#         life = input("Enter lifeline name: ")

#         # 50-50
#         if life == "50-50" and lifelines["50-50"]:

#             lifelines["50-50"] = False

#             correct = q["answer"]

#             wrong = [x for x in q["options"] if x != correct]

#             remove = random.sample(wrong, 2)

#             print("\nRemaining Options:")

#             for key, value in q["options"].items():
#                 if key not in remove:
#                     print(f"{key}. {value}")

#         # Audience Poll
#         elif life == "Audience Poll" and lifelines["Audience Poll"]:

#             lifelines["Audience Poll"] = False

#             print("\nAudience Poll Results:")

#             ans = q["answer"]

#             for key in q["options"]:

#                 if key == ans:
#                     vote = random.randint(60, 90)
#                 else:
#                     vote = random.randint(5, 20)

#                 print(f"{key} ➜ {vote}%")

#         # Phone Friend
#         elif life == "Phone Friend" and lifelines["Phone Friend"]:

#             lifelines["Phone Friend"] = False

#             print("\n📞 Calling Friend...")
#             time.sleep(2)

#             guess = random.choice(
#                 [q["answer"], random.choice(list(q["options"].keys()))]
#             )

#             print(f"Friend thinks answer is: {guess}")

#         else:
#             print("❌ Lifeline already used or invalid.")

#     ans = input("\nEnter your answer (A/B/C/D): ").upper()

#     if ans == q["answer"]:

#         print("✅ Correct Answer!")
#         money = prize_money[index]

#         print(f"You won ₹{money}")

#         time.sleep(1)

#     else:
#         print("❌ Wrong Answer")
#         print(f"Correct Answer was: {q['answer']}")
#         break

# print("\n" + "=" * 80)
# print(f"🏆 GAME OVER | Total Winning Amount: ₹{money}")
# print("=" * 80)












# st = " hiren mustved mnisarg java jenish".split()
# for i in range(len(st)):
#     for j in range(i+1,len(st)+1):
#         if len(st[i])>len(st[j]):
#             st[i],st[j]=st[j],st[i]


# print(st)
# li=[1,2,4,5,7] 
# target=9
# new=[]
# for i in li :
#     num=target-i
#     if num in li:
#         new.append(f"{i}+{num}=9")
# print(new)
# def addTwoNumbers(l1, l2):
#     num1,num2,revsum ="","",""
#     for i in l1[::-1]:
#         num1 = num1+str(i)    
#     for i in l2[::-1]:
#         num2 = num2+str(i)   
#     str(sum) = int(num1)+int(num2)
#     for i in str(sum[::-1]):
#         revsum = revsum + str(i)
#     return int(revsum)
# print(addTwoNumbers([2,4,3],[5,6,4]))
