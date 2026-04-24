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
    