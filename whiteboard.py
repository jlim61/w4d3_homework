# How to solve a problem:
    # Figure out what the input and its type are
    # Set up a function
    # Figure out what the output and its type are
    # Gather Your Knowledge
    # Gathers Your Constraints (Not always necessary) 
    # Determine a Logical way to solve the problem
        #Write each step out English
        #Write each step out in Python-esse (sudo-code)
    # Invoke and Test Your Function

# Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number.

# Example
# create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"
# The returned format must be correct in order to complete this challenge.

# Don't forget the space after the closing parentheses!


# Given a list of 10 numbers between 0 and 9. We have to return it in a specific format: (123) 456-7890
# maybe can target based on index and have it go in order.
# alst notice that we have to return a string

test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

def create_phone_number(alist):
    return f'({alist[0]}{alist[1]}{alist[2]}) {alist[3]}{alist[4]}{alist[5]}-{alist[6]}{alist[7]}{alist[8]}{alist[9]}'


print(create_phone_number(test_list))