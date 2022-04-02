import tkinter
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    print("password generate")

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    print("save password")
# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Password Generator")
window.config(padx=20, pady=20)

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
input_website1_1 = tkinter.Entry(width=35)
input_website1_1.grid(column=1, row=1, columnspan=2)

input_email1_2 = tkinter.Entry(width=35)
input_email1_2.grid(column=1, row=2, columnspan=2)

input_password1_3 = tkinter.Entry(width=18 )
input_password1_3.grid(column=1, row=3)

#Button

generate_button = tkinter.Button(text="Generate Password", width=14,font=("Arial", 8), command=generate_password)
generate_button.grid(column=2, row=3)

add_button = tkinter.Button(text="Add", width=35, font=("Arial", 8),  command=save_password)
add_button.grid(column=1, row=4, columnspan=2, )

window.mainloop()