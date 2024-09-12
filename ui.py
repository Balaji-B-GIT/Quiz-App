from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self,quiz_brain:QuizBrain):
        self.quiz = quiz_brain
        self.count = None
        self.score = 0
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR,pady=20,padx=20)

        self.score_label = Label(text=f"Score: {self.score}",pady=20,bg=THEME_COLOR,fg="White",font = ("Arial",18,"italic"))
        self.score_label.grid(row = 0 , column = 0,columnspan = 2)

        self.canvas = Canvas(width=300,height=250,bg= "white")
        self.question = self.canvas.create_text(150,125,text="hello",font = ("Arial",20,"italic"),width=280)
        self.canvas.grid(row = 1, column = 0,columnspan=2)

        true = PhotoImage(file = "images/true.png")
        false = PhotoImage(file = "images/false.png")
        self.true_button = Button(image=true,highlightthickness=0,command=self.correct)
        self.true_button.grid(row = 2 , column = 0,pady=20,padx=20)

        self.false_button = Button(image=false,highlightthickness=0,command=self.wrong)
        self.false_button.grid(row = 2 , column = 1,pady=20,padx=20)

        self.get_new_question()

        self.window.mainloop()


    def get_new_question(self):
        self.canvas.configure(bg = "white")
        self.score_label.config(text=f"Score: {self.score}")
        self.canvas.itemconfig(self.question,text = self.quiz.next_question())


    def correct(self):
        is_true = self.quiz.check_answer("true")
        self.feedback(is_true)

    def wrong(self):
        is_true =  self.quiz.check_answer("false")
        self.feedback(is_true)


    def feedback(self,is_true):
        if is_true:
            self.score += 1
            self.canvas.configure(bg = "green")
            self.end_of_quiz_checker()
        else:
            self.canvas.configure(bg = "red")
            self.end_of_quiz_checker()


    def end_of_quiz_checker(self):
        if self.quiz.still_has_questions():
            self.window.after(1000, func=self.end_of_quiz)
        else:
            self.window.after(1000, func=self.get_new_question)

    def end_of_quiz(self):
        self.canvas.configure(bg = "white")
        self.canvas.itemconfig(self.question, text=f"You've completed the quiz\nYour final score was:\n"
                                                   f"            {self.score}/{self.quiz.question_number}")
        self.counter(5)


    def counter(self,count):
        if count > 0:
            self.score_label.config(text=f"Closes in \n{count}")
            self.window.after(1000,self.counter,count - 1)
        elif count == 0:
            self.window.destroy()




