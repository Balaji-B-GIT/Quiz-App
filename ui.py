from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self,quiz_brain:QuizBrain):
        self.no_of_que = 0
        self.quiz = quiz_brain
        self.score = quiz_brain.score
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR,pady=20,padx=20)

        self.score_label = Label(text=f"Score: {self.score}",pady=20,bg=THEME_COLOR,fg="White",font = ("Arial",18,"italic"))
        self.score_label.grid(row = 0 , column = 1)

        self.canvas = Canvas(width=300,height=250,bg= "white")
        self.question = self.canvas.create_text(150,125,text="hello",font = ("Arial",20,"italic"),width=280)
        self.canvas.grid(row = 1, column = 0,columnspan=2)

        true = PhotoImage(file = "images/true.png")
        false = PhotoImage(file = "images/false.png")
        self.true_button = Button(image=true,highlightthickness=0,command=self.correct)
        self.true_button.grid(row = 2 , column = 0,pady=20,padx=20)

        self.false_button = Button(image=false,highlightthickness=0,command=self.wrong)
        self.false_button.grid(row = 2 , column = 1,pady=20,padx=20)

        self.new_question()

        self.window.mainloop()

    def new_question(self):
        self.canvas.itemconfig(self.question,text = self.quiz.next_question())


    def correct(self):
        self.no_of_que += 1
        self.quiz_completed()
        self.score = self.quiz.check_answer("true")
        self.score_label.config(text = f"Score: {self.score}")
        self.new_question()

    def wrong(self):
        self.no_of_que += 1
        self.quiz_completed()
        self.score = self.quiz.check_answer("false")
        self.score_label.config(text=f"Score: {self.score}")
        self.new_question()

    def quiz_completed(self):
        if self.no_of_que == 10:
            self.canvas.itemconfig(self.question, text=f"Your final score was: {self.score}/{self.quiz.question_number}")



