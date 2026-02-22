import pandas as pd
import numpy as np

class DataAnalysisQuiz:
    def __init__(self):
        self.levels_map = {
            1: "Novice",
            2: "Intermediate",
            3: "Advanced",
            4: "Expert",
            5: "Master"
        }
        self.questions = [
            # Level 1: Beginner (Basic operations)
            {
                "level": 1,
                "question": "Which Pandas function is used to read data from a CSV file?",
                "options": ["read_csv()", "load_csv()", "open_csv()", "get_csv()"],
                "answer": "A"
            },
            {
                "level": 1,
                "question": "How do you select the first 5 rows of a DataFrame 'df'?",
                "options": ["df.first(5)", "df.top(5)", "df.head(5)", "df.peek(5)"],
                "answer": "C"
            },
            # Level 2: Intermediate (Selection & Filtering)
            {
                "level": 2,
                "question": "Which method is used to filter rows based on a condition (e.g., df['age'] > 30)?",
                "options": ["df.filter()", "df.query()", "Boolean indexing (df[df['age'] > 30])", "Both B and C"],
                "answer": "D"
            },
            {
                "level": 2,
                "question": "How do you select a single column named 'Salary' from a DataFrame 'df'?",
                "options": ["df['Salary']", "df.Salary", "df.get('Salary')", "All of the above"],
                "answer": "D"
            },
            # Level 3: Advanced (Manipulation & Cleaning)
            {
                "level": 3,
                "question": "Which Pandas method is used to handle missing values by filling them with a specific value?",
                "options": ["dropna()", "fillna()", "replace_na()", "fixna()"],
                "answer": "B"
            },
            {
                "level": 3,
                "question": "How do you rename a column 'Old' to 'New' in a DataFrame 'df'?",
                "options": ["df.rename(columns={'Old': 'New'})", "df.set_name('Old', 'New')", "df.columns['Old'] = 'New'", "df.change_column('Old', 'New')"],
                "answer": "A"
            },
            # Level 4: Expert (Aggregation & Joins)
            {
                "level": 4,
                "question": "Which function is used to group data by one or more columns and calculate an aggregate?",
                "options": ["pivot()", "melt()", "groupby()", "stack()"],
                "answer": "C"
            },
            {
                "level": 4,
                "question": "Which join type in merge() returns only the rows with matching keys in both DataFrames?",
                "options": ["left", "right", "outer", "inner"],
                "answer": "D"
            },
            # Level 5: Master (Reshaping & Optimization)
            {
                "level": 5,
                "question": "What does the 'melt()' function do in Pandas?",
                "options": ["Summarizes data", "Unpivots a DataFrame from wide format to long format", "Deletes all columns with NaN", "Merges two DataFrames"],
                "answer": "B"
            },
            {
                "level": 5,
                "question": "In NumPy, what is 'broadcasting'?",
                "options": ["Sending data to multiple CPUs", "Resizing an array to fit a disk", "Rules for arithmetic operations between arrays of different shapes", "A method for distributed data analysis"],
                "answer": "C"
            }
        ]
        self.score = 0

    def categorize_skill(self, score):
        if score <= 2:
            return "Beginner"
        elif score <= 4:
            return "Intermediate"
        elif score <= 6:
            return "Advanced"
        elif score <= 8:
            return "Expert"
        else:
            return "Master"

    def run_quiz(self, mock_input=None):
        """Runs the quiz in CLI mode. If mock_input is provided, it uses that instead of interactive input."""
        print("\n" + "="*50)
        print("   🚀 PYTHON DATA ANALYSIS QUIZ: TEST YOUR SKILLS! 🚀")
        print("="*50)
        print("Instructions: Enter the letter (A, B, C, or D) for your choice.\n")

        total_q = len(self.questions)
        input_idx = 0
        self.score = 0 # Reset score for fresh run
        for i, q in enumerate(self.questions):
            print(f"Question {i+1}/{total_q} [Level {q['level']} - {self.levels_map[q['level']]}]")
            print(f"Q: {q['question']}")
            
            options_labels = ['A', 'B', 'C', 'D']
            for idx, opt in enumerate(q['options']):
                print(f"   {options_labels[idx]}. {opt}")
            
            while True:
                if mock_input:
                    if input_idx < len(mock_input):
                        user_input = mock_input[input_idx].upper()
                        input_idx += 1
                        print(f"\nMock answer: {user_input}")
                    else:
                        break
                else:
                    user_input = input("\nYour answer: ").strip().upper()

                if user_input in options_labels:
                    break
                print("Invalid input! Please enter A, B, C, or D.")

            if user_input == q['answer']:
                print("✅ Correct!")
                self.score += 1
            else:
                correct_idx = options_labels.index(q['answer'])
                print(f"❌ Incorrect. The correct answer was {q['answer']}: {q['options'][correct_idx]}")
            print("-" * 30)

        print("\n" + "="*50)
        print("                QUIZ RESULTS")
        print("="*50)
        print(f"Final Score: {self.score} / {total_q}")
        print(f"Assessed Skill Level: {self.categorize_skill(self.score)}")
        print("="*50 + "\n")

if __name__ == "__main__":
    quiz = DataAnalysisQuiz()
    try:
        quiz.run_quiz()
    except EOFError:
        print("\nNote: Input required to run the quiz. Please run in an interactive terminal.")
