mydict={
    "ashutosh":" a coder ",
    "collage":"where we study ",
    "roll no":[1,2,3,4,5],
    "dairy": {"cow" : " milk"}
}
print(mydict["ashutosh"])
print(mydict["collage"])
print(mydict["roll no"])
print(mydict["dairy"]["cow"])

print(mydict.keys())
print(list(mydict.keys()))
print(mydict.values())
print(mydict.items())
print(mydict)

updatemydict={
    "name":"user name",
    "class":"standard"
}
mydict.update(updatemydict)
print(mydict)
print(mydict.get("ashutosh"))
    
