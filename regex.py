import re


def is_valid_string(s):

    """
    this is a function that checks if a sting  contains characters A-z and 0-9
    """
    pattern = re.compile(r'^[a-zA-Z0-9]+$')
    return bool(pattern.match(s))

#example tests
print(is_valid_string("Mbuta2024"))   #True
print(is_valid_string("Goodmorning@Nancy"))  #False
print(is_valid_string("BOOK"))       #True
print(is_valid_string("apple"))    #True
print(is_valid_string("198989"))     #True


#question 2


def match_a_to_b(s):
    """
    this is a function that checks if a string starts with 'a' and ends with 'b'"""
    pattern = re.compile(r'^a.*b$')
    return bool(pattern.match(s))

# Example cases
print(match_a_to_b("aXYZb"))     # True
print(match_a_to_b("ab"))        # True
print(match_a_to_b("cab"))       # False  

