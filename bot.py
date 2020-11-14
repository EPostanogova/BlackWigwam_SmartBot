
#Name = input ("Username: ")
def hello(Name):
    print(f'Hello,{Name}')


#def fibonacci():
    #b = 1, 1
    #while True:
        #yield a #zapominaem mesto restarta
        #a, b = b, a + b

#gen = fibonacci()
#for i in range(num):
    #print(next(gen)

#num=int(input("Enter quantity of namber:"))
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