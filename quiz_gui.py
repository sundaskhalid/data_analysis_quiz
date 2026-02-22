import tkinter as tk
from tkinter import messagebox
from quiz_app import DataAnalysisQuiz

class QuizGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Data Analysis Quiz")
        self.root.geometry("800x700") # Increased default height
        self.root.configure(bg="#121212") # Deeper dark background

        self.quiz = DataAnalysisQuiz()
        self.current_question_idx = 0
        self.score = 0
        
        # Color Palette (Enhanced High-Contrast Dark Theme)
        self.colors = {
            "bg": "#121212",         # Deep charcoal
            "surface": "#1e1e1e",    # Lighter charcoal for containers
            "primary": "#3498db",    # Bright blue
            "secondary": "#27ae60",  # Strong green
            "header": "#1a252f",     # Dark navy for header
            "text_main": "#ffffff",  # Pure white
            "text_dim": "#bdc3c7",   # Light silver
            "highlight": "#f39c12",  # Amber for emphasis
            "error": "#e74c3c",      # Red
            "submit_bg": "#1e1e1e",  # Dark button background
            "submit_fg": "#3498db"   # Colored button text
        }

        # Base font sizes
        self.base_header_size = 22
        self.base_info_size = 11
        self.base_question_size = 16
        self.base_option_size = 13
        self.base_button_size = 14
        self.base_score_size = 11

        self.setup_ui()
        self.load_question()
        
        # Bind resize event for dynamic font scaling
        self.root.bind("<Configure>", self.on_resize)

    def setup_ui(self):
        # Header (Now with a modern border)
        self.header_frame = tk.Frame(self.root, bg=self.colors["header"], pady=20)
        self.header_frame.pack(fill=tk.X)
        
        self.header_label = tk.Label(
            self.header_frame, text="🚀 PYTHON DATA ANALYSIS QUIZ", 
            font=("Helvetica", self.base_header_size, "bold"), 
            bg=self.colors["header"], fg=self.colors["text_main"]
        )
        self.header_label.pack()

        # Content Container (Centered with padding)
        self.content_frame = tk.Frame(self.root, bg=self.colors["bg"], pady=30)
        self.content_frame.pack(expand=True, fill=tk.BOTH, padx=50)

        # Info Label (Question # and Level)
        self.info_label = tk.Label(
            self.content_frame, text="", 
            font=("Helvetica", self.base_info_size), 
            bg=self.colors["bg"], fg=self.colors["primary"]
        )
        self.info_label.pack(pady=(0, 10))

        # Question Text
        self.question_label = tk.Label(
            self.content_frame, text="", 
            font=("Helvetica", self.base_question_size, "bold"), 
            wraplength=700, bg=self.colors["bg"], fg=self.colors["text_main"], 
            justify="center", pady=10
        )
        self.question_label.pack(pady=(10, 20))

        # Options Container
        self.options_frame = tk.Frame(self.content_frame, bg=self.colors["bg"])
        self.options_frame.pack(fill=tk.X, pady=20)

        self.radio_var = tk.StringVar(value="None")
        self.radio_var.trace_add("write", lambda *args: self.on_radio_change())
        self.option_buttons = []
        for i in range(4):
            # Using indicatoron=0 makes the entire button clickable
            rb = tk.Radiobutton(
                self.options_frame, text="", variable=self.radio_var, value="",
                font=("Helvetica", self.base_option_size), 
                bg=self.colors["surface"], fg=self.colors["text_dim"],
                activebackground=self.colors["primary"], 
                activeforeground=self.colors["text_main"],
                selectcolor=self.colors["primary"],
                padx=20, pady=15, anchor="w",
                indicatoron=0, 
                relief="flat", bd=0, highlightthickness=1,
                highlightbackground=self.colors["surface"],
                takefocus=True
            )
            rb.pack(fill=tk.X, pady=8) # Increased spacing
            rb.bind("<Enter>", lambda e, r=rb: self.on_hover(r))
            rb.bind("<Leave>", lambda e, r=rb: self.on_leave(r))
            # Fix responsiveness by binding click explicitly to variable change
            rb.bind("<Button-1>", lambda e, r=rb: self.on_click(r))
            self.option_buttons.append(rb)

        # Submit Button (Modern "Dark Form" style)
        self.submit_button = tk.Button(
            self.content_frame, text="SUBMIT ANSWER", command=self.check_answer,
            font=("Helvetica", self.base_button_size, "bold"), 
            bg="#2c3e50", fg=self.colors["primary"], 
            activebackground=self.colors["primary"], activeforeground=self.colors["text_main"],
            padx=60, pady=20, relief="flat", cursor="hand2",
            highlightthickness=2, highlightbackground=self.colors["primary"], 
            bd=0
        )
        self.submit_button.pack(pady=40)
        
        # Explicitly set background for macOS compatibility
        try:
            self.submit_button.config(highlightbackground=self.colors["primary"])
        except:
            pass

        # Score Footer
        self.score_label = tk.Label(
            self.root, text="Score: 0 / 10", 
            font=("Helvetica", self.base_score_size, "italic"), 
            bg=self.colors["bg"], fg=self.colors["text_dim"]
        )
        self.score_label.pack(side=tk.BOTTOM, pady=20)

    def on_click(self, rb):
        # Force the radio variable to update and update focus
        self.radio_var.set(rb.cget("value"))
        rb.focus_set()

    def on_hover(self, rb):
        # Change highlight if not selected
        if self.radio_var.get() != rb.cget("value"):
            rb.config(bg="#2c3e50", fg=self.colors["text_main"], highlightbackground=self.colors["primary"])

    def on_leave(self, rb):
        # Restore style if not selected
        if self.radio_var.get() != rb.cget("value"):
            rb.config(bg=self.colors["surface"], fg=self.colors["text_dim"], highlightbackground=self.colors["surface"])
        else:
            # Keep selected look
            rb.config(bg=self.colors["primary"], fg=self.colors["text_main"], highlightbackground=self.colors["primary"])

    def on_radio_change(self):
        # Update all buttons based on current selection
        selected = self.radio_var.get()
        if selected == "None":
            return
            
        for rb in self.option_buttons:
            if rb.cget("value") == selected:
                rb.config(bg=self.colors["primary"], fg=self.colors["text_main"], highlightbackground=self.colors["primary"])
            else:
                rb.config(bg=self.colors["surface"], fg=self.colors["text_dim"], highlightbackground=self.colors["surface"])

    def restore_rb_style(self, rb):
        # Deprecated: using on_leave and on_radio_change
        pass

    def on_resize(self, event):
        # Only handle top-level resize
        if event.widget != self.root:
            return
            
        new_width = self.root.winfo_width()
        new_height = self.root.winfo_height()
        
        # Scaling factor based on base 800x700
        scale = min(new_width / 800, new_height / 700)
        scale = max(0.8, min(scale, 1.8))
        
        self.update_font_sizes(scale)
        self.question_label.config(wraplength=int(new_width * 0.85))

    def update_font_sizes(self, scale):
        self.header_label.config(font=("Helvetica", int(self.base_header_size * scale), "bold"))
        self.info_label.config(font=("Helvetica", int(self.base_info_size * scale)))
        self.question_label.config(font=("Helvetica", int(self.base_question_size * scale), "bold"))
        for rb in self.option_buttons:
            rb.config(font=("Helvetica", int(self.base_option_size * scale)))
        self.submit_button.config(font=("Helvetica", int(self.base_button_size * scale), "bold"))
        self.score_label.config(font=("Helvetica", int(self.base_score_size * scale), "italic"))

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
        try:
            selected = self.radio_var.get()
            if selected == "None" or not selected:
                messagebox.showwarning("Warning", "Please select an answer first!")
                return

            current_q = self.quiz.questions[self.current_question_idx]
            correct_answer = current_q["answer"]
            
            if selected == correct_answer:
                self.score += 1
                messagebox.showinfo("Result", "✅ Correct!")
            else:
                options = current_q["options"]
                labels = ['A', 'B', 'C', 'D']
                correct_text = options[labels.index(correct_answer)]
                messagebox.showerror("Result", f"❌ Incorrect!\nThe correct answer was {correct_answer}: {correct_text}")

            self.current_question_idx += 1
            self.score_label.config(text=f"Score: {self.score} / {len(self.quiz.questions)}")
            self.load_question()
        except Exception as e:
            messagebox.showerror("Error", f"An unexpected error occurred: {e}")

    def show_results(self):
        skill = self.quiz.categorize_skill(self.score)
        result_text = f"Quiz Finished!\n\nFinal Score: {self.score} / {len(self.quiz.questions)}\nSkill Level: {skill}"
        messagebox.showinfo("Final Results", result_text)
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizGUI(root)
    root.mainloop()
