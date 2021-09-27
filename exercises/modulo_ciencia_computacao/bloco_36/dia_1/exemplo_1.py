def squared_array(numbers):
    array_of_squares = []
    for number in numbers:
        array_of_squares.append(number * number)

    return array_of_squares


def multiply_array(numbers):
    result = 0
    for number in numbers:
        result *= number

    return result
