from my_fib import my_fib

def my_fib_test():
    assert my_fib(1) == 1, 'hoge'
    assert my_fib(2) == 1, 'hoge'
    assert my_fib(3) == 2, 'hoge'
    assert my_fib(4) == 3, 'hoge'


if __name__ == '__main__':
    my_fib_test()
