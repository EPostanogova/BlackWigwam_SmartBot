class Fibonacci:
    def __init__(self):
        pass

    def hello(self, name):
        print(f'Hello', name)

    def fibo(self, num):
        fib1 = fib2 = 1
        i = 0
        while i < num:
            fib1, fib2 = fib2, fib1 + fib2
            i = i + 1
            print(fib2)
            if i = = num:
                break
if __name__ = ='__main__':
        myfibo = Fibonacci()
        myfibo.hello('Bob')
        myfibo.fibo(3)