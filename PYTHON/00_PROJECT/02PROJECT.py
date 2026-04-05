
print("_________grocery bill________")
cus_name = input("Enter customer name :")
customer_mem = input("have a customer member yes or no :")
Num_of_item = int(input("Enter number of item purchase :"))

bill=0
for i in range(Num_of_item):
    item = input("Enter item name :")
    quantity = int(input("how much item purchase :"))
    price = int(input("Enter each item price"))
    item_total = quantity *price
    total_amount = quantity *price
    if quantity>5:
        item_total-=item_total*5/100
    bill+= item_total
#==========discount for have your bill above this amount===============

if bill>2000:
    discount = bill *15/100
    bill-=discount
elif bill>1000:
    discount = bill*10
    bill-=discount
elif bill>500:
    discount  = bill *5/100
    bill-=discount
else:
    print("No discount")
#========Have you Member of customer so count discount 5%=========
if customer_mem == "yes" or "YES":
    ex_disc = bill * 5/100
    bill-=ex_disc
#===========gst on your bill===========
gst=bill *18/100
payable =bill + gst
print("====================A one store=========================")
print("=================Bill==================")
print(cus_name)
print(total_amount)
print("-Discount =",total_amount-bill)
print("-gst =",gst)
print("   Finale payable amount =",payable)
