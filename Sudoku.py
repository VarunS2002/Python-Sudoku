from tkinter import *
from tkinter import messagebox
import pickle
import os
import random
import array_module

# Main Window

root = Tk()
root.title("Sudoku")
root.resizable(False, False)
grid_frame = Frame(root)

# Creates Empty Save File

save_exists = os.path.isfile("save_game")
save_exists2 = os.path.isfile("save_game2")
save_exists3 = os.path.isfile("save_game3")

if save_exists:
    pass
else:
    create_save = open("save_game", "xb")
if save_exists2:
    pass
else:
    create_save2 = open("save_game2", "xb")
if save_exists3:
    pass
else:
    create_save3 = open("save_game3", "xb")

# Flag

global flag
flag = random.randint(1, 3)
global a
a = str(flag)

# Predefined Unsolved

global start
start = []

# Predefined Editable

global game
game = start.copy()

# Predefined Solved

global gameSolved
gameSolved = []

# Populating Arrays

if flag == 1:
    start = array_module.start_1.copy()
    game = start.copy()
    gameSolved = array_module.gameSolved_1.copy()
elif flag == 2:
    start = array_module.start_2.copy()
    game = start.copy()
    gameSolved = array_module.gameSolved_2.copy()
elif flag == 3:
    start = array_module.start_3.copy()
    game = start.copy()
    gameSolved = array_module.gameSolved_3.copy()

# Variables

global k
k = 0


# Choose Window

def choose_window():
    window = Toplevel()
    window.title("Choose")
    window.resizable(False, False)
    window.geometry('220x200')
    window.attributes('-topmost', True)
    window.grab_set()
    window.focus_force()
    return window


# Choose Game Function

def choose_game():
    window = choose_window()
    listbox = Listbox(window)
    for u in range(1, 4):
        listbox.insert(END, u)
    listbox.focus_force()
    bframe = Frame(window)

    # Ok Button Function

    def do_ok():
        text = listbox.get(ACTIVE)
        global start
        global game
        global gameSolved
        global flag
        if text == 1:
            start = array_module.start_1.copy()
            game = start.copy()
            gameSolved = array_module.gameSolved_1.copy()
            flag = 1
        elif text == 2:
            start = array_module.start_2.copy()
            game = start.copy()
            gameSolved = array_module.gameSolved_2.copy()
            flag = 2
        elif text == 3:
            start = array_module.start_3.copy()
            game = start.copy()
            gameSolved = array_module.gameSolved_3.copy()
            flag = 3
        global a
        a = str(flag)
        new()
        window.destroy()

    # Cancel Button Function

    def do_cancel():
        window.destroy()

    ok = Button(bframe, command=do_ok, text="Ok")
    ok.pack(side='left', fill='x', expand='1')

    cancel = Button(bframe, command=do_cancel, text="Cancel")
    cancel.pack(side='right', fill='x', expand='1')

    listbox.pack(side='top', fill='both', expand='1')
    bframe.pack(side='top', fill='x', expand='1')

    window.mainloop()


# Choose Number Function

def choose(btn_x, btn_y):
    x = 'a' + str(btn_x) + str(btn_y)
    exec('y=' + x + str(['text']), globals())
    global y
    y = (y % 9) + 1
    exec('a' + str(btn_x) + str(btn_y) + f'.config(text ={y} )')
    index = (btn_x * 9) + btn_y
    game[index] = y


# Restart Game Function

def new():
    global game
    game = start.copy()
    global colourTxt
    for z in range(9):
        for w in range(9):
            exec('a' + str(z) + str(w) + '.config(text = game[(z*9)+w])')
            if game[(z * 9) + w] == 0:
                exec('a' + str(z) + str(w) + '.config(state = NORMAL)')
                colourTxt = "blue"
            else:
                colourTxt = "black"
                exec('a' + str(z) + str(w) + '.config(state = DISABLED)')
            exec('a' + str(z) + str(w) + '.config(fg = colourTxt)')
    file.entryconfig(file.index(0), label=f"Choose Game: {a}", state=NORMAL)
    file.entryconfig(file.index("Load Game"), state=NORMAL)
    file.entryconfig(file.index("Save Game"), state=NORMAL)
    file.entryconfig(file.index("Check Result"), state=NORMAL)


# Load Function

def load():
    def load2(f):
        global game
        try:
            with open(f, 'rb') as save_game:
                game = pickle.load(save_game)
            for z in range(9):
                for w in range(9):
                    exec('a' + str(z) + str(w) + '.config(text = game[(z*9)+w])')
            messagebox.showinfo("Restored", "Your progress has been restored")
        except:
            messagebox.showerror("Error", "Please save a game before using function")

    if flag == 1:
        load2('save_game')
    elif flag == 2:
        load2('save_game2')
    elif flag == 3:
        load2('save_game3')


# Save Function

def save():
    def save2(f):
        with open(f, 'wb') as save_game:
            pickle.dump(game, save_game)
        messagebox.showinfo("Saved", "Your progress has been saved")

    if flag == 1:
        save2('save_game')
    elif flag == 2:
        save2('save_game2')
    elif flag == 3:
        save2('save_game3')


# Clear Save Function

def clear():
    def clear2(f):
        save = open(f, "wb")
        save.flush()
        save.close()
        messagebox.showinfo("Cleared Save", "Your saved game has been cleared")

    if flag == 1:
        clear2("save_game")
    elif flag == 2:
        clear2("save_game2")
    elif flag == 3:
        clear2("save_game3")


# Result Function

def check():
    if game == gameSolved:
        messagebox.showinfo("Result", "You won")
    else:
        messagebox.showinfo("Result", "You lost")


# Solution Function

def sol():
    global game
    game = gameSolved.copy()
    for z in range(9):
        for w in range(9):
            text = gameSolved[(z * 9) + w]
            index = (z * 9) + w
            game[index] = text
            exec('a' + str(z) + str(w) + f'.config(text = {text})')
            exec('a' + str(z) + str(w) + '.config(state = DISABLED)')
            file.entryconfig(file.index("Load Game"), state=DISABLED)
            file.entryconfig(file.index("Save Game"), state=DISABLED)
            file.entryconfig(file.index("Check Result"), state=DISABLED)


# Grid

for rowindex in range(9):

    for colindex in range(9):

        if rowindex in (0, 1, 2, 6, 7, 8) and colindex in (3, 4, 5):
            colour = "white"
        elif rowindex in (3, 4, 5) and colindex in (0, 1, 2, 6, 7, 8):
            colour = "white"
        else:
            colour = "light grey"

        x = start[k]
        k = k + 1
        if x == 0:
            colourTxt = "blue"
        else:
            colourTxt = "black"
        btn_name = ''
        exec('btn_name = "a" + str(rowindex) + str(colindex)')
        exec(
            btn_name + '= Button(grid_frame, width=8, height=4, bg=colour,fg=colourTxt, text=x,command=lambda '
                       'i=rowindex, '
                       'j=colindex : choose(i,j))')
        exec(btn_name + '.grid(row=rowindex, column=colindex, sticky=N+S+E+W)')
        if colourTxt == 'black':
            exec('a' + str(rowindex) + str(colindex) + '.config(state = DISABLED)')
        grid_frame.pack()

# Option Menu

menubar = Menu(root)
file = Menu(menubar, tearoff=0)
file.add_command(label=f"Choose Game: {a}", command=choose_game)
file.add_command(label="Restart Game", command=new)
file.add_separator()
file.add_command(label="Load Game", command=load)
file.add_command(label="Save Game", command=save)
file.add_command(label="Clear Saved Game", command=clear)
file.add_separator()
file.add_command(label="Check Result", command=check)
file.add_command(label="Show Solution", command=sol)
file.add_separator()
file.add_command(label="Quit", command=exit)
menubar.add_cascade(label="Menu", menu=file)
root.config(menu=menubar)

root.mainloop()
