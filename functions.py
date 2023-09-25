def hello():
    print("Hello Functions")

hello()

def sum(num1, num2): #parameters inside function
    print(num1+num2)

#arguments can change but paramenters cannot

sum(2,3) #arguments - actual data
sum(4,3) #arguments

def sum1(num1, num2): #parameters inside function
    if type(num1) is not int or type(num2) is not int:
        return 0 #returns none
    return num1+num2

total = sum1("h",2)
print("Sum: "+str(total))

def multiple_items(*args): #multiple parameters
    print(args)
    print(type(args))

multiple_items("Dave",42)

def multiple_item_names(**kwargs): #multiple parameters with keyword arguments
    print(kwargs)
    print(type(kwargs))

multiple_item_names(first = "Dave",last = "final")