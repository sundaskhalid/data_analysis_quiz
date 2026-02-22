import unittest
from quiz_app import DataAnalysisQuiz

class TestDataAnalysisQuiz(unittest.TestCase):
    def setUp(self):
        self.quiz = DataAnalysisQuiz()

    def test_initial_score(self):
        self.assertEqual(self.quiz.score, 0)

    def test_skill_categorization(self):
        self.assertEqual(self.quiz.categorize_skill(2), "Beginner")
        self.assertEqual(self.quiz.categorize_skill(4), "Intermediate")
        self.assertEqual(self.quiz.categorize_skill(6), "Advanced")
        self.assertEqual(self.quiz.categorize_skill(8), "Expert")
        self.assertEqual(self.quiz.categorize_skill(10), "Master")

    def test_questions_count(self):
        self.assertEqual(len(self.quiz.questions), 10)

    def test_question_structure(self):
        for q in self.quiz.questions:
            self.assertIn("level", q)
            self.assertIn("question", q)
            self.assertIn("options", q)
            self.assertIn("answer", q)
            self.assertIsInstance(q["options"], list)

    def test_levels_coverage(self):
        levels = set(q['level'] for q in self.quiz.questions)
        self.assertEqual(levels, {1, 2, 3, 4, 5})

if __name__ == "__main__":
    unittest.main()
