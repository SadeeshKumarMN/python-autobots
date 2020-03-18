from common.numtowords import num_to_words


def find_fibonacci(number):
    message = 'Oh! No! Please note that your input is invalid as per fibonacci program! ' \
              'This accepts only a positive integer from no#1! ' \
              'Example valid inputs: 1, 1234, 10, 123456'

    try:
        if isinstance(number, int):
            fibolist = []
            if number > 0:
                for i in range(number):
                    fibolist.append(i)
                    if i > 1:
                        fibolist[i] = fibolist[i - 2] + fibolist[i - 1]
                output = num_to_words(fibolist[number - 1])
            else:
                output = message
        else:
            output = message
        return output
    except ValueError:
        return message
