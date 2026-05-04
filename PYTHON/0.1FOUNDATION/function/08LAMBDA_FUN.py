"""
lambda function : is sn anonyms fun without any name its called lambda function

using of lambda keyword we can define lambda function.

sy  :
      
      var = lambda perameter : exopression 


      lambda fun can acess as many as perameter but cam return single expresinon

      use for a little func create 
"""

def tab(num):
    ans=num*num
    return ans

print(tab(5))


ans = lambda num :num*num
print(ans(10))


#=================================


answer=lambda num : num%2==0
print(answer(15))


#===============
pos= lambda n : n>0
print(pos(-25))

