import tkinter as tk
from tkinter import messagebox
from quiz_app import DataAnalysisQuiz

class QuizGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Data Analysis Quiz")
        self.root.geometry("600x500")
        self.root.configure(bg="#f0f0f0")

        self.quiz = DataAnalysisQuiz()
        self.current_question_idx = 0
        self.score = 0
        
        self.setup_ui()
        self.load_question()

    def setup_ui(self):
        # Header
        self.header_label = tk.Label(
            self.root, text="🚀 Data Analysis Quiz", 
            font=("Helvetica", 18, "bold"), bg="#2c3e50", fg="white", pady=10
        )
        self.header_label.pack(fill=tk.X)

        # Info Label (Question # and Level)
        self.info_label = tk.Label(
            self.root, text="", font=("Helvetica", 10), bg="#f0f0f0", fg="#7f8c8d", pady=5
        )
        self.info_label.pack()

        # Question Text
        self.question_label = tk.Label(
            self.root, text="", font=("Helvetica", 12, "bold"), 
            wraplength=550, bg="#f0f0f0", justify="center", pady=20
        )
        self.question_label.pack()

        # Options (Radio Buttons)
        self.radio_var = tk.StringVar(value="None")
        self.option_buttons = []
        for i in range(4):
            rb = tk.Radiobutton(
                self.root, text="", variable=self.radio_var, value="",
                font=("Helvetica", 11), bg="#f0f0f0", activebackground="#f0f0f0",
                padx=20, pady=5, anchor="w"
            )
            rb.pack(fill=tk.X, padx=50)
            self.option_buttons.append(rb)

        # Submit Button
        self.submit_button = tk.Button(
            self.root, text="Submit Answer", command=self.check_answer,
            font=("Helvetica", 12, "bold"), bg="#27ae60", fg="white", 
            padx=20, pady=10, relief="raised", cursor="hand2"
        )
        self.submit_button.pack(pady=30)

        # Score Footer
        self.score_label = tk.Label(
            self.root, text="Score: 0 / 10", font=("Helvetica", 10, "italic"), 
            bg="#f0f0f0", fg="#34495e"
        )
        self.score_label.pack(side=tk.BOTTOM, pady=10)

    def load_question(self):
        if self.current_question_idx < len(self.quiz.questions):
            q = self.quiz.questions[self.current_question_idx]
            self.info_label.config(
                text=f"Question {self.current_question_idx + 1} of {len(self.quiz.questions)} | "
                     f"Level {q['level']}: {self.quiz.levels_map[q['level']]}"
            )
            self.question_label.config(text=q["question"])
            
            options_labels = ['A', 'B', 'C', 'D']
            for i, opt in enumerate(q["options"]):
                self.option_buttons[i].config(text=f"{options_labels[i]}. {opt}", value=options_labels[i])
            
            self.radio_var.set("None")
        else:
            self.show_results()

    def check_answer(self):
        selected = self.radio_var.get()
        if selected == "None":
            messagebox.showwarning("Warning", "Please select an answer!")
            return

        correct_answer = self.quiz.questions[self.current_question_idx]["answer"]
        if selected == correct_answer:
            self.score += 1
            messagebox.showinfo("Result", "✅ Correct!")
        else:
            options = self.quiz.questions[self.current_question_idx]["options"]
            labels = ['A', 'B', 'C', 'D']
            correct_text = options[labels.index(correct_answer)]
            messagebox.showerror("Result", f"❌ Incorrect!\nThe correct answer was {correct_answer}: {correct_text}")

        self.current_question_idx += 1
        self.score_label.config(text=f"Score: {self.score} / {len(self.quiz.questions)}")
        self.load_question()

    def show_results(self):
        skill = self.quiz.categorize_skill(self.score)
        result_text = f"Quiz Finished!\n\nFinal Score: {self.score} / {len(self.quiz.questions)}\nSkill Level: {skill}"
        messagebox.showinfo("Final Results", result_text)
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizGUI(root)
    root.mainloop()
