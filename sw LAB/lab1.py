# -*- coding: utf-8 -*-
"""Lab01_116310462007-0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fD190T5R-GStFClaD7J-_BZ8SQoxr-rg
"""
#=======================================1=========================================
pi = 3.14159
msg = 'CPE'

print ('1 Hello', msg, pi)
print ('2 Hello %s %f'%('CPE', 3.14159))
print ('3 Hello %s %.2f'%('CPE', 3.14159))

print ('4 Hello {} {}' .format(msg, pi))
print ('5 Hello {} {:.2f}' .format(msg, pi))
print ('6 Hello {var2} {var1:.2f}'.format(var1=pi,var2=msg))

print(f'7 Hello {msg} {pi}')
print(f'8 Hello {msg} {pi:.2f}')

print('9 Hello ', end=""); print(msg)
print('10 Hello ' + 'CPE')
print("11 Hello " +"CPE")

print(''' 12 Hello "CPE"
RMUTT
2019
''')

print(""" 13 Hello 'CPE' RMUTT
2
0
1
9 """)

print('14',end=' ');print(22/7)
print('15 {:0.50f}'.format(22/7))
#print("16HELLO CPE")
print('17 Type of pi={} and id={} '.format(type(pi),id(pi)))

Pie = pi
print('18 Type of Pie={} and id={} '.format(type(Pie),id(Pie)))





#=====================================2============================================
C= float(input('Enter C : ')) 
print('Result :\nF = %.2f' %(((9/5)*C)+32))
print('K = %.2f' %(C+273.15))