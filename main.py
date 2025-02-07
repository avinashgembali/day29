from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    password_list = [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]

    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    # copy to clipboard we use pyper clip 
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    web = website_entry.get()
    ema = email_entry.get()
    pas = password_entry.get()
    if len(web) == 0 or len(pas) == 0:
        messagebox.showinfo(title="oops", message="please dont leave any field to be empty")
    else:
        is_ok = messagebox.askokcancel(title=web, message=f"These are the details entered \nemail:{ema} "
                                                          f"\npassword:{pas} Is it ok to save?")
        if is_ok:
            with open("data.txt", mode="a") as file:
                file.write(f"{web} | {ema} | {pas}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("password manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image)
canvas.grid(column=1, row=0)

website_label = Label(text="website:")
website_label.grid(column=0, row=1)
email_label = Label(text="email/username:")
email_label.grid(column=0, row=2)
password_label = Label(text="password:")
password_label.grid(column=0, row=3)

website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "avinashgembali05@gmail.com")

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)


generate_button = Button(text="generate password", width=14, command=generate_password)
generate_button.grid(column=2, row=3)

add_button = Button(text="add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)
window.mainloop()
