def countdown(n):
    for i in range(1, n + 1):
        print((n+1)-i)
        if i == n:
            print("Lift off!")


def reverse_string(s):
    ranges = len(s)
    reverse = ""
    for i in range(1, ranges + 1):
        char = s[-i]
        reverse = reverse + char
    return reverse

def is_palindrome(s):
    ranges = len(s)
    palindrome = False
    for i in range(0, ranges - 1):
        if ranges % 2 == 1:
            even = ranges - 1
            middle = (even/2)
            if i == middle:
                break
        if s[i] == s[-(i+1)]:
            palindrome = True
        else:
            palindrome = False
            break
    return palindrome

recursionfib = []
num1 = 0
num2 = 1
original = 0
newnum = 0

def fib_recursion(n): # current focus
    if num1 == 0:
        original = n
    n = n - 1
    print(n)
    if n == 0:
        return
    else:
        fib_recursion(n)

def fib_iterative(n):
    fibonacci = []
    n1 = 0
    n2 = 1
    newnum = 0
    for i in range(0, n):
        if i == 0:
            fibonacci.insert(i, 0)
        elif i == 1:
            fibonacci.insert(i, 1)
        else:
            newnum = n1 + n2
            n1 = n2
            n2 = newnum
            fibonacci.insert(i, newnum)
    print(fibonacci)
    print(fibonacci[n-1])

countdown(3)
print(" ")
revWord = reverse_string("hello")
palAns = is_palindrome("noon")

print(revWord)
print(palAns)
fib_iterative(15)

print(" ")
fib_recursion(15)

