"""

"""
products ={} #blnck dictionary

menu=  """

            MENU
        1 for pro manager
        2 for custor
        3 for exit


       """

status=True
while status:
    print(menu)


    role =int(input("Enter Role :"))
    if role==1:
        print("*************   WELCOME TO MANAGER PANEL       ***************")
        man_status=True
        while man_status:
            SubDict={}#nested

            manager_menu = """

                    manager your product
                    1 add new pro
                    2 for remove
                    3 for view
                    4 for exit
                    
            """
            print(manager_menu)
            man_choice=int(input("Enter man choice :"))
            if man_choice==1 :
                print("****************** ADD NEW PRO  ****************")
                pro_name=input("Enter pro name :")
                price=int(input("Enter price :"))
                Disc=int(input("Enter Disc :"))

                
                SubDict['price']=price
                SubDict['disc']=Disc

                #add content insubDictionary
                products[pro_name]=SubDict

                print("\n***************************SUCCESSFULLY*****************")
            elif man_choice==3:
                print("\n*************** ALL PRODUCT *******************")
                for k,v in products.items():
                    print(f" {k}   | price : {products[k]['price']} discount  : {products[k]['disc']}")
                    print("******************************")
                    print(k)
            else:
                man_status=False
   
    elif role==2:
        cus_ord={}
        cus_status=True
        while cus_status:
            item={}
            customer_menu=  """

                1 oreder
                2 bill
                2 cancell 
                3 payament

                            """
            cus_ch=int(input("Enter Customer choice :"))
            if cus_ch==1:
                print("What you Want :")
                item_name=input('Enter item Name :')
                bill_no=int(input("Enter Bill No "))
                que=int(input("Enter Que ;"))
                price=int(input("ENter Price :"))
                total_bill=price*que
                gst=(total_bill*18)
                payable=total_bill+(total_bill*18)

                item['bill no']=bill_no
                item['price']=price
                item['que']=que
                item['total']=total_bill
                item['GST']=gst
                item["Payament"]=payable
                
                cus_ord[item_name]=item

            elif cus_ch==2:
                print('SHOW BILL')
                for k,v in cus_ord.items():
                    cus_ord[k]['total']+=cus_ord[k]['total']
                    cus_ord[k]['gst']+=cus_ord[k]['gst']
                    cus_ord
                    print(f" |{k}|\n bil=  {cus_ord[k]['bill no']}       \n price={cus_ord[k]['price']}\n quentity {cus_ord[k]['que']} ")
                print(f"bill={cus_ord[k]['total']}")

                

            else:
                pass
    
#=====================================================================

#     pro={}
# menu="""\n
#                         :menu:
#                     press 1 for meneger
#                     press 2 for costomenr
#                     press 3 for exit
# \n""".upper()

# while 1:
#     print(menu)
#     role=int(input("enter your name :".upper()))
#     if role==1:
#         while 1:  
#             print("\n\t\t~~~~~~~~~~~~~~~~~~~~:welcom meneger:~~~~~~~~~~~~~~~~~~~~\n".upper())
#             m_menu="""
#                                 ::menu::
#                             press 1 for adding 
#                             press 2 for removing 
#                             press 3 for seeing
#                             press 4 for exit
#             """.upper()
#             print(m_menu)
#             m_ch=int(input("enter your choice :".upper()))
#             if m_ch==1:
#                 print("\n\t\t-----------------------------:add:--------------------------------\n")
#                 while 1:
#                     sub={}
#                     pro_name=input("enter your product name :".title())
#                     pro_pri=int(input(f"enter your {pro_name.upper()} price :".title()))
#                     pro_q=int(input("enter your product quantity :".title()))
#                     pro_dis=float(input("enter discount :".title()))
#     #               adding on sub 
#                     sub['price']=pro_pri
#                     sub['quantity']=pro_q
#                     sub['discount']=pro_dis
#                     # adding sub into main pro
#                     pro[pro_name]=sub

#                     more=input("""
#                                     do you wanted to add more product
#                                     press -> (y) for yes
#                                     press -> (n) for no
#                     enter :""".upper()).upper()
#                     if more=="Y":
#                         continue
#                     else:
#                         break

#             elif m_ch==2:
#                 print("\n\n\t\t-----------------------:remove:------------------------------\n".upper())
#                 ch=input("enter wat you wanted to removing eliment : ".upper())
#                 pass
#             elif m_ch==3:
#                 print("\n\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
#                 for i in pro:
#                     print(f"{i}:- price : RS.{pro[i]['price']} | quantity : {pro[i]['quantity']} | discount : {pro[i]['discount']}%")
#                     print("_______________________________________________________\n\n")
#             else:
#                 break

#     elif role==2:
#         total=0
#         all_total=0
#         discount_total=0
#         print("\t\t<><><><><><><><><><>:welcom:<><><><><><><><><><>".upper())
#         while 1:
#             print("""\n\t________________>menu<___________________""".upper())
#             j=1
#             for i in pro:
#                 print(f"\t\tpress -> {j} for {i}")
#                 j+=1
#             j=1
#             u_ch=int(input("\nenter your choice :".upper()))
#             for i in pro:
#                 if u_ch==j:
#                     print(f"your choice is {i}\n".title())
#                     print(f"\tit's price = RS.{pro[i]['price']}")
#                     print(f"\n\n-------if you by more then 5 quantity you will gate {pro[i]["discount"]}% discount.----------\n".upper())
#                     q=int(input("enter your quantity:".upper()))
#                     total=q*pro[i]['price']
#                     discount=0
#                     if q>=5:
#                         discount=(total*pro[i]['discount'])/100
#                     break
#                 else:
#                     j+=1
#             all_total+=total
#             discount_total+=(total-discount)
#             print(f"your total : {total} and discount : {discount}% = RS.{total-discount}")
#             print("\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
#             more_by=input("\ndo you wanted to by more items press (y) or press (n) :".title()).upper()
#             if more_by=="Y":
#                 continue
#             else:
#                 print("\n\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n")
#                 print("thank you for comming".upper())
#                 print(f"your all total bil is = RS.{all_total} and with discount you have to pay = RS.{discount_total}".title())
#                 break
#         break
         
#     else:
#         break