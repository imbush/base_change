def to_base_10(num: str, from_base: int, key="0123456789abcdefghijklmnopqrstuvwxyz", digits=100, minus_sign="-") -> int:
    """Convert a num in from_base to base 10."""
    if len(key) < from_base:
        raise ValueError("Must have key length > base")

    if num == key[0]:
        return 0

    if num[0] == minus_sign:
        sign = -1
    else:
        sign = 1

    new_num = 0
    num_length = len(num)

    for i in range(num_length):
        try:
            new_digit = key.index(num[i])
        except ValueError:
            raise ValueError("digit, " + str(num[i]) + ", not in key")
        new_num += from_base ** (num_length - i - 1) * new_digit

    return new_num * sign


def from_base_10(num, new_base: int, key: str, digits=100, minus_sign="-") -> str:
    """Convert num, a base 10 number to new_base."""
    if new_base <= 1:
        raise TypeError("new_base <= 1")
    elif not (isinstance(num, int) or isinstance(num, float)):
        raise TypeError("num must be float or int type")

    new_num = ""

    if num == 0:
        return key[0]
    elif num < 0:
        num = -num
    else:
        minus_sign = ""

    decimals = num % 1  # All digits less than 1
    if decimals != 0:
        num = num - decimals
        new_num += "."
        for _ in range(digits):
            entry = int(decimals * new_base)  # Number of decimal units in 1/base digit
            new_num = new_num + key[entry]
            decimals = new_base * decimals - entry  # Shift left

    while num >= 1:  # Until num is reduced
        remainder = int(num % new_base)
        new_num = key[remainder] + new_num
        num = (num - remainder) / new_base

    return minus_sign + new_num


def basechange(num: str, first_base: int, end_base: int, first_key="0123456789abcdefghijklmnopqrstuvwxyz", end_key="", minus_sign="-"):
    """Convert num from first_base to end_base given corresponding keys."""
    if end_key == "":
        end_key = first_key

    intermediate = to_base_10(num, first_base, first_key, minus_sign)
    return from_base_10(intermediate, end_base, end_key, minus_sign)
