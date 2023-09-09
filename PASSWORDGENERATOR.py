import random
import string
import tkinter as tk
from tkinter import messagebox, simpledialog, font

def generate_password(length):
    characters = string.ascii_letters +string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_passwords():
    try:
        num_passwords = int(simpledialog.askstring("Number of Passwords","Enter the number of passwords to generate:"))
        if num_passwords <= 0:
            messagebox.showerror("Error","Number of passwords must be a positive number.")
            return

        passwords = []
        for _ in range(num_passwords):
            password_length = int(simpledialog.askstring("Password Length",f"Enter desired password length for password {_ + 1}:"))
            if password_length <= 0:
                messagebox.showerror("Error","Password length must be a positive number.")
                return

            password =generate_password(password_length)
            passwords.append(f"Generated Password {_ + 1}: {password}")

        generated_passwords = "\n".join(passwords)
        messagebox.showinfo("Generated Passwords",generated_passwords)

    except ValueError:
        messagebox.showerror("Error","Invalid input. Please enter a valid number.")

def on_enter(event):
    event.widget.default_bg = event.widget["bg"]
    event.widget.config(bg="lightgray")

def on_leave(event):
    event.widget.config(bg=event.widget.default_bg)

def main():
    root = tk.Tk()
    root.title("Password Generator")
    
    custom_font =font.Font(family="Helvetica",size=15)

    generate_button = tk.Button(root, text="Generate Passwords",command=generate_passwords, font=custom_font, bg="green", fg="white")
    generate_button.pack(pady=20)
    generate_button.default_bg = generate_button["bg"]
    generate_button.bind("<Enter>", on_enter)
    generate_button.bind("<Leave>", on_leave)

    exit_button = tk.Button(root, text="Exit",command=root.quit, font=custom_font, bg="red", fg="white")
    exit_button.pack()
    exit_button.default_bg = exit_button["bg"]
    exit_button.bind("<Enter>", on_enter)
    exit_button.bind("<Leave>", on_leave)

    root.mainloop()

if __name__ == "__main__":
    main()
