def q1():
    list = [1,2,3,4,5,6,7,8,9,10]
    print(sum(list))
    return

def q2():
    inp = abs(int(input("Enter a positive number to get the factorial of\n--> ")))
    
    def factorial(num):
        if num < 2:
            return 1
        else:
            return num * factorial(num-1)
    
    print(factorial(inp))
    return

def q3():
    term = int(input("Which term of the fibonacci sequence would you like to find?\n --> "))


def q4():
    def sum_of_digits(num):
        if num == 0:
            return 0
        else:
            return (int(num) % 10) + sum_of_digits(int(num / 10))
        
        
def q5():
    a = int(input("Enter first number to find their GCD -->"))
    b = int(input("Enter second number  to find their GCD -->"))

    def euclidean(a, b):
        AdivideB = a / b
        AmodB = a % b
        
            
        
        

    print(sum_of_digits(abs(int(input("Enter a positive integer to get the sum of it's digits of -->")))))	