# number_base_change
3 Python functions for changing the base of numbers. All functions are kept in [base_change.py](base_change.py)

## The Functions
### basechange_to10()
This function converts a base (first_base) number to base 10, assuming the key for the first base is (first_key). This works simply by multiplying the corresponding index of each digit in the input by the initial base to the power of the place in the input. For example, the second digit will be = (the base ^ 2) * (the value of the digit at that position as given by the key).
#### Inputs:
- first_input: str      -The input number/message as a string
- first_base: int       -The initial base
- first_key = "0123456789abcdefghijklmnopqrstuvwxyz"    - The key of the initial number
- digits = 100          -The number of decimal digits of the answer


### basechange_from10()
This function converts a base 10 number to a new base with the digits in the new base corresponding to that index of the key.
This function can accept decimal (floating point) numbers and negative numbers. 
#### Inputs:
- number                -The input base 10 number. Can be float or int
- new_base:int          -The new base, integer
- key:str               -The key to be used for base change
- digits = 100          -The number of places after the floating point for the answer

### basechange()
This function combines the two above functions by converting a number from the first base to base 10 then from base 10 to the final base.
#### Inputs:
- first_input:str       -The input string
- first_base: int       -The input base (integer)
- first_key             -The key to convert from the first base to base 10
- new_base:int          -The second base
- new_key:str = ""      -The key to convert from base 10 to the new base, NOTE: if no parameter is given, new_key is set to first_key.


## The Endgoal
The endgoal of this project was to see what the digits of pi would be if pi was converted to base 26 and the key was "abcdefghijklmnopqrstuvwxyz". These are the digits: 

**d.drsqlolyrtrclrggukbjkpsrfvkrodhljrfszsoxnhxzewt...**
BIG NEWS : nh shows up in the first 50 digits ;). New Hampshire represent.
