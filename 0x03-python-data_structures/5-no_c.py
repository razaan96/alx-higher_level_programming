#!/usr/bin/python3
def no_c(my_string):
    if my_string[:]:
        newstring = my_string.translate({ord("C"): None})
        secondstring = newstring.translate({ord("C"): None})
        return secondstring
    return my_string
