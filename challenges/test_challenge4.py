"""
******************
Challenge#4:
******************
Display the fibonacci sequence up to a certain number.
If I want the fibonacci for the 9(input) order of the sequence, I should see 21 and instead of displaying the number 21 in words
twenty one(output)
"""
from common.fibonacci import find_fibonacci


def test_fibonacci(input_number):
    output = find_fibonacci(input_number)
    print("The order of fibonacci sequence for the given input# is " + output)


test_fibonacci(0)
test_fibonacci(1)
test_fibonacci(9)
test_fibonacci(15)
test_fibonacci(1234)
test_fibonacci(1.0)
test_fibonacci(-1)
test_fibonacci("A")
