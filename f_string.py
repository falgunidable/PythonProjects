person = "faran"
coins = 3

print("\n%s has %s coins left" % (person,coins))
print("\n\n{} has {} coins left" .format(person,coins))
print("\n\n{1} has {0} coins left" .format(person,coins))
print("\n\n{person} has {coins} coins left" .format(person=person,coins=coins))
print(f"\n{person} has {coins} coins left\n")
print(f"\n{person.upper()} has {coins} coins left\n")

num = 10
print(f"\n2.25 is {num} whereas {2.25 * num:.2f}\n") #here .2 means 0.2 f is fixed to that much decimal point

print(__name__)