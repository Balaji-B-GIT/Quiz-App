from tkinter import *
THEME_COLOR = "#375362"

class QuizInterface():

    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR,pady=20,padx=20)

        self.score = Label(text="Score: 0",pady=20,bg=THEME_COLOR,fg="White",font = ("Arial",18,"italic"))
        self.score.grid(row = 0 , column = 1)

        self.canvas = Canvas(width=300,height=250)
        self.canvas.create_text(150,125,text="hello",font = ("Arial",40,"italic"))
        self.canvas.grid(row = 1, column = 0,columnspan=2)

        self.true = PhotoImage(file = "images/true.png")
        self.false = PhotoImage(file = "images/false.png")
        self.true_button = Button(image=self.true,highlightthickness=0,padx=20,pady=20)
        self.true_button.grid(row = 2 , column = 0,pady=20,padx=20)

        self.false_button = Button(image=self.false,highlightthickness=0)
        self.false_button.grid(row = 2 , column = 1,pady=20,padx=20)


        self.window.mainloop()

QuizInterface()