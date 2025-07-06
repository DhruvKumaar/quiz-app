import tkinter as tk
from tkinter import messagebox

questions = [
    {
        "question": "What is the capital of India?",
        "options": ["Kolkata", "New Delhi", "Madras", "Mumbai"],
        "correct": 1
    },
    {
        "question": "What is the largest planet in our solar system?",
        "options": ["Earth", "Saturn", "Jupiter", "Uranus"],
        "correct": 2
    },
    {
        "question": "Who painted the Mona Lisa?",
        "options": ["Leonardo da Vinci", "Michelangelo", "Raphael", "Caravaggio"],
        "correct": 0
    }
]

current_question = 0
score = 0
user_answers = [-1] * len(questions)

root = tk.Tk()
root.title("Quiz App")
root.geometry("500x400")
selected_option = tk.IntVar()

def load_question():
    question_label.config(text=f"Q{current_question + 1}: {questions[current_question]['question']}")
    selected_option.set(user_answers[current_question])
    for i, opt in enumerate(questions[current_question]['options']):
        options[i].config(text=opt, value=i)

def next_question():
    global current_question
    selected = selected_option.get()
    if selected == -1:
        messagebox.showwarning("No Selection", "Please select an option before continuing.")
        return

    user_answers[current_question] = selected
    current_question += 1

    if current_question >= len(questions):
        show_results()
    else:
        load_question()

def prev_question():
    global current_question
    if current_question > 0:
        selected = selected_option.get()
        user_answers[current_question] = selected
        current_question -= 1
        load_question()

def show_results():
    global score
    result_text = ""
    score = 0

    for i, ans in enumerate(user_answers):
        correct = questions[i]["correct"]
        if ans == correct:
            result_text += f"Q{i+1}: ✅ Correct\n"
            score += 1
        else:
            correct_answer = questions[i]["options"][correct]
            your_answer = "Not answered" if ans == -1 else questions[i]["options"][ans]
            result_text += f"Q{i+1}: ❌ Wrong (Your answer: {your_answer}, Correct: {correct_answer})\n"

    result_text += f"\nFinal Score: {score}/{len(questions)}"
    messagebox.showinfo("Quiz Results", result_text)
    root.quit()

question_label = tk.Label(root, text="", font=("Arial", 16), wraplength=450, justify="left")
question_label.pack(pady=20)

options = []
for i in range(4):
    rb = tk.Radiobutton(root, text="", variable=selected_option, value=i, font=("Arial", 12), anchor="w")
    rb.pack(fill="x", padx=30, pady=5)
    options.append(rb)

nav_frame = tk.Frame(root)
nav_frame.pack(pady=20)

prev_btn = tk.Button(nav_frame, text="Previous", command=prev_question, bg="#4CAF50", fg="white", padx=20)
prev_btn.grid(row=0, column=0, padx=10)

next_btn = tk.Button(nav_frame, text="Next", command=next_question, bg="#4CAF50", fg="white", padx=20)
next_btn.grid(row=0, column=1, padx=10)

load_question()
root.mainloop()