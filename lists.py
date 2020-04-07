import random

"""
Print a message to the console indicating whether each value of
`number` is in the `my_randoms` list.
"""

# variable that contains the list method to create a list
my_randoms = list() 
# for loop. i is any integer in a range up to ten
for i in range(10):
    # adds integers to my_randoms. random makes the numbers, randrange chooses random number from list
    my_randoms.append(random.randrange(1, 6))

# variable containing numbers 1 to 10
numbers_1_to_10 = range(1, 11)

# loops over numbers in 1 to 10 range
for number in numbers_1_to_10:
    # sets the variable to start as false
    the_numbers_match = False

    # loops over ints in my_randoms list
    for random in my_randoms:
        # if the number is equal to the random number then it is in the list
        if number == random:
            # then the variable is switched to true
            the_numbers_match = True


if the_numbers_match:
    print(f'{number} is in the random list')
else:
    print(f'{number} is not in the random list')