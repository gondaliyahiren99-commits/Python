
print("-------------grocery bill---------------")
customer_name = input("Enter customer name :")
customer_member=input("have you customer member ")
item_member =int(input("Enter item :"))

total_amount=0
bill=0

disc_amt=0
for i in range(1,item_member-1):
    item_name = input("Enter item name :")
    item_quantity = int(input("Enter item quantity :"))
    item_price = int(input("Enter price of item :"))
    calc_item_price = item_quantity * item_price
    if item_quantity>5:
        discount = calc_item_price*5/100
        after_disc=calc_item_price-discount
        total_bill+=calc_item_price
print(total_bill)   

#extra discount
after_aply_disc=0
if total_bill>2000:
    total_bill-=(total_bill*15)/100
elif total_bill>1000:
    total_bill-=(total_bill*10)/100
elif total_bill>500:
    total_bill-=(total_bill*5)/100
else:
    print("No discount :")


if customer_member == "yes" or "YES":
    mem_disc=(total_bill *5)/100
    bill_befor_gst = total_bill - mem_disc

#apply gst
payable =0
gst=bill_befor_gst*18/100
payable =bill_befor_gst-gst

print(customer_name)
print(total_amount)
print(discount)
print(gst)
print(payable)




    


    





