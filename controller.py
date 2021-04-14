import tkinter
from tkinter import *
from tkinter import colorchooser
from Arduino import Arduino
onoff = 0

def compiler(t):
    exec(text.get(1.0, END))

def undo():
    try:
        text.edit_undo()
    except:
        pass

def redo():
    try:
        text.edit_redo()
    except:
        pass


def select_all(e):
    text.tag_add('sel', '1.0', 'end')


def clear_all(e):
    text.delete(1.0, END)


def bg_color():
    color = colorchooser.askcolor()[1]
    if color:
        text.config(bg=color)


def text_color():
    color = colorchooser.askcolor()[1]
    if color:
        text.config(fg=color)


def text_cursor_color():
    color = colorchooser.askcolor()[1]
    if color:
        text.config(insertbackground=color)


def window1():
    port = message.get()

    win1 = Tk()
    win1.geometry("1000x600")
    win1.title("Arduino compiller")
    win1['bg'] = '#00778f'

    toolbar = Frame(win1)
    toolbar.pack(fill = X)

    frame = Frame(win1)
    frame.pack(pady = 30)

    scroll = Scrollbar(frame)
    scroll.pack(side=RIGHT, fill = Y)
    global text
    text = Text(frame, font = "Roboto 15", width = 500, height = 700, bg = '#e1e9eb', fg = '#374042', undo = True, yscrollcommand = scroll.set)
    text.pack()
    text.config(insertbackground = 'black')
    text.insert(tkinter.END, """from Arduino import Arduino\nboard = Arduino("115200", port="{}")\nboard.pinMode({}, "OUTPUT")\nboard.digitalWrite(13, "HIGH")""".format(port, '12'))

    scroll.config(command = text.yview)

    button_compiller = Button(win1, text = "Run", font = "Roboto 15", command = lambda: compiler(False))
    button_compiller.place(x=50, y=15, anchor= "c", height=30, width=100, bordermode=OUTSIDE)
    button_undo = Button(win1, text = "Undo", font = "Roboto 15", command = undo)
    button_undo.place(x=160, y=15, anchor= "c", height=30, width=100, bordermode=OUTSIDE)
    button_redo = Button(win1, text = "Redo", font = "Roboto 15", command = redo)
    button_redo.place(x=270, y=15, anchor= "c", height=30, width=100, bordermode=OUTSIDE)

    m = Menu(win1)
    win1.config(menu=m)
    fm = Menu(m)
    m.add_cascade(label="Файл", menu=fm)
    fm.add_command(label="Скомпилировать", command = lambda: compiler(False))
    fm.add_command(label="Отменить", command=undo)
    fm.add_command(label="Применить", command=redo)

    fm.add_command(label="Выбрать все", command= lambda: select_all(True))
    fm.add_command(label="Отчистить", command= lambda: clear_all(True))
    fm.add_command(label="Цвет фона", command=bg_color)
    fm.add_command(label="Цвет текста", command=text_color)
    fm.add_command(label="Цвет курсора", command=text_cursor_color)

    win1.mainloop()

def window2():
    port = message.get()

    def on_off():
        global onoff
        if onoff == 1:
            buttonon.config(state=tkinter.NORMAL, bg="red")

            onoff = 0
        else:
            onoff = 1
            buttonon.config(state=tkinter.NORMAL, bg="green")

    def start():
        global onoff

        board = Arduino("115200", port=message.get())
        board.pinMode(w.get(), "OUTPUT")
        if onoff == 1:
            board.digitalWrite(w.get(), "HIGH")
        else:
            board.digitalWrite(w.get(), "LOW")

    root2 = Tk()
    root2.geometry("1000x600")
    root2['bg'] = '#e1e9eb'
    label_e = tkinter.Label(root2, bg="#00778f")
    opts = {'ipadx': 49, 'ipady': 10, 'fill': tkinter.BOTH}
    label_e.pack(side=tkinter.TOP, **opts)
    root2.title("Arduino controller")

    name_label1 = Label(root2, text="Выберите порт.")
    name_label1.place(x=90, y=90, anchor="c", height=50, width=150, bordermode=OUTSIDE)

    w = Scale(root2, from_=0, to=30, orient=HORIZONTAL)
    w.place(x=90, y=120, anchor="c", height=40, width=150, bordermode=OUTSIDE)

    buttonon = Button(root2, text="on/off", font="Roboto 15", command=on_off)
    buttonon.place(x=90, y=160, anchor="c", height=30, width=150, bordermode=OUTSIDE)

    bg_btn = Button(root2, text="Start", font="Roboto 15", command=start)
    bg_btn.place(x=90, y=200, anchor="c", height=30, width=150, bordermode=OUTSIDE)

    root2.mainloop()


root = Tk()
root.geometry("400x400")
root.title("Arduino Controller")
root['bg'] = 'grey'

button1 = Button(root, text = "Arduino Compiler", font = "Roboto 15", activebackground = '#585858', command=window1)
button1.grid(row = 0, column = 1, padx = 90, pady = 20)
button2 = Button(root, text = "Arduino Compiler", font = "Roboto 15", activebackground = '#585858', command=window2)
button2.grid(row = 1, column = 1, padx = 90, pady = 20)
button3 = Button(root, text = "Arduino Compiler", font = "Roboto 15")
button3.grid(row = 2, column = 1, padx = 90, pady = 20)

port_label = Label(root, text = "Введите порт.")
port_label.grid(row = 3, column = 1, pady = 10)

message = StringVar()
message_entry = Entry(textvariable = message)
message_entry.grid(row = 4, column = 1, pady = 10)


root.mainloop()

message = StringVar()
message_entry = Entry(textvariable = message)
message_entry.grid(row = 4, column = 1, pady = 10)


root.mainloop()
