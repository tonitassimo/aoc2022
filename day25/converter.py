def decimal_to_snafu(decimal):
    pass


def snafu_to_decimal(snafu):
    base = 5
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
