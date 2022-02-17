from unicodedata import name


a={
    "name" : "manish",
    "clss" : "14th",
    "college": "Nit hamirpur",
    1:2,
    "b":[5,2,3,1,4],
    "a1":{ 
        "n1":"ram"
     }
}
print(a)
print(type(a))
print(a["name"])
print(a.get("clss"))
print(a.values())
print(a.keys())
print(a.items())
a["clss"]="none"
print(a)
print(a["a1"]["n1"])

