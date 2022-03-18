from tkinter import *

window = Tk()
window.title("Miles to Kilometers Converter")
window.minsize(width=200, height=100)
window.maxsize(width=200, height=100)

# entry
inputEntry = Entry(width=5)
inputEntry.grid(column=1, row=0)


# button
def buttonClick():
    try:
        result = float(inputEntry.get()) * 1.6
    except Exception as ex:
        print(ex)
        result = 'error'
    kilometerNum.set(result)


button = Button(text="Convert", command=buttonClick)
button.grid(column=1, row=2)

# Miles label
Label(text="Miles", font="Arial").grid(column=2, row=0)

# Km label
Label(text="Km", font="Arial").grid(column=2, row=1)

# equal to label
Label(text="is equal to", font="Arial").grid(column=0, row=1)

kilometerNum = StringVar()
kilometerNum.set('0.0')
numLabel = Label(textvariable=kilometerNum, font="Arial")
numLabel.grid(column=1, row=1)

window.mainloop()
