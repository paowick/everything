from tkinter import *
win = Tk()
win.geometry('250x300')
win.title('Body-Mass Index(BMI)')
ent_w = StringVar()
ent_h = StringVar()
bmi=StringVar()
Status=StringVar()
def bt_click():
    if(ent_h.get() != '' and ent_w.get() != ''):
        numh = ent_h.get()
        numw = ent_w.get()
        numh = int(numh)
        numw = int(numw)
        sum = numw/(numh**2)*10000 
        bmi.set(f'BMI = {sum:.2f}')
    else:
        bmi.set(f'BMI = n/a')
    if(ent_h.get() != '' and ent_w.get() != ''):
        if(sum < 18.5):
            Status.set('Status = Underweight')
            Label(textvariable = Status , bg='white',fg='black').grid(row=6,column=1,columnspan=3)
        elif(sum > 18.5 and sum < 24.9):
            Status.set('Status = Normal')
            Label(textvariable = Status , bg='green',fg='pink').grid(row=6,column=1,columnspan=3)
        elif(sum > 24.9 and sum < 29.9):
            Status.set('Status = Overweight ')
            Label(textvariable = Status , bg='yellow',fg='black').grid(row=6,column=1,columnspan=3)
        elif(sum > 29.9):
            Status.set('Status = Obese')
            Label(textvariable = Status , bg='red',fg='white').grid(row=6,column=1,columnspan=3)
    else:
        Status.set('Status = n/a')
        Label(textvariable = Status , bg='SystemButtonFace',fg='black').grid(row=6,column=1,columnspan=3)
Label(text = 'Weight',borderwidth=20).grid(row=1,column=1)
Entry(textvariable = ent_w).grid(row=1,column=2)
Label(text = 'Height',borderwidth=20).grid(row=2,column=1)
Entry(textvariable = ent_h).grid(row=2,column=2)
Button(text='คำนวณค่า',width=10,command=bt_click).grid(row=3,column=2)
Label(text = 'ผลการคำนวล',borderwidth=20).grid(row=4,column=1)
Label(textvariable = bmi,borderwidth=20).grid(row=5,column=1,columnspan=3)
Label(textvariable = Status).grid(row=6,column=1,columnspan=3)
win.mainloop()