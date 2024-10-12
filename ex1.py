import random
#


bool_list = [random.choice([True, False]) for _ in range(3)]
print('random list of true & false:', bool_list)

print('true in list:', all(bool_list))

print('at least 1 true:', any(bool_list))

print('if all the list contains no', not any(bool_list))

print('at least one false:', any(not x for x in bool_list))

random_numbers = [random.randint(-2,2) for _ in range(5)]
print('list of random numbers between -2 to 2:', random_numbers)

print('all number are different then 0:', all(x != 0 for x in random_numbers))

print('at least one number that is no 0:', any(x != 0 for x in random_numbers))

print('all number are 0:', all(x == 0 for x in random_numbers))

print('at least one 0:', any(x == 0 for x in random_numbers))

