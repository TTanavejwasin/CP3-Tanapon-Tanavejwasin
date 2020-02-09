from tkinter import *
import math


def leftClickButton(event):
    result = float(textBoxWeight.get())/math.pow(float(textBoxHeight.get())/100, 2)
    if result >= 30.0:
        labelResult.configure(text= "อ้วนมาก")
    elif result > 25.0 and result <= 29.9:
        labelResult.configure(text= "อ้วน")
    elif result > 23.0 and result <= 24.9:
        labelResult.configure(text= "น้ำหนักเกิน")
    elif result > 18.6 and result <= 22.9:
        labelResult.configure(text= "น้ำหนักปกติ เหมาะสม")
    else:
        labelResult.configure(text= "ผอมเกินไป")

mainWindow = Tk()
mainWindow.title("Weight Calculator")

labelHeight = Label(mainWindow,text="ส่วนสูง (cm.)")
labelHeight.grid(row=0,column=0)
textBoxHeight = Entry(mainWindow)
textBoxHeight.grid(row=0,column=1)

labelWeight = Label(mainWindow,text="น้ำหนัก (kg.)")
labelWeight.grid(row=1,column=0)
textBoxWeight = Entry(mainWindow)
textBoxWeight.grid(row=1,column=1)

calculateButton = Button(mainWindow,text="คำนวน")
calculateButton.grid(row=2,column=0)
calculateButton.bind('<Button-1>',leftClickButton)

labelResult = Label(mainWindow,text="ผลลัพธ์")
labelResult.grid(row=2,column=1)

showResult = Label(mainWindow,text="สถานะ")
showResult.grid(row=2,column=2)


mainWindow.mainloop()