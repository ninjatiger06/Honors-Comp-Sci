def fibonacci(n):
   """ Recursive function to print Fibonacci sequence """
   if n <= 1:
       return n
   else:
       return(fibonacci(n-1) + fibonacci(n-2))

def main():
    nterms = int(input("How many terms? "))
    print("Fibonacci sequence: ")

    for i in range(nterms):
        print(fibonacci(i))

main()
