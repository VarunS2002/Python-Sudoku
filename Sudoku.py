from tkinter import *
from tkinter import messagebox
import pickle
import os

# Main Window

root = Tk()
root.title("Sudoku")
root.resizable(False, False)

# Creates Empty Save File

save_exists = os.path.isfile("save_game")
if save_exists:
    pass
else:
    create_save = open("save_game", "wb")
    create_save.close()

# Predefined Unsolved

start = [0, 7, 5, 0, 9, 0, 0, 0, 6,
         0, 2, 3, 0, 8, 0, 0, 4, 0,
         8, 0, 0, 0, 0, 3, 0, 0, 1,
         5, 0, 0, 7, 0, 2, 0, 0, 0,
         0, 4, 0, 8, 0, 6, 0, 2, 0,
         0, 0, 0, 9, 0, 1, 0, 0, 3,
         9, 0, 0, 4, 0, 0, 0, 0, 7,
         0, 6, 0, 0, 7, 0, 5, 8, 0,
         7, 0, 0, 0, 1, 0, 3, 9, 0]

# Predefined Editable

global game

game = start.copy()

# Predefined Solved

gameSolved = [1, 7, 5, 2, 9, 4, 8, 3, 6,
              6, 2, 3, 1, 8, 7, 9, 4, 5,
              8, 9, 4, 5, 6, 3, 2, 7, 1,
              5, 1, 9, 7, 3, 2, 4, 6, 8,
              3, 4, 7, 8, 5, 6, 1, 2, 9,
              2, 8, 6, 9, 4, 1, 7, 5, 3,
              9, 3, 8, 4, 2, 5, 6, 1, 7,
              4, 6, 1, 3, 7, 9, 5, 8, 2,
              7, 5, 2, 6, 1, 8, 3, 9, 4]

# Variables and Lists

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


# Choose Function

def choose(btn_x, btn_y):
    window = choose_window()
    listbox = Listbox(window)
    for i in range(1, 10):
        listbox.insert(END, i)
    listbox.focus_force()
    bframe = Frame(window)

    # Ok Button Function

    def do_ok():
        text = listbox.get(ACTIVE)
        exec('a' + str(btn_x) + str(btn_y) + f'.config(text = {text})')
        index = (btn_x * 9) + btn_y
        game[index] = text
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


# Restart Game Function

def new():
    global game
    game = start.copy()
    for z in range(9):
        for w in range(9):
            exec('a' + str(z) + str(w) + '.config(text = game[(z*9)+w])')
            if game[(z * 9) + w] == 0:
                exec('a' + str(z) + str(w) + '.config(state = NORMAL)')
    file.entryconfig(file.index("Load Game"), state=NORMAL)
    file.entryconfig(file.index("Save Game"), state=NORMAL)
    file.entryconfig(file.index("Check Result"), state=NORMAL)


# Load Function

def load():
    global game
    try:
        with open('save_game', 'rb') as save_game:
            game = pickle.load(save_game)
        for z in range(9):
            for w in range(9):
                exec('a' + str(z) + str(w) + '.config(text = game[(z*9)+w])')
        messagebox.showinfo("Restored", "Your progress has been restored")
    except:
        messagebox.showerror("Error", "Please save a game before using function")


# Save Function

def save():
    with open('save_game', 'wb') as save_game:
        pickle.dump(game, save_game)
    messagebox.showinfo("Saved", "Your progress has been saved")


# Clear Save Function

def clear():
    save = open("save_game", "wb")
    save.flush()
    save.close()
    messagebox.showinfo("Cleared Save", "Your saved game has been cleared")


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
            btn_name + '= Button(root, width=6, height=3, bg=colour,fg=colourTxt, text=x,command=lambda i=rowindex, '
                       'j=colindex : choose(i,j))')
        exec(btn_name + '.grid(row=rowindex, column=colindex, sticky=N+S+E+W)')
        if colourTxt == 'black':
            exec('a' + str(rowindex) + str(colindex) + '.config(state = DISABLED)')

# Option Menu

menubar = Menu(root)
file = Menu(menubar, tearoff=0)
file.add_command(label="Restart Game", command=new)
file.add_command(label="Load Game", command=load)
file.add_command(label="Save Game", command=save)
file.add_command(label="Clear Saved Game", command=clear)
file.add_command(label="Check Result", command=check)
file.add_command(label="Show Solution", command=sol)
file.add_command(label="Quit", command=exit)
menubar.add_cascade(label="Menu", menu=file)
root.config(menu=menubar)

root.mainloop()
