products= [
    {
        'name':'lap', 'price':35000 
    },
    {
        'name':'tv', 'price':5000
    },
        {
        'name':'phone', 'price':50000 
    },
]

price_dt=list(filter(lambda product: product["price"]>15000,products))
print(price_dt)


product_naem=list(map(lambda p: p['price'],price_dt))
print(product_naem)