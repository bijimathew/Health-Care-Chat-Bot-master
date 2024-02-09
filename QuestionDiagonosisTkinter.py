from tkinter import *
from tkinter import messagebox

class HealthCareBot:
    def __init__(self, master):
        self.master = master
        master.title("Health Care Bot")
        master.geometry("900x500")

        self.symptoms = [
            "Running Nose",
            "Cough",
            "Fever",
            "Headache",
            "Fatigue",
            "Shortness of Breath",
            "Chest Pain",
            "Sore Throat",
            "Muscle or Body Aches",
            "Nausea",
            "Vomiting",
            "Diarrhea",
            "Joint Pain",
            "Skin Rash",
            "Abdominal Pain"
        ]

        self.current_question = 0
        self.yes_responses = 0  # Track the number of "Yes" responses

        self.label = Label(master, text="Health Care Bot", bg="crimson", width="300", height="2", font=("cambria", 16))
        self.label.pack()

        self.label_question = Label(master, text=self.symptoms[self.current_question], font=("cambria", 14))
        self.label_question.pack(pady=(50, 10))

        self.btn_yes = Button(master, text="Yes", command=self.answer_yes, width=20, height=2, bg="green", fg="white", font=("cambria", 12))
        self.btn_yes.pack(side=LEFT, padx=20, pady=(100, 0))

        self.btn_no = Button(master, text="No", command=self.answer_no, width=20, height=2, bg="red", fg="white", font=("cambria", 12))
        self.btn_no.pack(side=RIGHT, padx=20, pady=(100, 0))

    def answer_yes(self):
        self.yes_responses += 1
        if self.yes_responses >= 4:
            self.show_prediction()
        else:
            self.show_next_question()

    def answer_no(self):
        self.show_next_question()

    def show_next_question(self):
        self.current_question += 1

        if self.current_question < len(self.symptoms):
            self.label_question.config(text=self.symptoms[self.current_question])
        else:
            messagebox.showinfo("Prediction", "Not enough information for prediction. Consult with a doctor.")

    def show_prediction(self):
        prediction_message = "Based on your symptoms, you may have the common cold. " \
                             "However, this is just a prediction. Consult with a doctor for accurate diagnosis."
        messagebox.showinfo("Prediction", prediction_message)

if __name__ == "__main__":
    root = Tk()
    bot = HealthCareBot(root)
    root.mainloop()
