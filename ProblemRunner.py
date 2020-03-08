import importlib

if __name__ == '__main__':
    debug = False

    test_number = 2

    module = importlib.import_module('Problems.Problem%s' % test_number)
    module.debug = debug
    result = module.test_problem()
    print('Answer:\n%s' % result)
