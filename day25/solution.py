from day25.converter import snafu_to_decimal, decimal_to_snafu, decimal_to_base_5


def solve():
    puzzle = open("day25/test.txt", "r").readlines()
    result = 0
    for line in puzzle:
        line = line[:-1]
        decimal = snafu_to_decimal(line)
        result += decimal
        # snafu = decimal_to_snafu(decimal)
        # base_5 = decimal_to_base_5(decimal)
        # base_5.reverse()
        # print(line + " --> " + str(decimal) + " --> " + str(base_5) + " --> " + str("".join(snafu)))
    snafu = decimal_to_snafu(result)
    print(result)
    print("".join(snafu))
