'''
@ASSESSME.USERID: fa6375
@ASSESSME.AUTHOR: Faraj Aliyev
@ASSESSME.DESCRIPTION: Assignment 3.1
@ASSESSME.ANALYZE: YES
'''

import math


def fact(x):
    if x > 0: 
        return math.factorial(int(x))
    return 0

def root(y):
    if y > 0:
      return math.sqrt(float(y))
    return 0


def trunk(z):
    return math.trunc(z)
    
    
"""
  Expected:10 factorial = 3628800
  The square root of 9.0 = 3.0
  10.5 truncated = 10
  Returned:Factorial is:  3628800
  The square root of 9.0 is 3.0
  truncated 10
  """


def main():
   a1 = int(input("Enter a numeric value: "))
   print(a1, "factorial","=",fact(a1))


   a2 = float(input("Enter a numeric value: "))
   print("The square root of",a2, "=", root(a2))

   a3 = float(input("Enter a numeric value: "))
   print(a3,"truncated","=",trunk(a3))


if __name__ == "__main__":
    main()