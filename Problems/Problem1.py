# If we list all the natural numbers below 10 that are multiples of 3 or 5,
# # we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.


def test_problem():
    result = 0
    multiple = 1

    while multiple * 3 < 1000:
        result += multiple * 3
        multiple += 1

    multiple = 1
    while multiple * 5 < 1000:
        if multiple % 3 != 0:
            result += multiple * 5
        multiple += 1

    return str(result)
