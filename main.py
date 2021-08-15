from tkinter import *
from tkinter import messagebox
from password_generator import password_maker


background_color = "#FDF6F0"
FONT_NAME = "Courier"
RED= "#E40017"
BLACK = "#000000"
FONT = (FONT_NAME, 10, "bold")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def passport_generator():
    password = password_maker()
    password_entry.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_inputs():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showwarning(title="Warning", message="Every entry should be filled")
    else:
        message = messagebox.askquestion(title="Entry Information", message="These are details entered:"
                                                                            f"\nWebsite: {website}"
                                                                            f"\nEmail: {email}"
                                                                            f"\nPassword: {password}"
                                                                            "\nAre you sure?")
        if message.lower() == "yes":
            with open("data.txt","a") as file:
                file.write(f"{website.lower()},{email},{password}\n")
                website_entry.delete(0, 'end')
                email_entry.delete(0, 'end')
                password_entry.delete(0, 'end')
                messagebox.showinfo("Result", "New Password has been added successfully")

# ---------------------------- BRING PASSWORD ------------------------------- #
def bring_passport():
    password_entry.delete(0, 'end')
    website = website_entry.get()
    email = email_entry.get()
    with open("data.txt") as file:
        content = file.readlines()
        for item in content:
            if (website.lower() in item) and len(email)== 0 :
                lst = item.split(",")
                passport = lst[-1]
                password_entry.insert(0, passport)
            elif (email.lower() in item) and len(website) == 0:
                lst = item.split(",")
                passport = lst[-1]
                password_entry.insert(0, passport)
            elif (website.lower() in item) and (email.lower() in item):
                lst = item.split(",")
                passport = lst[-1]
                password_entry.insert(0, passport)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(bg=background_color, padx=30, pady=30)
window.geometry("500x600")
window.resizable(0, 0)

canvas = Canvas(width=250, height=250, bg=background_color, highlightthickness=0)
lock_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_image)
#canvas.create_text(100, 7, text="Password Manager", fill=BLACK, font=(FONT_NAME, 14, "bold"))
canvas.place(x=130, y=10)

website_label = Label(text="Website:", fg="#000000",  bg=background_color)
website_label.place(x=0, y=270)
website_entry = Entry(width=43)
website_entry.focus()
website_entry.place(x=100, y=270)

email_username = Label(text="Email/Username:", fg="#000000",  bg=background_color)
email_username.place(x=0, y=310)
email_entry = Entry(width=43)
#email_entry.insert(0,"email@gmail.com") we can use a starting defalut value
email_entry.place(x=100, y=310)

password = Label(text="Password:", fg="#000000",  bg=background_color)
password.place(x=0, y=350)
password_entry = Entry(width=23)
password_entry.place(x=100, y=350)
password_button = Button(text="Generate Password", bg=background_color, command= passport_generator)
password_button.place(x=250, y=345)

add_button = Button(text="Add Password", bg=background_color, width=16, command=save_inputs)
add_button.place(x=100, y=390)

bring_button = Button(text="Bring Password", bg=background_color, width=16, command=bring_passport)
bring_button.place(x=240, y=390)


window.mainloop()