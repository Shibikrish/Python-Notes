'''
https://docs.google.com/document/d/1FKz7SnHsTt2ujbanEQwPboZ0QpSwl2g4GnwpfgTzk6Y/edit?tab=t.0
'''

def factorial(n):
    if n < 2:
        return 1 
    else:
        return n * factorial(n-1)
def factorial_loop(n):
    fact=1
    for i in range(1,n+1):
       fact*=i
    return fact

val=int(input("Enter a number:"))
#out=factorial(val)
#print("Factorial of",val ,"is", out) 
outlo=factorial_loop(val)
print("Factorial of",val ,"is", outlo)
