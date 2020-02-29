import math

def basechange_to10(first_input: str, first_base: int, first_key = "0123456789abcdefghijklmnopqrstuvwxyz", digits = 100):
    '''Converts a base (first_base) number to base 10, assuming the key for the first base is (first_key),
    Requirements: key >= first_base, all digits of first_input are in first_key'''
    if first_input == first_key[0]:
        return 0
    
    output = 0
    
    for index in range(len(first_input)):
        output += first_base**(len(first_input) - index - 1) * (key.index(first_input[index]))
        
    return output
    



def basechange_from10(number, new_base:int, key:str , digits = 100):
    """Converts a base 10 number to a new base, 
    with the digits in the new base corresponding to that index of the key"""

    message = ""

    if number < 0: # switches negative numbers to positive, sets variable to be converted back at end
        number = -number
        num_is_negative = True
    else:
        num_is_negative = False

    decimals = number % 1 #decimals = All digits less than 1

    if decimals != 0:
        number = number - decimals
        message = "."

        for i in range(digits):
            #For each digits in the final result, multiply by the base to find the number of whole units of that digit.
            entry = int(math.floor(decimals * new_base))
            message = message + key[int(entry)]
            decimals = new_base * decimals - entry

    if number == 0:#returns 0 if number == 0
        return key[0]

    while number >= 1:#repeats until number is totally reduced
        remainder = int(number % new_base)
        message = key[remainder] + message
        number = (number - remainder)/new_base

    if num_is_negative:#adds back the - sign
        message = "-" + message

    return message

def basechange(first_input:str, first_base: int, first_key, new_base:int, new_key:str = ""):
    if new_key =="":
        new_key = first_key
        
    number = basechange_to10(first_input, first_base,first_key)
    return basechange_from10(number,new_base, new_key)

if __name__ == "__main__":
    print("Converts a number in base 10 to a new base:\n")
    number = float(input("Your input number:\n").strip())
    new_base = int(input("Your new base:\n").strip())
    key = "0123456789abcdefghijklmnopqrstuvwxyz"
    print("The new number is: ", basechange_from10(number, new_base, key))

    print("____________________________________________________________________")

    print("Converts a number in a base to base 10:\n")
    number = input("Your input number:\n").strip()
    new_base = int(input("The base:\n").strip())
    key = "0123456789abcdefghijklmnopqrstuvwxyz"
    print("The number in base 10", basechange_to10(number, new_base, key))
    print("____________________________________________________________________")
   
    print("Converts a number in any base to a new base:\n")
    number = input("Your input number:\n").strip()
    first_base = int(input("The original base:\n").strip())
    second_base = int(input("The new base:\n").strip())
    key = "0123456789abcdefghijklmnopqrstuvwxyz"
    print("The final number:", basechange(number, first_base, key, second_base))