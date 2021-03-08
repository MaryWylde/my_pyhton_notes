from math import *

# print("Hello World!")

#drawing a shape!!
#
# print("    /|")
# print("   / |")
# print("  /  |")
# print(" /   |")
# print("/____|")

# variable is a container where we can store certain data values

# creating variable !!

# character_name = "John"
# character_age = "25"
# print("Thee once was a man named " + character_name + ",")
# print("he was " + character_age + " year old." )
#
# character_name = "Mike"
# print("And there was another man named " + character_name + ",")
# print("he was also " + character_age + " year old." )

#STRINGS
# phrase = "this lesson"
#
# print(phrase + " is coooool")

# function is a block of code and it performs specific operation for us
#
# phrase = "This Lesson"
# print(phrase.upper().isupper())
# # length print(len(phrase))
# # getting first string print(phrase[0])
#
# # tell us where specific character is located
# # print(phrase.index("i")) you csan even use word
#
# print(phrase.replace("Lesson", "Cat"))

# NUMBERS
# my_nums = 5.6
# print(floor(my_nums))

# # getting input from users
# name = input("Enter your name: ")
# age = input("Enter your age: ")
# print("hello " + name + " You are " + age + " !")


# buliding basic calculator

# num1 = input(" Enter a number: ")
# num2 = input(" Enter another number: ")
# # by default it becomes string :/ not cool
# # we have to use int to it will give us integer number and not a atring
# #result =  int(num1) + int(num2)
#
# #float for any number
# result =  float(num1) + float(num2)
# print(result)
#

# MAD LIBS GAME
# 3 vars
# color = input("Type a color: ")
# plural_noun = input("Now write a plural noun: ")
# celebrity = input("And name of your favorite celebrity: ")
#
# print("Roses are " + color )
# print(plural_noun + " are blue")
# print("I love " + celebrity)

# My CARD AGAINST HUMANITY CARD


# verb = input("Enter a verb: ")
# verb2 = input("Enter another verb: ")
# plural = input("Enter a plural noun e.g. Cats or Dogs: ")
#
#
# print("That's one small " + verb + " for man, one giant " + verb2 + " for " + plural )
#


# LISTS
# first list !! array eli
# its ok to add numbs booolean, strings.. in list
# friends = ["Karen", "Kevin", "Jim", "Jane", 'Anna']
#
# #accessing based on their index
# # -1 indexing back of the list
# # changing smt from the list
# friends[1] = "John"
# print(friends[1])

# LIST FUNCTIONS

lucky_numbers = [4, 60, 15, 2, 23, 45, 66, 72]
friends = ["Karen", "Kevin", "Jim", "Jane", "Anna", "Anna", "Anna"]
# extend literally joins both lists together
# friends.extend(lucky_numbers)
# append() is basically aloowing to append/add new more values
# friends.append("Child")

#if we want to add in the middle or somewhere we want we use inser()
# it takes 2 params - 1 is index 2-new value
# friends.insert(1, 'David')

# for removing - remove()
# friends.remove("Anna")

# for removing literally everything - clear()
# friends.clear()

# getting rid off last element- pop()
# friends.pop()

# to check if we have a value
# print(friends.index("Anna"))

#counting vvalues (to see if we have more than one)
# print(friends.count("Anna")) // 3

# #sorting
# lucky_numbers.sort()
# print(lucky_numbers)

# reverse
# lucky_numbers.reverse()

#copying list with its all value

# friends2 = friends.copy()
# print(friends2)

# TUPLES - for unchangable DATA
# is similar to list
# for storing multiple pices of information
#its immutable / unchangable
# coordinates = (4, 5)
# # also you can store tuples inside list [(), ()]
# # coordinates[0] = 10 this is throwing eroor
# print(coordinates[1])

# FUNCTIONS - performs specific task
# keyword- def
# has to be intented- use tab
# parameter (...) is a pice of info that we give to funciton
# def sayhi(name, age):
#     print("Hello " + name + " you are " + str(age))
# if we want to pss just a number we have to convert it into string
# str(age)

# print("Top")
# sayhi("Mary", 22)

# print("Bottom")

# RETURN - STATEMENT # wont work another print inside function
# def cube(num):
#     return num*num*num
#     # no code after return statement
#
# result = cube(4)
# print(result)

# IF STATEMENT
# IF condition - can be true or false

# is_male = False
# is_tall = False
# #its not gonna input anything if condition is false
# # we can add 2 values after if - one can be true or both
#
# # if is_male or is_tall:
# #     print("you are a male or tall or both")
# # else:
# #     print("You are neither male not tall")
#
# # and - when both conditions have to be true!
# if is_male and is_tall:
#     print("you are a tall male")
# elif is_male and not(is_tall):
#     print("You are a short male")
# elif not(is_male) and is_tall:
#     print("You are not male but a tall")
# else:
#     print("You arenot a male and not tall")


# IF STATEMENT AND COMPARISONS
# comparison operators == - equal != - not equal <+ - < = >+ = > =

# def max_num(num1, num2, num3):
#     if num1 >= num2 and num1 >= num3:
#         return num1
#     elif num2 >= num1 and num2 >= num3:
#         return num2
#     else:
#         return num3
#
# print(max_num(222, 8, 13))


# BETTER ADVANCED CALCULATOR
#3 vars = 2 for nums - 1 for operator
# # float for converting string to number
# num1 = float(input("Enter first number: "))
# op = input("Enter operator: ")
# num2 = float(input("Enter second number: "))
#
# if op == "+":
#     print(num1 + num2)
# elif op == '-':
#     print(num1 - num2)
# elif op == "/":
#     print(num1 / num2)
# elif op == "*":
#     print(num1 * num2)
# else:
#     print("Invalid operator")


# DICITONARIES - allows  us to store info in key value pairs
# like in basic dictionary word = key, definition = value
# every key has to be unique
#key values can be nums, strings

# monthConversions = {
#     "Jan": "January",
#     "Feb": "February",
#     "Mar": "March"
# }
#
# # print(monthConversions["Jan"])
# # another way
# # print(monthConversions.get("Jan"))
#
# #adding default vale
#
# print(monthConversions.get('Jaan', 'Not a valid value'))


# WHILE LOOP
# i = 1
# while i <= 10: # as long as condition true, it keeps looping
#     print(i)
#     i += 1
# print("Done with loop")


# BUILDING GUESSING GAME
secret_word = "giraffe"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
     if guess_count < guess_limit:
          guess = input("Enter a guess: ")
          guess_count += 1
     else:
          out_of_guesses = True

if out_of_guesses:
     print("You Lose!")
else:
     print("You Win!")



