
Name = input ("Username: ")
def hello(Name):
    print(f'Hello,{Name}')

def main():
        hello(Name)
if __name__ == "__main__":
          main()

def fibonacci():
    a, b = 1, 1
    while True:
        yield a #zapominaem mesto restarta
        a, b = b, a + b

gen = fibonacci()
for i in range(5):
    print(next(gen))

def main():
    fibonacci()
if __name__=="__main__":
    main()