print(15/7) #float
print(15//7) #int
print(15%7) #mod
print(2**8) #power
print(_)
x=-2
if x<0:
    x=0;
    print(x);
#x = int(input("input x"))

###########################################
for i in range(1,10,3):
    print(i);
########################################
for num in range(2, 10):
     if num % 2 == 0:
         print("Found an even number", num)
         continue
     
     print("Found a number", num)
     num = num + 2;
num = 100;
print (num);

###########################
def fib(n):    # write Fibonacci series up to n
     #"""Print a Fibonacci series up to n."""
     a, b = 0, 1
     while a < n:
         print(a, end=' ')
         a, b = b, a+b
     print()
     
     
fib(1000)
##########################
def fib2(n):  # return Fibonacci series up to n
     """Return a list containing the Fibonacci series up to n."""
     result = []
     a, b = 0, 1
     while a < n:
         result.append(a)    # see below
         a, b = b, a+b
     return result
print(fib2(1000))
###########################
ok=int(input())
x=int(2.5)
################################
def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)
ask_ok('Do you really want to quit?',2,'Come on, only yes or no!')
###############################
def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L
print(f(1))
print(f(2))
print(f(3))
########################
#squares = [x**2 for x in range(10)]
squares = list(map(lambda x: x**2, range(10)))
print(squares)
###############################################

