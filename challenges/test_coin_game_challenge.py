"""" 
Objective
------------
Get enough change in coins to equal exactly $1.
Acceptance Criteria
------------------------
Create a program that asks the user to enter the quantities for the following coins:
pennies
nickels
dimes
quarters
Your program should sum up the value of each coin and then sum up all the coins for a grand total:
If the total is exactly $1, they win!
If the total is more than one dollar, tell them by how much they went over.
If the total is less than one dollar, tell them by how much they went under.

Challenge 1:Write the tests to validate the logic you know you will need to complete the game
"""
from courses.coins import find_out_who_has_exactly_one_dollar


def test_sum_pennies():
    # find_out_who_has_exactly_one_dollar(number_of_pennis,number_of_nickels,number_of_dimes,number_of_quarters)
    find_out_who_has_exactly_one_dollar(1, 2, 3, 4)
