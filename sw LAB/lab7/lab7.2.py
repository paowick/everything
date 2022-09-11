from email import message
from tkinter import *
from tkinter import messagebox
win = Tk()
win.geometry('200x300')
win.title('calculator')
summit = StringVar()
ram = StringVar()
controlbus = StringVar()
summit.set('0')
def operand(val):
    if(summit.get() == '0'):summit.set('')
    sum = summit.get()
    val = sum+val
    summit.set(f'{val}')   
def clr():
    summit.set('0')
    ram.set('')
def plus():
    controlbus.set('plus')
    if(summit.get() != 0):
        ram.set(summit.get())
        summit.set('0')
def minus():
    controlbus.set('minus')
    if(summit.get() != 0):
        ram.set(summit.get())
        summit.set('0')
def multi():
    controlbus.set('muti')
    if(summit.get() != 0):
        ram.set(summit.get())
        summit.set('0')
def divide():
    controlbus.set('divide')
    if(summit.get() != 0):
        ram.set(summit.get())
        summit.set('0')
def div():
    controlbus.set('div')
    if(summit.get() != 0):
        ram.set(summit.get())
        summit.set('0')
def mod():
    controlbus.set('mod')
    if(summit.get() != 0):
        ram.set(summit.get())
        summit.set('0')
def SUM():
    ramint = ram.get()
    summitint = summit.get()
    ramint = float(ramint)
    summitint = float(summitint)  
    if(controlbus.get() == 'plus'):
        sum = ramint + summitint 
        summit.set(sum)  
    if(controlbus.get() == 'minus'):
        sum = ramint - summitint
        summit.set(sum)
    if(controlbus.get() == 'muti'):
        sum = ramint * summitint 
        summit.set(sum)
    if(controlbus.get() == 'divide'):
        try:
            sum = ramint / summitint 
            summit.set(sum)
        except ZeroDivisionError:
            messagebox.showerror('ERROR','Divide by Zero')
    if(controlbus.get() == 'div'):
        try:
            sum = ramint // summitint 
            summit.set(sum)
        except ZeroDivisionError:
            messagebox.showerror('ERROR','Divide by Zero')
    if(controlbus.get() == 'mod'):
        try:
            sum = ramint % summitint 
            summit.set(sum)
        except ZeroDivisionError:
            messagebox.showerror('ERROR','Divide by Zero')
    ram.set('0')
Entry(textvariable=summit).grid(sticky=EW,row=1,columnspan=4)
Button(text='clr',height=2,width=5,command=clr).grid(row=2,column=0)
Button(text='+',height=2,width=5,command=plus).grid(row=2,column=1)
Button(text='-',height=2,width=5,command=minus).grid(row=2,column=2)
Button(text='*',height=2,width=5,command=multi).grid(row=2,column=3)
Button(text='7',height=2,width=5,command=lambda: operand('7')).grid(row=3,column=0)
Button(text='8',height=2,width=5,command=lambda: operand('8')).grid(row=3,column=1)
Button(text='9',height=2,width=5,command=lambda: operand('9')).grid(row=3,column=2)
Button(text='/',height=2,width=5,command=divide).grid(row=3,column=3)
Button(text='4',height=2,width=5,command=lambda: operand('4')).grid(row=4,column=0)
Button(text='5',height=2,width=5,command=lambda: operand('5')).grid(row=4,column=1)
Button(text='6',height=2,width=5,command=lambda: operand('6')).grid(row=4,column=2)
Button(text='div',height=2,width=5,command=div).grid(row=4,column=3)
Button(text='1',height=2,width=5,command=lambda: operand('1')).grid(row=5,column=0)
Button(text='2',height=2,width=5,command=lambda: operand('2')).grid(row=5,column=1)
Button(text='3',height=2,width=5,command=lambda: operand('3')).grid(row=5,column=2)
Button(text='mod',height=2,width=5,command=mod).grid(row=5,column=3)
Button(text='0',height=2,width=5,command=lambda: operand('0')).grid(row=6,column=0)
Button(text='.',height=2,width=5,command=lambda: operand('.')).grid(row=6,column=1)
Button(text='=',height=2,width=12,command=SUM).grid(row=6,column=2,columnspan=2)
win.mainloop()
