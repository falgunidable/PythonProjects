users = ['jane','floral','riveria']

data = ['Dave', 42, True]

print('Dave' in users)
print('Dave' in data)
print(users[-1])
print(data.index(42))
print(users[0:2])

users.append("sara")
print(users)

users.extend(["Reddy","lal"])
print(users)

users.extend(data)
print(users)

users[2:2] = ["Hanna","Martin"]   #the words are shifted according to the index mentioned
print(users)

users[1:2] = ["Moana"]    #the word is replaced by the word given in the index
print(users)

users.remove("lal")
print(users)

users.pop()
users.pop()
print(users)

del users[0]
print(users)

print(data)
# del data  - gives error if the list is not present
data.clear()
print(data) # prints an empty list without any error

# users.sort(key=str.lower) alphabetically sorts the list
users.sort()
print(users)

nums = [4,20,12,1,5]
nums.reverse()
print(nums)

nums.sort()   #ascending
print(nums)

nums.sort(reverse=True)   #ascending
print(nums)

mylist = list([1,True,"Dev"])
print(mylist)

mytuple = tuple((1,3,4,6))
print(mytuple)

anothertuple = (10,12,5)
print(anothertuple)
print(type(anothertuple))

#to modify a tuple first we need to change into list() update it and then again change it to tuple() because tuple are immutable

(one, *two ,hey) = mytuple
print(one)
print(two)
print(hey)