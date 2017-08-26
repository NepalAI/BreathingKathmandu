import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib import style
style.use('ggplot')
import tkinter as tk
from tkinter import ttk
matplotlib.use("TkAgg")


LARGE_FONT = ("Verdana", 12)

f = Figure(figsize=(5,5), dpi=100)
a = f.add_subplot(111)

def animate(i):

    pullData = open('sample.txt','r').read()
    dataList = pullData.split('\n')
    xList = []
    yList = []

    for eachLine in dataList:
        if len(eachLine) > 1:
            x, y = eachLine.split(',')
            xList.append(int(x))
            yList.append(int(y))

    a.clear()
    a.plot(xList, yList)

# Define BreathingKathmandu class

# We're inheriting everything from the tk.Tk class.

class BreathingKathmandu(tk.Tk):

    # Whatever you put in here is going to always run whenever the class is called upon.

    # The other methods will only run when you specifically call upon them to run.

    def __init__(self, *args, **kwargs):

        # https://stackoverflow.com/questions/36901/what-does-double-star-and-star-do-for-parameters

        # https://stackoverflow.com/questions/287085/what-do-args-and-kwargs-mean#287101

        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.wm_title(self, "Breathing Kathmandu")

        # We've defined this container, which will be filled with a bunch of frames to be accessed later on.

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne, PageTwo, PageThree):
            frame = F(container, self)
            self.frames[F] = frame

            # "nsew" corresponds to directions (north, south, east, west).
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

# We're defining the Start Page class where all the start page functions are executed.

class StartPage(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)

        label = ttk.Label(self, text="Breathing Kathmandu", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button = ttk.Button(self, text="Visit Page 1",
                           command=lambda: controller.show_frame(PageOne))
        button.pack()

        button2 = ttk.Button(self, text="Visit Page 2",
                            command=lambda: controller.show_frame(PageTwo))
        button2.pack()

        button3 = ttk.Button(self, text="Pollution",
                             command=lambda: controller.show_frame(PageThree))
        button3.pack()


class PageOne(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)

        label = ttk.Label(self, text="Page One!!!", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = ttk.Button(self, text="Page Two",
                            command=lambda: controller.show_frame(PageTwo))
        button2.pack()


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)

        label = ttk.Label(self, text="Page Two!!!", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = ttk.Button(self, text="Page One",
                            command=lambda: controller.show_frame(PageOne))
        button2.pack()

# class PageThree loads the page that has plots

class PageThree(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text="Realtime Pollution Chart", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                             command=lambda: controller.show_frame(StartPage))
        button1.pack()

        # f = Figure(figsize=(5, 5), dpi=100)
        #
        # a = f.add_subplot(111)
        # a.plot([1, 2, 3, 4, 5, 6, 7, 8], [5, 6, 1, 3, 8, 9, 3, 5])

        canvas = FigureCanvasTkAgg(f, self)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

app = BreathingKathmandu()
ani = animation.FuncAnimation(f,animate, interval=1000)
app.mainloop()
