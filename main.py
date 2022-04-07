import datetime
import tkinter
from tkinter import END
from tkinter import messagebox as mb
from _datetime import date
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    print("password generate")
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_symbols + password_letters + password_numbers

    random.shuffle(password_list)

    # password = ""
    # for char in password_list:
    #     password += char

    password = "".join(password_list)

    print(f"Your password is: {password}")
    input_password1_3.delete(0, END)
    input_password1_3.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():

    now_date = datetime.datetime.now()
    print(f"save password on {now_date}")
    print(type(now_date))
    website = input_website1_1.get()
    email = input_email1_2.get()
    password = input_password1_3.get()

    #mb.showinfo(title="Title", message="Message")
    if len(website) == 0 or len(password) == 0:
        mb.showerror(title="Что-то не так", message=f"all fields must be filled")
    else:
        is_ok = mb.askokcancel(title=website, message=f"These are details entered: \n"
                                                             f"Email: {input_email1_2.get()} \n"
                                                             f"Password: {password}")
        if is_ok:
            with open('datatext.txt', 'a') as f:
                f.write(f"{input_website1_1.get()},  {input_email1_2.get()}, {input_password1_3.get()}, {now_date},  \n")
            input_website1_1.delete(0, END)
            input_password1_3.delete(0, END)
            input_website1_1.focus()

# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=30, pady=30)

canvas = tkinter.Canvas(width=200, height=200)
picture = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=picture)
canvas.grid(column=1, row=0)
#Label
label0_1 = tkinter.Label(text="Website:", font=("Arial", 12))
label0_1.grid(column=0, row=1)
label0_2 = tkinter.Label(text="Email/Username:", font=("Arial", 12))
label0_2.grid(column=0, row=2)
label0_3 = tkinter.Label(text="Password:", font=("Arial", 12))
label0_3.grid(column=0, row=3)

#entry
input_website1_1 = tkinter.Entry(width=40)
input_website1_1.grid(column=1, row=1, columnspan=2)
input_website1_1.focus()

input_email1_2 = tkinter.Entry(width=40)
input_email1_2.grid(column=1, row=2, columnspan=2)
input_email1_2.insert(0, "demontage09@gmail.com")

input_password1_3 = tkinter.Entry(width=25 )
input_password1_3.grid(column=1, row=3)

#Button

generate_button = tkinter.Button(text="Generate Password", width=14,font=("Arial", 8), highlightthickness=0, command=generate_password)
generate_button.grid(column=2, row=3)

add_button = tkinter.Button(text="Add", width=40, font=("Arial", 8),  command=save_password)
add_button.grid(column=1, row=4, columnspan=2, )

window.mainloop()