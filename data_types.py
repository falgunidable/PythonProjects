#literal assignment
fname = "david"
lname = "selmon"
contact = 90973891
check = False

# print(type(fname))
# print(type(fname) == str)
# print(type(lname))
# print(type(contact))
# print(isinstance(contact,int))
# print(type(check))

#constructor function
# pizza = str("Peporoni")
# print(type(pizza))
# print(type(pizza) == str)
# print(isinstance(pizza,str))

#concatination
fullname = fname + " " + lname
print(fullname)

fullname += "!"
print(fullname)

#I\'m \t - tab \n - enter

#string methods
print(fname.lower())
print(fname.upper())

multiline = '''
Hey you are the one, everything takes time!
    Your's will also take time.
'''

print(multiline.title())
print(multiline.replace('time','late'))
print(len(multiline))
print(multiline)

title = "menu".upper()
print(title.center(10,"="))
print("Coffee".ljust(16,".") + "$1".rjust(4))

#string index values
print(fname[1])
print(fname[1:]) #all letters from the givem index is printed
print(fname[1:-1]) #last index is not included

#complex type
comp_val = 5 + 3j
print(type(comp_val))
print(comp_val.real)
print(comp_val.imag)

import math #at top

print(math.pi)