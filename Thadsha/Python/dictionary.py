print("==== Dictionary Example 1 ====")
d = {
    "name": "seelan",
    "age": 38,
    "address": "puttalai"
}
print(d)
print("Type of d:", type(d))

print("\n==== Creating Dictionary from List of Tuples ====")
data = [
    ("name", "Thadsha"),
    ("age", 19),
    ("address", "kokuvil")
]
print(data)
d1 = dict(data)
print(d1)
print("Age:", d1["age"])
print("Name:", d1.get("name"))
print("Address:", d1.get("address"))
print("City:", d1.get("city"))  # Key does not exist

d1.update(city="jaffna")
print("After adding city:", d1)

d1["NIC"] = "200583400834"
print("After adding NIC:", d1)

print("\n==== Dictionary Example 2 ====")
d2 = {
    "name": "yoga",
    "age": 38,
    "address": "puttalai"
}

d2["nic"] = "200583400"
d2.update({
    "age": 19,
    "Grade": 10
})
print(d2)
print("Is 'name' in d2?", "name" in d2)

del d2["age"]
print("After deleting age:", d2)

d2.pop("name")
print("After popping name:", d2)

d2.popitem()  # Removes last inserted item
print("After popitem:", d2)

# d2.clear()  # Uncomment to clear the dictionary
# print(d2)

print("\n==== Keys, Values, and Items ====")
print("Keys:", d2.keys())
print("Values:", d2.values())
print("Items:", d2.items())

print("\n==== Looping through Dictionary ====")
print("Keys and Values using keys():")
for key in d2.keys():
    print(key, d2[key])

print("\nValues using values():")
for value in d2.values():
    print(value)

print("\nKeys and Values using items():")
for key, value in d2.items():
    print(key, value)
