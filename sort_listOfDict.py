l = [
    {'name': 'p1' , 'price':50},
    {'name': 'p2' , 'price':30},
    {'name': 'p3' , 'price':40},
    {'name': 'p4' , 'price':20},
]

l1 = sorted(l, key = lambda x : x['price'])

for i in l1:
    print(i)