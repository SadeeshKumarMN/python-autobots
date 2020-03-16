"""
******************
Challenge#4:
******************
write out the code for convert the word representation of a number
Ex: 2002 should display "two thousand two"
"""
from common.numtowords import num_to_words


def test_convert_word_to_string(num):
    print(num_to_words(num))


# inputs
test_convert_word_to_string(0)
test_convert_word_to_string(1)
test_convert_word_to_string(19)
test_convert_word_to_string(90)
test_convert_word_to_string(99)
test_convert_word_to_string(1234)
test_convert_word_to_string(2002)
test_convert_word_to_string(100000)
test_convert_word_to_string(1000000000)
test_convert_word_to_string(-1)
test_convert_word_to_string("A")
test_convert_word_to_string("1,00")
test_convert_word_to_string("")


