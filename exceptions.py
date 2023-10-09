#   in java we throw errors, where as in python we raise exceptions

class CustomException(Exception):
    pass

x = 2
try:
    # print(x/0)
    raise CustomException("Understanding custom exceptions")
    raise Exception("Generic exception - I'm a custom exception")
    if not type(x) is str:  
        raise TypeError("Only strings allowed") #  built in function of python - raise error on your own
except NameError:
    print('\nNameError - something is undefined\n')
except ZeroDivisionError:
    print("\nDo not divide any number by 0\n")
except Exception as error:
    print(error)
else:       # this will run if no errors are thrown
    print("No errors\n")
finally:
    print("Will get printed irrespective of if there is an error or not")