import tkinter as tk
from tkinter import messagebox

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz App")
        self.root.configure(bg="#f0f0f0")  # Set background color
        self.questions = [
            {"question": "What is the capital of France?", "options": ["Paris", "London", "Berlin"], "answer": "Paris"},
            {"question": "What is the largest planet in the solar system?", "options": ["Earth", "Jupiter", "Mars"], "answer": "Jupiter"},
            {"question": "Who wrote 'Romeo and Juliet'?", "options": ["William Shakespeare", "Charles Dickens", "Jane Austen"], "answer": "William Shakespeare"},
            {"question": "Which country is famous for the Great Wall?", "options": ["China", "India", "USA"], "answer": "China"},
            {"question": "What is the chemical symbol for water?", "options": ["H2O", "CO2", "NaCl"], "answer": "H2O"},
            {"question": "Who painted the Mona Lisa?", "options": ["Leonardo da Vinci", "Pablo Picasso", "Vincent van Gogh"], "answer": "Leonardo da Vinci"},
            {"question": "What is the currency of Japan?", "options": ["Yen", "Dollar", "Euro"], "answer": "Yen"},
            {"question": "What is the tallest mammal?", "options": ["Giraffe", "Elephant", "Horse"], "answer": "Giraffe"},
            {"question": "Who is known as the father of modern physics?", "options": ["Albert Einstein", "Isaac Newton", "Galileo Galilei"], "answer": "Albert Einstein"},
            {"question": "Which planet is known as the Red Planet?", "options": ["Mars", "Venus", "Saturn"], "answer": "Mars"}
        ]
        self.current_question_index = 0
        self.score = 0
        self.total_marks = len(self.questions)
        self.create_widgets()

    def create_widgets(self):
        self.question_label = tk.Label(self.root, text="", wraplength=400, bg="#f0f0f0", font=("Arial", 16))  # Set background color and font size
        self.question_label.pack(pady=20)

        self.option_var = tk.StringVar()
        for i in range(3):
            option_radio = tk.Radiobutton(self.root, text="", variable=self.option_var, value="", command=self.select_option, bg="#f0f0f0", font=("Arial", 14))  # Set background color and font size
            option_radio.pack(anchor=tk.W, padx=20, pady=5)

        self.next_button = tk.Button(self.root, text="Next", command=self.next_question, bg="#009688", fg="white", font=("Arial", 14))  # Set background and text color, font size
        self.next_button.pack(pady=10)

        self.show_answer_button = tk.Button(self.root, text="Show Answer", command=self.show_answer, bg="#ffa000", fg="white", font=("Arial", 14))  # Set background and text color, font size
        self.show_answer_button.pack(pady=10)

        self.quit_button = tk.Button(self.root, text="Quit", command=self.quit_quiz, bg="#f44336", fg="white", font=("Arial", 14))  # Set background and text color, font size
        self.quit_button.pack(pady=10)

        self.update_question()

    def update_question(self):
        question_info = self.questions[self.current_question_index]
        self.question_label.config(text=question_info["question"])
        options = question_info["options"]
        for i in range(3):
            option_radio = self.root.winfo_children()[i + 1]  # Skip question_label
            option_radio.config(text=options[i], value=options[i])

    def select_option(self):
        selected_option = self.option_var.get()
        correct_answer = self.questions[self.current_question_index]["answer"]
        if selected_option == correct_answer:
            self.score += 1
            messagebox.showinfo("Feedback", "Correct!")
            self.next_question()
        else:
            messagebox.showerror("Feedback", f"Incorrect! The correct answer is {correct_answer}")

    def next_question(self):
        self.current_question_index += 1
        if self.current_question_index < len(self.questions):
            self.update_question()
        else:
            if self.score == len(self.questions):
                messagebox.showinfo("Quiz Complete", "Congratulations! You got all the answers correct.")
            else:
                messagebox.showinfo("Quiz Complete", f"You have completed the quiz. Your score is {self.score}/{self.total_marks}.")

    def show_answer(self):
        correct_answer = self.questions[self.current_question_index]["answer"]
        messagebox.showinfo("Correct Answer", f"The correct answer is: {correct_answer}")

    def quit_quiz(self):
        messagebox.showinfo("Quiz Score", f"Your secured marks: {self.score}/{self.total_marks}")

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
