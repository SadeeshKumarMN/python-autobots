def find_out_who_has_exactly_one_dollar(number_of_pennis, number_of_nickels, number_of_dimes, number_of_quarters):
    penny = .01
    nickel = .05
    dime = .10
    quarter = .25
    dollar = 1
    print(" ")
    print("Your goal is to enter enough change to make exactly $1.00")
    try:
        total = number_of_pennis * penny + number_of_nickels * nickel + number_of_dimes * dime + number_of_quarters * quarter;
        if total < dollar:
            amount_short = dollar - total
            print("Sorry, you lose! You were short {amount_short:.2f} cents.".format(amount_short=amount_short))
        elif total > dollar:
            amount_over = total - dollar
            print("Sorry, you lose! You were over {amount_over:.2f} cents.".format(amount_over=amount_over))
        else:
            print("Congratz! That's exactly $1.00! You win!")
    except ValueError:
        print('Accept Only whole numbers! Please re-execute the script')
