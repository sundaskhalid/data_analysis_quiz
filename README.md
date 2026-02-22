# Data Analysis Quiz App

A Python-based quiz application to test data manipulation and wrangling skills using Pandas and NumPy.

[![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

## Features
- 10 Questions across 5 levels (Beginner, Intermediate, Advanced, Expert, Master).
- Tracks score and assesses skill level based on performance.
- Two interfaces: Command Line Interface (CLI) and Graphical User Interface (GUI).

## Prerequisites
- Python 3.x
- Pandas (`pip install pandas`)
- NumPy (`pip install numpy`)

## How to Run

### Option 1: Graphical User Interface (GUI)
This is the recommended way to take the quiz.
```bash
python quiz_gui.py
```

### Option 2: Command Line Interface (CLI)
Run the quiz directly in your terminal.
```bash
python quiz_app.py
```

## Question Levels
1. **Novice**: Basic operations (reading CSV, head).
2. **Intermediate**: Selection and filtering (boolean indexing).
3. **Advanced**: Data cleaning and manipulation (fillna, rename).
4. **Expert**: Aggregation and Joins (groupby, inner join).
5. **Master**: Reshaping and Optimization (melt, broadcasting).

## Scoring & Skill Categorization
- 0-2: Beginner
- 3-4: Intermediate
- 5-6: Advanced
- 7-8: Expert
- 9-10: Master
