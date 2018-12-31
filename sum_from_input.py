def sum_from_string(string: str) -> int:
    """:return: sum of all the natural numbers which are inside the string"""
    total = 0
    multiplier = 1
    for char in reversed(string):
        if char.isdigit():
            total += multiplier * int(char)
            multiplier *= 10
        else:
            multiplier = 1
    return total


if __name__ == '__main__':
    inputted_string = input('Enter your string (note: strings with only natural numbers are supported): ')
    print(f'Sum of numbers inside the list: {sum_from_string(inputted_string)}')
