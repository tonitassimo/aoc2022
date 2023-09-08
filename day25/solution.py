from day25.converter import snafu_to_decimal, decimal_to_snafu


def solve():
    puzzle = open("day25/data.txt", "r").readlines()
    result = 0
    for line in puzzle:
        line = line[:-1]
        decimal = snafu_to_decimal(line)
        result += decimal
        # snafu = decimal_to_snafu(decimal)
        # print(line + " --> " + str(decimal) + " --> " + str("".join(snafu)))
    snafu = decimal_to_snafu(result)
    print(result)
    print("".join(snafu))
