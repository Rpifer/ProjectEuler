# Each new term in the Fibonacci sequence is generated by adding the previous two terms.
# By starting with 1 and 2, the first 10 terms will be:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# By considering the terms in the Fibonacci sequence whose values do not exceed four million,
# find the sum of the even-valued terms.
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
