from tkinter import *
from tkinter import messagebox
import random

import json


# SEARCH

def search():
    website_check = website_input.get()
    email_check = email_input.get()
    with open("database.json", "r") as data_file:
        data = json.load(data_file)
        try:
            if email_check != data[website_check]['Email']:
                email_input.insert(0, data[website_check]['Email'])
        except KeyError:
            messagebox.showinfo(title="ALERT", message="You have provided wrong website name")
            website_input.focus_set()
        else:
            if email_check != data[website_check]['Email']:
                email_input.delete(0, END)
                email_input.insert(0, data[website_check]['Email'])
            password_input.delete(0, END)
            password_input.insert(0, data[website_check]['Password'])


# PASSWORD GENERATE

def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(4, 9)
    nr_symbols = random.randint(2, 5)
    nr_numbers = random.randint(2, 5)

    letters_part = []
    upper_bound_letters = len(letters) - 1
    for letter in range(0, nr_letters):
        letters_part.append(letters[random.randint(0, upper_bound_letters)])

    numbers_part = []
    upper_bound_numbers = len(numbers) - 1
    for number in range(0, nr_numbers):
        numbers_part.append(numbers[random.randint(0, upper_bound_numbers)])

    symbols_part = []
    upper_bound_symbols = len(symbols) - 1
    for symbol in range(0, nr_symbols):
        symbols_part.append(symbols[random.randint(0, upper_bound_symbols)])

    password_unordered = letters_part + symbols_part + numbers_part
    random.shuffle(password_unordered)

    password = ""
    for character in range(0, len(password_unordered)):
        password += password_unordered[character]

    password_input.insert(0, password)
    pyperclip.copy(password)


# PASSWORD_SAVE

def save():
    website_get = website_input.get()
    username_get = email_input.get()
    password_get = password_input.get()

    new_data = {
        website_get: {
            "Email": username_get,
            "Password": password_get,
        }
    }

    if password_get == "" or website_get == "":
        messagebox.showinfo(title="Alert", message="You cannot leave password or website empty")

    else:
        try:
            with open("database.json", "r") as data_file:
                data = json.load(data_file)

        except FileNotFoundError:
            with open("database.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)

            with open("database.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_input.delete(0, len(website_get))
            password_input.delete(0, len(password_get))

        label_result.config(text=f"Your password for {website_get} has been saved", fg="red")

    website_input.focus()


# GUI

window = Tk()

window.config(padx=50, pady=75)

window.title("Password Manager")

canvas = Canvas(width=200, height=200, highlightthickness=0)
Logo_image = PhotoImage(file="znak_graficzny_agh_w_pozytywowa.png")
canvas.create_image(100, 80, image=Logo_image)
canvas.grid(column=1, row=0)

label_website = Label(text="Website: ")
label_website.grid(column=0, row=1)

website = website_input = Entry(width=21)
website_input.grid(column=1, row=1)
website_input.focus()

email_label = Label(text="Email/Username: ")
email_label.grid(column=0, row=2)

email_input = Entry(width=35)
email = Entry.get(email_input)
email_input.grid(column=1, row=2, columnspan=2)
email_input.insert(0, "denis.poloczek@icloud.com")

password_label = Label(text="Password: ")
password_label.grid(column=0, row=3)

password_input = Entry(width=21)
password_input.grid(column=1, row=3)

generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

search_button = Button(text="Search", command=search, width=13, highlightthickness=2)
search_button.grid(column=2, row=1)

label_result = Label()
label_result.grid(row=6, column=1, columnspan=2)

window.mainloop()
