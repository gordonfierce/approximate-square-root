# Initialize a guess. What makes a good guess?
# Something closer than n-1, like n/2.

# While loop until a guess variable is good enough.


def find_root(my_num, precision=0.01):
    guess = my_num/2
    loop_pass = 1
    while (pow(guess, 2) - my_num) > precision:
        guess = (guess + (my_num / guess)) / 2
        print("Pass number {}: {}".format(loop_pass, guess))
        loop_pass += 1
    return guess

if __name__ == '__main__':
    while True:

        user_input = input("Enter a number: ")

        try:
            number = float(user_input)
            break
        except ValueError:
            print("Not a valid number.")

    if number < 0:
        pos_number = -1 * number
        positive_root = find_root(pos_number)
        guess = complex(positive_root, 1)

    else:
        guess = find_root(number)

    print("The square root of {} is {}".format(number, guess))
