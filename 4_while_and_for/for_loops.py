# for loop statement, will start counting from 0 first (argument - 1)
import time

for number in range(11):
    print(number)

print()
print("Here are the numbers 7 through 14")
# can have different ranges depending on what's entered in the range function.
# range() is a function useful for a task that needs to be repeated a number of times
for number in range(7, 14):
    print(number)

print()
import random
# range() rolled the dice 5 times and printed the value. random.randint lets the computer pick from 1 through 6
for dice in range(5):
    dice_value = random.randint(1,6)
    print(dice_value)

print()
import random

number_of_dice = int(input('How many dice do you want to roll?: '))
for dice in range(number_of_dice):
    print(f'About to roll {number_of_dice} dice...')
    dice_value = random.randint(1,6)
    print(f'Dice {dice + 1} rolled {dice_value}')

print()
number_of_books = int(input('How many books did you buy?: '))
total = 0
for book in range(number_of_books):
    book_price = float(input('Enter the price of the book: $'))
    if book_price == 0:
        print('Nice you got a free book!')

    total = total + book_price

print(f'The total price for all {number_of_books} books is ${total:.2f}')

# for loops is for when you know you want it to stop/have the task repeat a limit number of times
# while loops is for when you don't know when you want it to stop and to have it keep repeating

for seconds in range(10,0,-1):
    print(seconds)
    time.sleep(1)
print('Happy new year!')

