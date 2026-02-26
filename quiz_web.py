import streamlit as st
from quiz_app import DataAnalysisQuiz

def main():
    st.set_page_config(page_title="Python Data Analysis Quiz", page_icon="🚀", layout="centered")

    # Custom CSS for Dark Theme and Aesthetics
    st.markdown("""
        <style>
        .main {
            background-color: #121212;
            color: #ffffff;
        }
        .stButton>button {
            width: 100%;
            border-radius: 5px;
            height: 3em;
            background-color: #1e1e1e;
            color: #3498db;
            border: 2px solid #3498db;
            font-weight: bold;
        }
        .stButton>button:hover {
            background-color: #3498db;
            color: #ffffff;
        }
        .question-text {
            font-size: 24px;
            font-weight: bold;
            margin-bottom: 20px;
        }
        .info-text {
            color: #3498db;
            font-size: 16px;
        }
        </style>
    """, unsafe_allow_html=True)

    if 'quiz' not in st.session_state:
        st.session_state.quiz = DataAnalysisQuiz()
        st.session_state.current_q = 0
        st.session_state.score = 0
        st.session_state.finished = False

    quiz = st.session_state.quiz

    st.title("🚀 Python Data Analysis Quiz")

    if not st.session_state.finished:
        q_idx = st.session_state.current_q
        total_q = len(quiz.questions)
        q = quiz.questions[q_idx]

        st.markdown(f"<p class='info-text'>Question {q_idx + 1} of {total_q} | Level {q['level']} - {quiz.levels_map[q['level']]}</p>", unsafe_allow_html=True)
        st.markdown(f"<p class='question-text'>{q['question']}</p>", unsafe_allow_html=True)

        options = q['options']
        # Map A, B, C, D to options
        option_labels = ['A', 'B', 'C', 'D']
        
        selection = st.radio("Choose the correct answer:", options, index=None, key=f"q_{q_idx}")

        if st.button("Submit Answer"):
            if selection:
                selected_letter = option_labels[options.index(selection)]
                if selected_letter == q['answer']:
                    st.success("✅ Correct!")
                    st.session_state.score += 1
                else:
                    correct_idx = option_labels.index(q['answer'])
                    st.error(f"❌ Incorrect. The correct answer was {q['answer']}: {options[correct_idx]}")
                
                if st.session_state.current_q + 1 < total_q:
                    st.session_state.current_q += 1
                    st.rerun()
                else:
                    st.session_state.finished = True
                    st.rerun()
            else:
                st.warning("Please select an option before submitting.")
    else:
        st.balloons()
        st.header("Quiz Results")
        total_q = len(quiz.questions)
        score = st.session_state.score
        skill = quiz.categorize_skill(score)

        st.metric("Final Score", f"{score} / {total_q}")
        st.subheader(f"Assessed Skill Level: {skill}")

        if st.button("Restart Quiz"):
            st.session_state.current_q = 0
            st.session_state.score = 0
            st.session_state.finished = False
            st.rerun()

if __name__ == "__main__":
    main()
