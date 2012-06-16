from Tkinter import *
from datetime import datetime
from time import gmtime, strftime

stack = []
stack.append({'name': "Idle", 'started': datetime.now()})

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.task = StringVar()
        self.timer = StringVar()
        self.task.set("Idle")
        self.timer.set("00:00:00")
        self.createWidgets()
        self.pack()
        self.taskEntry.bind("<Return>", self.pushtask)
        self.updateTimer()

    def createWidgets(self):
        self.taskEntry = Entry(self, textvariable=self.task)
        self.taskEntry.grid(row=0, padx=10, pady=10)
        self.taskEntry.configure(highlightbackground="#EDEDED")

        self.timerLabel = Label(self, textvariable=self.timer)
        self.timerLabel.grid(row=1)
        self.timerLabel.configure(background="#EDEDED")

        self.popButton = Button(self, text="Pop Task", width=18, command=self.poptask)
        self.popButton.grid(row=2, padx=10, pady=10)
        self.popButton.configure(highlightbackground="#EDEDED")

    def updateTimer(self):
        timedelta = datetime.now() - stack[-1]['started']
        timedelta = gmtime(timedelta.seconds)
        self.timer.set(strftime("%H:%M:%S", timedelta))
        self.master.after(1000, self.updateTimer)

    def poptask(self):
        if len(stack) > 1:
            stack.pop()
            if len(stack) == 1:
                stack.pop()
                stack.append({'name': "Idle", 'started': datetime.now()})
        self.task.set(stack[-1]['name'])
        self.updateTimer()

    def pushtask(self, event):
        stack.append({'name': self.task.get(), 'started': datetime.now()})
        self.updateTimer()

def main():
    root = Tk()
    root.resizable(0, 0)
    root.title('Timestack')
    app = Application(master=root)
    app.configure(background="#EDEDED")
    app.mainloop()
    try:
        root.destroy()
    except TclError:
        pass

if __name__ == "__main__":
    main()
