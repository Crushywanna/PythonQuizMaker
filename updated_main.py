
# Importing
import tkinter as tk
from tkinter.messagebox import askokcancel, showinfo, showerror, showwarning
from subprocess import call
import os
import datetime as dt
# import time
import csv
# import urllib.request
from tkinter.scrolledtext import ScrolledText
from tkinter.filedialog import askdirectory, askopenfile, asksaveasfile

logs_lq = []
csv_things = []

# Function to install a package

logs = []
answers_prov = []
marks_obt = []

def next_q(q_id):
    if types[q_id] == 'mcq':
        try:
            if options[q_id].split(';')[opts_var.get()-1] in answers[q_id].split(';'):
                if answers[q_id] == '':
                    answers_prov.append(options[q_id].split(';')[opts_var.get()-1])
                    showwarning('Alert', 'You did not enter an answer.')
                    logs.append('Manual')
                    marks_obt.append('?')
                elif options[q_id].split(';')[opts_var.get()-1] != '' and opts_var.get()-1 > -1:
                    answers_prov.append(options[q_id].split(';')[opts_var.get()-1])
                    showinfo('Correct!', 'Your answer is correct!')
                    logs.append('Auto: Correct')
                    marks_obt.append(marks[q_id])
                else:
                    answers_prov.append('')
                    showerror('Sorry!', 'You did not provide any info!')
                    logs.append('Auto: Wrong')
                    marks_obt.append('0')
            else:
                answers_prov.append(options[q_id].split(';')[opts_var.get()-1])
                showerror('Sorry!', 'Your answer is incorrect!')
                logs.append('Auto: Wrong')
                marks_obt.append('0')
        except:
            answers_prov.append(options[q_id].split(';')[opts_var.get()-1])
            showerror('Sorry!', 'Your answer is incorrect!')
            logs.append('Auto: Wrong')
            marks_obt.append('0')
    else:
        try:
            if ans_var.get() in answers[q_id].split(';'):
                if answers[q_id] == '':
                    answers_prov.append(ans_var.get())
                    showwarning('Alert', 'You did not enter an answer.')
                    logs.append('Manual')
                    marks_obt.append('?')
                elif ans_var.get() != '':
                    answers_prov.append(ans_var.get())
                    showinfo('Correct!', 'Your answer is correct!')
                    logs.append('Auto: Correct')
                    marks_obt.append(marks[q_id])
                else:
                    answers_prov.append('')
                    showerror('Sorry!', 'You did not provide any info!')
                    logs.append('Auto: Wrong')
                    marks_obt.append('0')
            else:
                answers_prov.append(ans_var.get())
                showerror('Sorry!', 'Your answer is incorrect!')
                logs.append('Auto: Wrong')
                marks_obt.append('0')
        except:
            answers_prov.append(ans_var.get())
            showerror('Sorry!', 'Your answer is incorrect!')
            logs.append('Auto: Wrong')
            marks_obt.append('0')
            
    if q_id + 1 < len(questions):
        make_quiz(q_id + 1)
    else:
        end()

def make_quiz(q_id):
    global opts_var, ans_var
    quiz_window = tk.Tk()
    quiz_window.title("Quiz")

    question_label = tk.Label(quiz_window, text=questions[q_id])
    question_label.pack()

    if types[q_id] == 'mcq':
        opts_var = tk.IntVar()
        for i, option in enumerate(options[q_id].split(';')):
            tk.Radiobutton(quiz_window, text=option, variable.opts_var, value=i+1).pack(anchor='w')
    else:
        ans_var = tk.StringVar()
        tk.Entry(quiz_window, textvariable=ans_var).pack()

    next_button = tk.Button(quiz_window, text="Next", command=lambda: next_q(q_id))
    next_button.pack()

    quiz_window.mainloop()

def end():
    print("Question, Provided Answer, Correct Answer, Marks Obtained")
    for x in range(len(questions)):
        print(f"{questions[x]}, {answers_prov[x]}, {answers[x]}, {marks_obt[x]}")
    
    print("Detailed Logs:")
    for b in logs_lq:
        print(b)

# Class to organise the introductory code
def init_array(subject):
    welcome_window.destroy()
    table = list(csv.reader(open(subject)))
    global types
    global questions
    global options
    global answers
    global marks
    types = []
    questions = []
    options = []
    answers = []
    marks = []
    for x in range(len(table)):
        types.append(table[x][0])
        questions.append(table[x][1])
        options.append(table[x][2])
        answers.append(table[x][3])
        marks.append(table[x][4])
    make_quiz(0)

class Intro:
    def cont(self):
        pass
    def open_quiz_csv(self):
        file_loc = askopenfile(title="Select Quiz File", filetypes=(("Comma Separated Values","*.csv"),))
        init_array(file_loc.name)
    def ask_name(self):
        global welcome_window
        welcome_window = tk.Tk()
        welcome_window.title("Choose a Subject")

        welcome_msg = tk.Label(welcome_window, text="Welcome To PyQuiz! Which Quiz Do You Want To Continue With?").grid(row=0, columnspan=4)

        py_but = tk.Button(welcome_window, command=lambda: init_array('Python.csv'), text="Python").grid(row=1, column=0)
        code_but = tk.Button(welcome_window, command=lambda: init_array('Coding.csv'), text="Coding").grid(row=1, column=1)
        gk_button = tk.Button(welcome_window, command=lambda: init_array('GK.csv'), text="General Knowledge").grid(row=1, column=2)
        CGRC_button = tk.Button(welcome_window, command=lambda: init_array('CGRC.csv'), text="CGRC").grid(row=1, column=3)
        file_button = tk.Button(welcome_window, command=self.open_quiz_csv, text="External Quiz").grid(row=1, column=4)

        welcome_window.mainloop()

intro_handle = Intro()

intro_handle.ask_name()
