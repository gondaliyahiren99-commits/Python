#nested quiz


QUIZ={
    'a':{
        'que' : 'who is pm of india ?',
        "op":{ "(a) narendra (b) salman khan  (c) shahruk khan (d) Akshay Kumar",},
         "ans": 'narendra modi'
    },      
    'b':{
        'que' : 'mot popular programing lan ?',
        'ans': 'python'
    },
    'c':{
        'que' : 'most popular cricketer' ,
        'ans': 'kohli'
    }
}

score=0
for ch in range(1,len(QUIZ)+1):
     i=chr(ch+96)
     print(i)
     print(f"{QUIZ[i]['que']}")
     print(f"op. {QUIZ[i]['op']}")
     print(QUIZ[i]["ans"])
     ans=input("Enter ans:")
     if ans==QUIZ[i]["ans"]:
        print("Correct")
        score+=1
     else:
        print("incorrect")
print(score)

