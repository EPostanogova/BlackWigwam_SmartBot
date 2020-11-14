
def fibo(num):
    fib1=fib2=1
    i=0
    while i < num :
        fib1,fib2 = fib2, fib1+fib2
        i=i+1
        print(fib2)
        if i==num:
            break
def main():
    fibo(5)
if __name__=="__main__":
    main()