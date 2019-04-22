import tkinter


def btnClick():
    print(rbValue.get())
    if lbl['text'] == "you clicked me":
        lbl['text'] = "hello world"
    else:
        lbl['text'] = "you clicked me"

root = tkinter.Tk()

btn = tkinter.Button(root)
btn['text'] = "click me"
btn['width'] = 30
btn['height'] = 30
btn['highlightbackground'] = "red"
btn['command'] = btnClick
btn.grid(row=1, column=0)


lbl = tkinter.Label(root)
lbl['text'] = "Hello World"
lbl['width'] = 30
lbl.grid(row=0, column=0)


cb = tkinter.Checkbutton(root)
cb['text'] = "A"
cb.grid(row=0, column=1)



rb = tkinter.Radiobutton(root)
rb['text'] = "a"
rb.grid(row=0, column=2)


root.mainloop()


