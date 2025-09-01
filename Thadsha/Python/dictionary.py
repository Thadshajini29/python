'''d={

    "name":"seelan",
    "age":38,
    "address":"puttalai"
    
}
print(d)
print(type(d))

data=[
    ("name","Thadsha"),
    ("age",19),
    ("address","kokuvil")
]
print(data)
d1=dict(data)
print(d1)
print(d1["age"])
print(d1.get("name"))
print(d1.get("address"))
print(d1.get("city"))
d1.update(city="jaffna")
print(d1)
d1["NIC"]="200583400834"
print(d1)'''

d2={
    "name":"yoga",
    "age":38,
    "address":"puttalai"
}
d2["nic"]="200583400"
d2.update({
    "age":19,
    "Grade":10
})
print(d2)
print("name" in d2)

del d2["age"]
print(d2)

d2.pop("name")
print(d2)

d2.popitem()
#d2.clear()
print(d2)

key=d2.keys()
print(d2)

value=d2.values()
print(value)

item=d2.items()
print(item)

for key in d2.keys():
    print(key,d2[key])

for value in d2.values():
    print(value)

for key,value in d2.items():
    print(key,value)