from tkinter import *
import os
import subprocess

# Designing window for registration
def destroyPackWidget(parent):
    for e in parent.pack_slaves():
        e.destroy()

def register():
    global root, register_screen
    destroyPackWidget(root)
    register_screen = root
    register_screen.title("Register")
    register_screen.geometry("1122x668")

    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()

    Label(register_screen, text="Please enter the details below", bg="crimson", width="300", height="2", font=("cambria", 16)).pack()
    Label(register_screen, text="").pack()
    Label(register_screen, text="").pack()
    username_lable = Label(register_screen, text="Username * ", font=("cambria", 12))
    username_lable.pack()
    username_entry = Entry(register_screen, textvariable=username, width="40")
    username_entry.pack()
    password_lable = Label(register_screen, text="Password * ", font=("cambria", 12))
    password_lable.pack()
    password_entry = Entry(register_screen, textvariable=password, show='*', width="40")
    password_entry.pack()
    Label(register_screen, text="").pack()
    Button(register_screen, text="Register", width=30, height=2, bg="silver", border=2, command=register_user).pack()

# Designing window for login
def login(main_screen):
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("1122x668")
    Label(login_screen, text="Please enter details below to login",bg="crimson", width="300", height="2", font=("cambria", 16)).pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="").pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_login_entry
    global password_login_entry

    Label(login_screen, text="Username * ", font=("cambria", 12)).pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify, width="40")
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ", font=("cambria", 12)).pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show='*',width="40")
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=30, height=2,bg="silver", command=lambda: login_verify(main_screen)).pack()

# Implementing event on register button
def btnSucess_Click():
    global root
    destroyPackWidget(root)
    open_question_diagnosis()

def open_question_diagnosis():
    # Open QuestionDiagonosisTkinter.py using subprocess
    subprocess.Popen(['python', 'QuestionDiagonosisTkinter.py'])

def register_user():
    global root, username, password
    username_info = username.get()
    password_info = password.get()
    print("abc", username_info, password_info, "xyz")
    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()

    username_entry.delete(0, END)
    password_entry.delete(0, END)

    Label(root, text="Registration Success", fg="green", font=("calibri", 11)).pack()
    Button(root, text="Click Here to proceed", command=btnSucess_Click).pack()

# Implementing event on login button
def login_verify(main_screen):
    global username_verify, password_verify
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)

    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_sucess()

        else:
            password_not_recognised()

    else:
        user_not_found()

# Designing popup for login success
def login_sucess():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("150x100")
    Label(login_success_screen, text="Login Success").pack()
    Button(login_success_screen, text="OK", command=lambda: [delete_login_success(), open_question_diagnosis()]).pack()

    # Open QuestionDiagonosisTkinter.py after successful login
    subprocess.Popen(["python", "F:/Health-Care-Chat-Bot-master/Health-Care-Chat-Bot-master/QuestionDiagonosisTkinter.py"])

    Button(login_success_screen, text="OK", command=delete_login_success).pack()

# Designing popup for login invalid password
def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()

# Designing popup for user not found
def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()

# Deleting popups
def delete_login_success():
    login_success_screen.destroy()

def delete_password_not_recognised():
    password_not_recog_screen.destroy()

def delete_user_not_found_screen():
    user_not_found_screen.destroy()

# Designing Main(first) window
def main_account_screen(frmmain):
    global root, username, password, username_entry, password_entry

    root = frmmain
    root.geometry("1122x668")
    root.title("Account Login")
    Label(root, text="Welcome to Healthcare bot", bg="crimson", width="300", height="2", font=("cambria", 16)).pack()

    Label(root, text="Select your choice", bg="silver", width="400", height="3", font=("cambria", 13)).pack()
    Label(root, text="").pack()
    Label(root, text="").pack()
    Label(root, text="").pack()
    Button(root, text="Login", height="2", width="30", font=("arial", 14), command=lambda: login(root)).pack()
    Label(root, text="").pack()
    Button(root, text="Register", height="2", width="30", font=("arial", 14), command=register).pack()
    Label(root, text="").pack()
    Label(root, text="").pack()
    Label(root, text="").pack()
    Label(root, text="").pack()
    Label(root, text="").pack()
    Label(root, text="").pack()
    Label(root, text="").pack()
    Label(root, text="").pack()
    Label(root, text="submit by:").pack()
    Label(root, text="").pack()

   
    Label(root, text="Biji Mathew - B40521015").pack()

    Label(root, text="").pack()

if __name__ == "__main__":
    root = Tk()
    main_account_screen(root)
    root.mainloop()
