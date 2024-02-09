# main_execution.py

import subprocess
from tkinter import Tk, Button, Label

class MainExecution:
    def __init__(self, master):
        self.master = master
        master.title("Health Care Bot Launcher")
        master.geometry("550x310")

        self.label = Label(master, text="Welcome to Health Care Bot Launcher", font=("cambria", 16))
        self.label.pack(pady=20)

        self.btn_launch = Button(master, text="Launch Health Care Bot", command=self.launch_health_care_bot, width=30, height=2, bg="silver", font=("cambria", 12))
        self.btn_launch.pack(pady=20)

    def launch_health_care_bot(self):
        # Execute
        subprocess.run(['python', 'newlogin.py'])
        
        subprocess.run(['python', 'QuestionDiagonosisTkinter.py'])
        

if __name__ == "__main__":
    root = Tk()
    app = MainExecution(root)
    root.mainloop()
