# function to check string is palindrome or not
def is_palindrome(str_val):
    str_val = str_val.lower()

    # make reverse of string and set to rev_str
    rev_str = str_val[::-1]
    # return s == rev_str

    # check if original and reversed str are equal or not.
    if str_val == rev_str:
        return True
    return False


# function to check string is palindrome or not using join function
def is_palindrome_v2(str_val):
    str_val = str_val.lower()

    # using predefined functions(reversed and join) to reverse into rev_str
    rev_str = ''.join(reversed(str_val))

    # checking if both str (original and reversed) are equal or not
    if str_val == rev_str:
        return True
    return False


# Python main driver entry
if __name__ == '__main__':
    str_entry = "Kayak"
    print("Checking if this word is palindrome:", str_entry)

    # 1st Implementation Check
    check_one = is_palindrome(str_entry)
    print("Check 1:", check_one)

    # 2nd Implementation Check
    check_two = is_palindrome_v2(str_entry)
    print("Check 2:", check_two)
