import tkinter as tk
from tkinter import messagebox

questions = [
    ("Що таке векторна графіка?",
     ["Зображення, побудоване з пікселів",
      "Зображення, яке описується за допомогою математичних формул",
      "Анімована графіка",
      "Растрова карта зображення"],
     1),
    ("Яке з наведених програм призначене для роботи з векторною графікою?",
     ["Adobe Photoshop", "GIMP", "Adobe Illustrator", "Paint"],
     2),
    ("Який з форматів є векторним?",
     [".jpg", ".png", ".svg", ".bmp"],
     2),
    ("Яка перевага векторної графіки над растровою?",
     ["Краще виглядає при малих розмірах",
      "Підтримує більше кольорів",
      "Не втрачає якості при масштабуванні",
      "Має менший розмір файлу"],
     2),
    ("Яке ПЗ є безкоштовною альтернативою Adobe Illustrator?",
     ["InDesign", "Sketch", "Inkscape", "Paint.NET"],
     2),
    ("Яка основна одиниця побудови зображення у векторній графіці?",
     ["Піксель", "Вектор", "Крапка", "Лінія"],
     1),
    ("Для чого використовується програма CorelDRAW?",
     ["Для створення таблиць", "Для роботи з текстом",
      "Для створення та редагування векторної графіки", "Для програмування"],
     2),
    ("Що є прикладом об'єкта у векторній графіці?",
     ["Піксель", "Масив", "Коло", "Фільтр"],
     2),
    ("Який інструмент використовується для створення кривих?",
     ["Ластик", "Перо (Pen tool)", "Гумка", "Кисть"],
     1),
    ("Яка професія найчастіше використовує векторну графіку?",
     ["Програміст", "Журналіст", "Графічний дизайнер", "Сценарист"],
     2),
    ("У якій галузі найчастіше використовують векторну графіку?",
     ["Веб-дизайн", "Фотографія", "Відеомонтаж", "Текстовий аналіз"],
     0),
    ("Що відбудеться з векторним зображенням при зміні його розміру?",
     ["Зменшиться якість", "Втратить чіткість", "Не зміниться якість", "Стане розмитим"],
     2)
]

class TestApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Тест: Векторна графіка")
        self.current = 0
        self.score = 0
        self.user_answers = []

        self.question_label = tk.Label(root, text="", font=("Arial", 14), wraplength=600, justify="left")
        self.question_label.pack(pady=10)

        self.buttons = []
        for i in range(4):
            btn = tk.Button(root, text="", font=("Arial", 12), width=60, command=lambda i=i: self.check_answer(i))
            btn.pack(pady=3)
            self.buttons.append(btn)

        self.display_question()

    def display_question(self):
        q, options, _ = questions[self.current]
        self.question_label.config(text=f"{self.current + 1}. {q}")
        for i, option in enumerate(options):
            self.buttons[i].config(text=option)
            self.buttons[i].pack()
        for i in range(len(options), 4):  # hide unused buttons
            self.buttons[i].pack_forget()

    def check_answer(self, selected):
        _, _, correct = questions[self.current]
        self.user_answers.append(selected)
        if selected == correct:
            self.score += 1
        self.current += 1
        if self.current < len(questions):
            self.display_question()
        else:
            self.show_result()

    def show_result(self):
        result_text = f"Ваш результат: {self.score} з {len(questions)}"
        messagebox.showinfo("Результат тесту", result_text)
        self.root.destroy()

# Запуск
root = tk.Tk()
app = TestApp(root)
root.mainloop()
