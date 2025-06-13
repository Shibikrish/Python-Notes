'''
https://docs.google.com/document/d/1FKz7SnHsTt2ujbanEQwPboZ0QpSwl2g4GnwpfgTzk6Y/edit?tab=t.0
'''

from math import sqrt, log, sin

def mathmod(inp):
    sq_rt=sqrt(inp)
    print("Square root:",sq_rt)
    logar=log(inp)
    print("logarithm:", logar)
    s_in=sin(inp)
    print("Sine:", s_in)

val=int(input("Enter a number:"))
mathmod(val)

