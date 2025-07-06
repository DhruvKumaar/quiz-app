# Project 4: Quiz App Using Tkinter

## Overview

A simple graphical quiz application developed using Python and Tkinter. This project allows users to take a multiple-choice quiz through a clean and interactive user interface.

## Features

- Graphical User Interface (GUI) built with Tkinter
- Multiple-choice questions with four options each
- Navigation buttons: Previous and Next
- Stores user-selected answers for navigation and review
- Shows a detailed result summary at the end
- Calculates and displays final score

## Requirements

- **Python 3.x**
- **Tkinter** (usually included by default in Python installations)

## How to Run

1. Make sure Python is installed on your system.
2. Save the code into a file named `quiz_app.py`.
3. Open a terminal or command prompt.
4. Navigate to the folder containing `quiz_app.py`.
5. Run the script using:

```bash
python quiz_app.py
```

## Output

- A window opens with the quiz interface.
- Each question appears with four options as radio buttons.
- Users can go back and forth between questions.
- If no option is selected and Next is clicked, a warning is shown.
- After the last question, a summary popup appears showing:
  - Correct answers (✓)
  - Incorrect answers (×)
  - Final score out of total questions
