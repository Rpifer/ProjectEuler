# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

debug = False


def test_problem():
    result = 0
    last_fib = 1
    current_fib = 1

    while current_fib < 4000000:
        if debug:
            print('current_fib:%d' % current_fib)
            print('last_fib:%d' % last_fib)
            print('result:%d' % result)

        if current_fib % 2 == 0:
            result += current_fib

        temp = last_fib
        last_fib = current_fib
        current_fib = current_fib + temp

    return str(result)
