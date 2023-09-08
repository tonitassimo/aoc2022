base = 5


# DECIMAL TO SNAFU:
def decimal_to_snafu(decimal):
    base_5 = decimal_to_base_5(decimal)
    snafu_digits = base_5_to_snafu_digits(base_5)
    snafu_string = digits_to_snafu(snafu_digits)
    return snafu_string


def decimal_to_base_5(decimal):
    result = []
    while decimal != 0:
        rest = decimal % base
        decimal = decimal // base
        result.append(rest)
    return result


def base_5_to_snafu_digits(base_5):
    result = []
    for index, digit in enumerate(base_5):
        if digit > 2:
            result.append(digit - base)
            if index < len(base_5) - 1:
                base_5[index + 1] += 1
            else:
                result.append(1)
        else:
            result.append(digit)
    result.reverse()
    return result


def digits_to_snafu(digits):
    return [digit_to_snafu(digit) for digit in digits]


def digit_to_snafu(digit):
    if digit == -1:
        return '-'
    if digit == -2:
        return '='
    return str(digit)


# SNAFU TO DECIMAL:
def snafu_to_decimal(snafu):
    snafu = parse_snafu(snafu)
    length = len(snafu)
    result = 0

    for index, digit in enumerate(snafu):
        result += digit * (base ** (length - index - 1))

    return result


def parse_snafu(snafu):
    return [parse_character(c) for c in snafu]


def parse_character(character):
    if character == "-":
        return -1
    if character == "=":
        return -2
    return int(character)
