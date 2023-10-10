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