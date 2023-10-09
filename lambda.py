squared = lambda num : num * num        # equivalent to def squared(num):    return num*num
print(squared(2))

addTwo = lambda num : num + 2
print(addTwo(10))

sum = lambda a,b : a + b
print(sum(3,3))

def builder(x):
    return lambda num : num + x

first = builder(10)
second = builder(20)

print(first(2))
print(second(2))

numbers = [2,3,4,5,6]
squre = map(lambda num : num * num, numbers)

print(list(squre))

odd_nums = filter(lambda num : num % 2 != 0, numbers)
print(list(odd_nums))

#   higher order functions - if function passed as an argument or as a return type