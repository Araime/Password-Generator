import os
import random
import sys
from tkinter import ttk
from tkinter import messagebox

from ttkthemes import ThemedTk

WORK_PATH = getattr(sys, "_MEIPASS", os.path.abspath(os.path.dirname(__file__)))


def generate_password(letters_qty, digits_qty, symbols_qty):
    letters = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
        'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F',
        'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
        'W', 'X', 'Y', 'Z'
    ]
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = [
        '!', '#', '$', '%', '&', '(', ')', '*', '+', '-', '_', '=', '@', '^', ';', ':',
        ',', '.', '/', '?', '\\', '|', '`', '~', '[', ']', '{', '}'
    ]
    random_password = ''
    password_list = []

    for char in range(1, letters_qty + 1):
        password_list.append(random.choice(letters))

    for char in range(1, digits_qty + 1):
        password_list.append(random.choice(numbers))

    for char in range(1, symbols_qty + 1):
        password_list.append(random.choice(symbols))

    random.shuffle(password_list)

    for char in password_list:
        random_password += char
    return random_password


def get_password():
    try:
        letters_qty = int(top_entry.get())
    except ValueError:
        password_txt['background'] = '#FF5733'
        password_txt['text'] = 'Incorrect input.'
    try:
        digits_qty = int(middle_entry.get())
    except ValueError:
        password_txt['background'] = '#FF5733'
        password_txt['text'] = 'Incorrect input.'
    try:
        symbols_qty = int(bottom_entry.get())
    except ValueError:
        password_txt['background'] = '#FF5733'
        password_txt['text'] = 'Incorrect input.'

    if type(letters_qty) == int and type(digits_qty) == int and type(symbols_qty) == int:
        password = generate_password(letters_qty, digits_qty, symbols_qty)
        password_txt['background'] = '#00FA9A'
        password_txt['text'] = password


def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(password_txt.cget('text'))
    password_txt['background'] = '#FFFF00'
    password_txt['text'] = 'Password copied.'


def on_closing():
    if messagebox.askokcancel("Exit", "Exit the program?"):
        root.destroy()


if __name__ == '__main__':
    root = ThemedTk(theme='radiance', themebg=True)
    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.title('Password Generator')
    root.geometry('350x210+550+300')
    root.resizable(False, False)
    root.iconbitmap(os.path.join(WORK_PATH, 'key.ico'))

    top_label = ttk.Label(root, text='How many letters?', font='Arial 12 bold')
    top_label.place(x=100, y=10, width=150, height=25, anchor='n')

    top_entry = ttk.Entry(root, font='Arial 12 bold')
    top_entry.place(x=300, y=10, width=50, height=25, anchor='n')

    middle_label = ttk.Label(root, text='How many digits?', font='Arial 12 bold')
    middle_label.place(x=100, y=50, width=150, height=25, anchor='n')

    middle_entry = ttk.Entry(root, font='Arial 12 bold')
    middle_entry.place(x=300, y=50, width=50, height=25, anchor='n')

    bottom_label = ttk.Label(root, text='How many symbols?', font='Arial 12 bold')
    bottom_label.place(x=110, y=90, width=170, height=25, anchor='n')

    bottom_entry = ttk.Entry(root, font='Arial 12 bold')
    bottom_entry.place(x=300, y=90, width=50, height=25, anchor='n')

    password_label = ttk.Label(root, text='Your password', font='Arial 12 bold')
    password_label.place(x=100, y=130, width=150, height=25, anchor='n')

    password_txt = ttk.Label(root, font='Arial 10 bold', background='#AFEEEE', anchor='e')
    password_txt.place(x=235, y=130, width=180, height=25, anchor='n')

    generate_button = ttk.Button(root, text='Generate', command=get_password, padding=(0, -3))
    generate_button.place(x=80, y=170, width=100, height=30, anchor='n')

    copy_button = ttk.Button(root, text='Copy to clipboard', command=copy_to_clipboard, padding=(0, -3))
    copy_button.place(x=250, y=170, width=160, height=30, anchor='n')

    root.mainloop()
