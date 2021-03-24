
import tkinter
from tkinter import *
from tkinter import colorchooser
from Arduino import Arduino


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





root = Tk()
root.geometry("400x400")
root.title("Arduino Controller")
root['bg'] = 'grey'

button1 = Button(root, text = "Arduino Compiler", font = "Roboto 15", activebackground = '#585858', command=window1)
button1.grid(row = 0, column = 1, padx = 90, pady = 20)
button2 = Button(root, text = "Arduino Compiler", font = "Roboto 15")
button2.grid(row = 1, column = 1, padx = 90, pady = 20)
button3 = Button(root, text = "Arduino Compiler", font = "Roboto 15")
button3.grid(row = 2, column = 1, padx = 90, pady = 20)

port_label = Label(root, text = "Введите порт.")
port_label.grid(row = 3, column = 1, pady = 10)

message = StringVar()
message_entry = Entry(textvariable = message)
message_entry.grid(row = 4, column = 1, pady = 10)


root.mainloop()
