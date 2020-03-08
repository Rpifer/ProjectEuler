import importlib

if __name__ == '__main__':
    test_number = 1
    module = importlib.import_module('Problems.Problem%s' % test_number)
    result = module.test_problem()
    print('Answer:\n%s' % result)
