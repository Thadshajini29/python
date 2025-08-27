'''s={"Maths","Tamil","English","Maths","Science"}
print(s)
print(type(s))
s.add("ICT")
print(s)
s.update(["SFT"])
print(s)
s.remove("Maths")
print(s)
s.discard("BST")
print(s)
s.pop()
print(s)
s.clear()
print(s)


number={70,50,60,80,40,60,65,70,80,95}
num=set(number)
print(num)

a={2,4,6,8,10,12}
b={12,14,20,16,2,8}
c=a|b
print(c)

c=a.union(b)
print(c)
d=a.intersection(b)
print(d)

e=a-b
print(e)
f=b-a
print(f)

g=a^b
print(g)
h=a.symmetric_difference(b)
print(h)'''

a={1,2,3}
b={1,2,3,4,5}
c={4,5,6}
d=a|b|c
print(d)
e=a&b&c
print(e)
print(a<=b)
print(a.issubset(b))
print(a.issuperset(b))
print(a.issubset(c))