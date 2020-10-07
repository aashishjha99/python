a = "  Hello,  World!"
print(a.strip())
print(a.lower())
print(a.upper())
print(a.replace("H","j"))
print(a.split(" , "))
txt = "The rain is in spain stays mainly in the plain"
x = "ram"  not in txt
print(x)
a = "hello"
b = "world"
c = a + " " +b
print(c)
age = 22
Txt = " my name is aashish and i am {}yrs old "
print(Txt.format(age))
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {2} pieces of item {0} for {1} dollars."
print(myorder.format(quantity,itemno,price))
