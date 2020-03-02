"""
******************
Challenge#4:
******************
# Fibonacci(TBD)- Waiting for the updates from master

Tried to write a program helps to
1) print fibonacci# for the given input# position
2) print fibonacci series
ex:
Value: 2(fibonacci#) is the 4th position(input) in it's fibonacci series [0,1,1,2]
Value: 3(fibonacci#) is the 5th position(input) in it's fibonacci series [0,1,1,2,3]
3) Negative conditions would be handled for the given input# from user
"""


def test_fibonacci(input_number):
    fibolist = []
    for i in range(input):
        fibolist.append(i)
        if (i == 0 and input == 0) or (i == 1 and input == 1):
            break
        if i > 1:
            fibolist[i] = fibolist[i - 2] + fibolist[i - 1]
    print("The fibonacci# for the given input# position is {}".format(fibolist[input - 1]))
    print("List of fibonacci series for the given input# {}".format(fibolist))


print()
is_boolean = True
while is_boolean:
    number = input("Enter the number:")
    try:
        num = int(number)
        if num > 0:
            test_fibonacci(num)
            str_input = input("Great ! Do you want to Continue? Accept only True or False")
            if str_input == "True":
                is_boolean = True
            elif str_input == "False":
                print("Thank you!")
                is_boolean = False
            else:
                print('Accept only True or False here. '
                      'Please try!')
        else:
            print('Please try with only positive numbers starts from 1')
    except ValueError:
        print('Accept Only numbers! Please re-execute the script')
        is_boolean = False

