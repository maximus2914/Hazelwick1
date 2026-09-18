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

def is_palindrome(s)
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

def fib_recursive():
    print(" ")

countdown(3)
print(" ")
revWord = reverse_string("hello")
palAns = is_palindrome("noon")

print(revWord, palAns)

