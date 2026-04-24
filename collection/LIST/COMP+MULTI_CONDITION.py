"""

syntax:

value if condition else value if condition else value if condition loop 


"""
marks=[99,45,80,68,75]
l2=[]
l2=[  "A" if marks>90 else " B" if marks>80 else "C" if marks>60 else "D" if marks>40 else "Fail" for i in marks ]


#=======================================================================================================================

l2=[(word,"palindrome") if word[::-1]==word else (word,"not a palindrome") for word in l1]
print(l2)

l2=[12,45,87,8,-45,-73,24,21,28,-47,-98]#['Even And Pos', '  Odd And Nag', '  Odd And Nag', 'Even And Pos', 'zero', 'zero', 'Even And Pos', '  Odd And Nag', 'Even And Pos', 'zero', 'Even And Nag']
l1=["Even And Pos" if i%2==0 and i>0 else "Even And Nag" if i%2==0 and i<0 else "  Odd And pos" if i%2!=0 and i>0 else "Odd And nag" if i%2==0 and i<0 else "zero" for i in l2 ]
print(l1)