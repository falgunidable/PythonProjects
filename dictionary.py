dictex = {
    "Name" : "Roby",
    "Age" : 23
}

band = dict(name = "roby",age=23)

print(dictex)
print(band)
print(type(band))

#len
print(len(dictex))

#accessing the value
print(dictex["Age"])
print(band.get("name"))

#list all keys
print(band.keys())

#list all values
print(band.values())

#list all key/value pairs in tuple format
print(band.items())

#verify a key exists
print("name" in band)
print("range" in band)

#change values
band["age"] = 52
band.update({"brand":"samsung"})
print(band) #prints in dictionary format


print(band.pop("brand"))    #gives the value of the popped key item     -  pop() gives the value of the key which is popped whereas popitem() gives the whole key value pair as output
print(band)

#del band deletes everything inside dictionary band.clear() clears everything inside dict and returns an empty {}

# we can use band2 = band.copy() or band2 = dict(band) to copy one dictionary into another

#nested dictionaries
member1 = {
    "stage1" : "rate",
    "lang" : "eng"
}
member2 = {
    "stage2" : "fry",
    "lang" : "spn"
}
all = {
    "member1" : member1,
    "member2" : member2
}
print(all)

print(all["member2"]["lang"])

#set
num = {1,2,3,4}

num1 = set((3,4,5,1))

print(num)
print(num1)
print(type(num))
print(len(num1))

#sets no duplicate allowed
check = {2,10,1,1}
print(check)    #doesnt print the duplicate and prints in asc order

#true is a duplicate of 1 and false is a duplicate of 0
duplicacy = {1 , True,2,False,3,4,0}
print(duplicacy)

#check a value in set
print(2 in duplicacy)


#but you cannot refer to an element in the set with an index position or key

num.add(7)
print(num)

#adding elements from one set to another
morenums = {5,6,7,8}
num.update(morenums)
print(num)

#we can use update with lists, tuples & dictionaries

# merge two sets to cretae a new set
one = {1,3,5}
two = {2,4,6}
mynewset = one.union(two)
print(mynewset)

#intersection_update() for common values