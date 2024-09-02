Python 3.12.5 (v3.12.5:ff3bc82f7c9, Aug  7 2024, 05:32:06) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> print ('HEllo', end='*')
HEllo*
>>> print("8225")
8225
>>> print ('Hello',"python","8225",sep='_',end'*')
SyntaxError: positional argument follows keyword argument
>>> print ('Hello',"Python", "8225", sep = '__', end = '*')
Hello__Python__8225*
>>> print ('Hello',"Python", "8225", sep = '__')
Hello__Python__8225
>>> math_str=input('what is your math score')
what is your math score90
>>> 9/3
3.0
>>> 10%6
4
>>> x=1.5
>>> y=2
>>> x*=y
>>> print(x)
3.0
>>> 2**2
4
>>> 2**3
8
>>> 2+53%7
6
>>> print(format(123456,',d'))
123,456
>>> print(format(123456,'d'))
123456
