customer_name = input("Enetr Customer Name : ")
clotthing_item = input("Eneter clothing item 1.shirt 2.jacket 3.jeans : ")
clthing_price = int(input("Enter clothimg price : "))
quantity = int(input("Enter quantity : "))


Total_Amount = clthing_price * quantity
Disc_Amount = 0
if(Total_Amount>500 and Total_Amount<999):
    Disc_Amount = Total_Amount - (Total_Amount*0.10)
elif(Total_Amount>1000 and Total_Amount<1999 ):
    Disc_Amount = Total_Amount - (Total_Amount*0.20)
elif(Total_Amount>2000):
    Disc_Amount = Total_Amount - (Total_Amount*0.30)

Extra_Disc_Deduct = 0
if(clotthing_item =="shirt"):
    Extra_Disc_Deduct = Disc_Amount - (Disc_Amount*0.05)
elif(clotthing_item == "jeans"):
    Extra_Disc_Deduct = Disc_Amount - (Disc_Amount*0.08)
elif(clotthing_item == "jacket"):
    Extra_Disc_Deduct = Disc_Amount - (Disc_Amount*0.12)

Total_payable = 0
if(Extra_Disc_Deduct<1000):
    Total_payable = Extra_Disc_Deduct - (Extra_Disc_Deduct*0.05)
else:
    Total_payable = Extra_Disc_Deduct - (Extra_Disc_Deduct*0.12)

print("--------------A one FashionShop--------------")
print( "Customer Name :",customer_name)
print("Item Name :",clotthing_item)
print("Total price :",clthing_price)
print("Total Quantity :",quantity)
print("Total Amount :",Total_Amount)
print("discount applied =",Total_Amount-Disc_Amount)
print("Extra Discount :",Disc_Amount-Extra_Disc_Deduct )
print("Final Payable Amount :",Total_payable)
