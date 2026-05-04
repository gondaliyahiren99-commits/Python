product=[
    {'name':'laptop','price':25000},
    {'name':'phone','price':15000},
    {'name':'tv','price':95000}
]
#fetch all product price 
pro_price=list(map(lambda p: p['price'],product))
print(pro_price)

#jis ki price 15k se jyad ho uska name

detail=list(filter(lambda p: p['price']>15000,product))
print(detail)
pro_name=list(map(lambda n:n['name'],detail))
print(pro_name)


#combine map and filter
name = list(map(lambda n : n["name"],list(filter(lambda a :a["price"]>15000,product))))
print(name)