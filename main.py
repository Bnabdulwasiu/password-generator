from tkinter import *
from random import randint, choice, shuffle
from tkinter import messagebox
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate(): 
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
            
    password_letters = [choice(letters) for letter in range(randint(8 , 10))]
    password_numbers = [choice(numbers) for num in range(randint(2, 4))]
    password_symbols = [choice(symbols) for symbol in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols
    #Randomizing the list new_password
    shuffle(password_list)
    password = "".join(password_list)
    password_entry.delete(0, END)  
    password_entry.insert(0, password)
    pyperclip.copy(password)
    
# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    
    website = website_entry.get()
    email = email_name_entry.get()
    password = password_entry.get()
    
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }
    
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Do not leave any fields empty")
        
    else:        
        #The code in the line below is saved in a variable bcos it returns a TRUE of FALSE value
        # is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email}"
        #                     f"\nPassword: {password_entry.get()}\nIs it ok to save?")
        
        try:
            with open('data.json', 'r') as data_file:
                #Reading old data
                data = json.load(data_file)

                
        except FileNotFoundError:
            with open('data.json', 'w') as data_file:
                json.dump(new_data, data_file, indent=4)
        
        else:   
            #Updating old data with a new data
            data.update(new_data)
            with open('data.json', 'w') as data_file:
            #Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
        #To delete the string from beginning to the end
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            website_entry.focus()                 
# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = website_entry.get()
    try: 
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Key Error", message="No data found")
    else:
        if website in data:
            messagebox.showinfo(title=website, message=f"Email: {data[website]['email']}\nPassword: {data[website]['password']}")
            
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists")            
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
website_entry = Entry(width=25)
website_entry.grid(row=1, column=1)
#Focusing the cursor on an entry
website_entry.focus()

email_name_label = Label(text='Email/Username:')
email_name_label.grid(row=2, column=0)
email_name_entry = Entry(width=45)
email_name_entry.grid(row=2, column=1, columnspan=2)
#Prepopulating the entry space
email_name_entry.insert(0, "bnabdulwasiu111@gmail.com")

password_label = Label(text="Password: ")
password_label.grid(row=3, column=0)
password_entry = Entry(width=25)
password_entry.grid(row=3, column=1)


#Buttons
generate_button = Button(text="Generate Password", command=generate)
generate_button.grid(row=3, column=2)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

search_button = Button(text="Search", width=15, command=find_password)
search_button.grid(row=1, column=2)



window.mainloop()