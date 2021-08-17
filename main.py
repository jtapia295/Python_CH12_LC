# Find the Part A instructions in the LCHS textbook here:(https://education.launchcode.org/lchs/chapters/dictionaries/exercises.html)

# Write your return_cost function here:
def return_cost(a_dictionary, flavor_choice):
    if flavor_choice not in a_dictionary:
        return 0
    else:
        return a_dictionary[flavor_choice]
        



# Write your fanciest_flavor function here:


def main():
  flavors = {
    'chocolate' : 0.35,
    'vanilla' : 0.35,
    'strawberry' : 0.42,
    'cookies and cream' : 0.45,
    'mint chocolate chip' : 0.42,
    'fudge chunk' : 0.45,
    'saffron' : 2.25,
    'garlic' : 0.05
  }

  choice = 'vanilla'
  price = return_cost(flavors, choice)
  if price == 0:
    print("Sorry, we don't have {0}.".format(choice))
  else:
    print(f"The price for {choice} is ${price} per scoop.")

# Uncomment the lines below after you code your fanciest_flavor function.
  # print('---')
  # expensive_flavor = fanciest_flavor(flavors)
  # print(f"The most expensive flavor we have is {expensive_flavor}.")




print('<',('-')*20,'>')


# Find the Part B & C instructions in the LCHS textbook here:(https://education.launchcode.org/lchs/chapters/dictionaries/exercises.html)

import random

# Code your assign_tickets function here:


# Code the Part C function here:


def main():
  names = ['Caleb', 'Naomi', 'Owen', 'Ava', 'Aaron', 'Lydia']

  
# if __name__ == '__main__':
#     print(main())


print('<',('-')*20,'>')



# Find the Part D & E instructions in the LCHS textbook here:(https://education.launchcode.org/lchs/chapters/dictionaries/exercises.html)

import string

# Code your character_count function here:


def main():
  text = "Python ROCKS!"

  
# if __name__ == '__main__':
