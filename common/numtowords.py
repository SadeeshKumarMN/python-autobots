def num_to_words(number):
    num = int(number)
    d = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
         6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
         11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
         15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen',
         19: 'nineteen', 20: 'twenty',
         30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty',
         70: 'seventy', 80: 'eighty', 90: 'ninety'}

    hundred = 100
    thousand = hundred * 10
    million = thousand * 1000
    billion = million * 1000
    trillion = billion * 1000

    if num < 20:
        return d[num]

    if num < hundred:
        if num % 10 == 0:
            return d[num]
        else:
            return d[num // 10 * 10] + ' ' + d[num % 10]

    if num < thousand:
        if num % 100 == 0:
            return d[num // 100] + ' hundred'
        else:
            return d[num // 100] + ' hundred and ' + num_to_words(num % 100)

    if num < million:
        if num % thousand == 0:
            return num_to_words(num // thousand) + ' thousand'
        else:
            return num_to_words(num // thousand) + ' thousand ' + num_to_words(num % thousand)

    if num < billion:
        if (num % million) == 0:
            return num_to_words(num // million) + ' million'
        else:
            return num_to_words(num // million) + ' million ' + num_to_words(num % million)

    if num < trillion:
        if (num % billion) == 0:
            return num_to_words(num // billion) + ' billion'
        else:
            return num_to_words(num // billion) + ' billion ' + num_to_words(num % billion)

    if num % trillion == 0:
        return num_to_words(num // trillion) + ' trillion'

    else:
        return num_to_words(num // trillion) + ' trillion ' + num_to_words(num % trillion)
