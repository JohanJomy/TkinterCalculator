import tkinter as tk
import maths
import pyttsx3
import time

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

rate = engine.getProperty('rate')                         
engine.setProperty('rate', 165) 

david = voices[0].id
zira = voices[1].id

engine.setProperty('voices', david)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

calculator = tk.Tk()
calculator.title("Calculator")
calculator.resizable(0, 0)
calculator.iconbitmap('./images/calculator2.ico')

frame=tk.Frame(calculator)
enter2=tk.Entry(frame, width=22, borderwidth=0, font=('Comic San MS',25))
enter=tk.Entry(frame, width=12, borderwidth=0, font=('Comic San MS',45))

scientificFrame=tk.Frame(calculator)

voiceOverText = " Voice Over OFF "

background = '#FFFFFF'
text = '#000000'
highlight = '#ADD8E6'

def colourDark():
    global background, text, highlight

    background = '#000000'
    text = '#FFFFFF'
    highlight = '#2F4F4F'
    
    standerd()

def colourLight():
    global background, text, highlight

    background = '#FFFFFF'
    text = '#000000'
    highlight = '#ADD8E6'
    
    standerd()

def colourGold():
    global background, text, highlight

    background = '#FCC200'
    text = '#000000'
    highlight = '#FFD700'
    
    standerd()

def colourSilver():
    global background, text, highlight

    background = '#838996'
    text = '#000000'
    highlight = '#757575'
    
    standerd()

myMenu = tk.Menu(calculator)
calculator.config(menu = myMenu)

history = []

class HoverButton(tk.Button):
    def __init__(self, master, **kw):
        tk.Button.__init__(self,master=master,**kw)
        self.defaultBackground = self["background"]
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)
        #self.bind("<Enter>", self.speechEnter)

    def on_enter(self, e):
        self['background'] = self['activebackground']
        if voiceOverText == " Voice Over ON ":
            speak(self['text'])

    def on_leave(self, e):
        self['background'] = self['activeforeground']
 
def standerd():

    global background, text, highlight

    frame.configure(bg=background)
    frame.grid(row=0, column=0, columnspan=6, padx=0, pady=0)
    
    enter2.configure(justify=tk.RIGHT,width=42)
    enter2.configure(bg=background)
    enter2.configure(fg=text)
    enter2.grid(row=0, column=0, columnspan=8, padx=0, pady=0, ipady=8)

    enter.configure(justify=tk.RIGHT,width=23)
    enter.configure(bg=background)
    enter.configure(fg=text)
    enter.bind("<Return>",maths.equal)
    enter.grid(row=1, column=0, columnspan=8, padx=0, pady=0, ipady=15)
    
    one=HoverButton(frame,text=" 1 ",padx=15,pady=15, borderwidth = 0, command=lambda:maths.buttonClick(1))
    one.grid(row=4,column=3)
    one.configure(bg=background,fg=text, font=('Comic San MS',20),activebackground=highlight,activeforeground=background)

    two=HoverButton(frame, text=" 2 ", padx=15,pady=15, borderwidth = 0, command=lambda:maths.buttonClick(2))
    two.grid(row=4,column=4)
    two.configure(bg=background,fg=text, font=('Comic San MS',20),activebackground=highlight,activeforeground=background)

    three=HoverButton(frame, text=" 3 ",padx=15,pady=15, borderwidth = 0,command=lambda:maths.buttonClick(3))
    three.grid(row=4,column=5)
    three.configure(bg=background,fg=text, font=('Comic San MS',20),activebackground=highlight,activeforeground=background)

    four=HoverButton(frame, text=" 4 ",padx=15,pady=15, borderwidth = 0,command=lambda:maths.buttonClick(4))
    four.grid(row=3,column=3)
    four.configure(bg=background,fg=text, font=('Comic San MS',20),activebackground=highlight,activeforeground=background)

    five=HoverButton(frame, text=" 5 ",padx=15,pady=15, borderwidth = 0,command=lambda:maths.buttonClick(5))
    five.grid(row=3,column=4)
    five.configure(bg=background,fg=text, font=('Comic San MS',20),activebackground=highlight,activeforeground=background)

    six=HoverButton(frame, text=" 6 ",padx=15,pady=15, borderwidth = 0,command=lambda:maths.buttonClick(6))
    six.grid(row=3,column=5)
    six.configure(bg=background,fg=text, font=('Comic San MS',20),activebackground=highlight,activeforeground=background)

    seven=HoverButton(frame, text=" 7 ",padx=15,pady=15, borderwidth = 0,command=lambda:maths.buttonClick(7))
    seven.grid(row=2,column=3)
    seven.configure(bg=background,fg=text, font=('Comic San MS',20),activebackground=highlight,activeforeground=background)

    eight=HoverButton(frame, text=" 8 ",padx=15,pady=15, borderwidth = 0,command=lambda:maths.buttonClick(8))
    eight.grid(row=2,column=4)
    eight.configure(bg=background,fg=text, font=('Comic San MS',20),activebackground=highlight,activeforeground=background)

    nine=HoverButton(frame, text=" 9 ",padx=15,pady=15, borderwidth = 0,command=lambda:maths.buttonClick(9))
    nine.grid(row=2,column=5)
    nine.configure(bg=background,fg=text, font=('Comic San MS',20),activebackground=highlight,activeforeground=background)

    zero=HoverButton(frame, text=" 0 ",padx=15,pady=15,borderwidth = 0, command=lambda:maths.buttonClick(0))
    zero.grid(row=5,column=3)
    zero.configure(bg=background,fg=text, font=('Comic San MS',20),activebackground=highlight,activeforeground=background)

    dot=HoverButton(frame, text=" . ",padx=19,pady=15,borderwidth = 0,command=maths.dot)
    dot.grid(row=5,column=5)
    dot.configure(bg=background,fg=text, font=('Comic San MS',20),activebackground=highlight,activeforeground=background)

    add=HoverButton(frame, text="  +  ",padx=14,pady=15,borderwidth = 0, command=maths.add)
    add.grid(row=5,column=6)
    add.configure(bg=background,fg=text, font=('Comic San MS',20),activebackground=highlight,activeforeground=background)

    subtract=HoverButton(frame, text="  -  ",padx=18,pady=15,borderwidth = 0, command=maths.subtract)
    subtract.grid(row=4,column=6)
    subtract.configure(bg=background,fg=text, font=('Comic San MS',20),activebackground=highlight,activeforeground=background)

    multiply=HoverButton(frame, text="  x  ",padx=17,pady=15,borderwidth = 0,command=maths.multiply)
    multiply.grid(row=3,column=6)
    multiply.configure(bg=background,fg=text, font=('Comic San MS',20),activebackground=highlight,activeforeground=background)

    divide=HoverButton(frame, text="  /  ",padx=18,pady=15,borderwidth = 0,command=maths.divide)
    divide.grid(row=3,column=7)
    divide.configure(bg=background,fg=text, font=('Comic San MS',20),activebackground=highlight,activeforeground=background)

    equalto=HoverButton(frame, text="  =  ",padx=18,pady=15,borderwidth = 0,command=maths.equal)
    equalto.grid(row=5,column=7)
    equalto.configure(bg=background,fg=text, font=('Comic San MS',20),activebackground=highlight,activeforeground=background)

    percent=HoverButton(frame, text=" % ",padx=17,pady=15,borderwidth = 0,command=maths.percent)
    percent.grid(row=4,column=7)
    percent.configure(bg=background,fg=text, font=('Comic San MS',20),activebackground=highlight,activeforeground=background)

    clear=HoverButton(frame, text="AC",padx=17,pady=15,borderwidth = 0,command=maths.clear)
    clear.grid(row=2,column=7)
    clear.configure(bg=background,fg=text, font=('Comic San MS',20),activebackground=highlight,activeforeground=background)

    delete=HoverButton(frame, text=" C ",padx=16,pady=15,borderwidth = 0,command=maths.delete)
    delete.grid(row=2,column=6)
    delete.configure(bg=background,fg=text, font=('Comic San MS',20),activebackground=highlight,activeforeground=background)

    plusminus=HoverButton(frame, text=" ± ",padx=15,pady=15,borderwidth = 0,command=maths.plusMinus)
    plusminus.grid(row=5,column=4)
    plusminus.configure(bg=background,fg=text, font=('Comic San MS',20),activebackground=highlight,activeforeground=background)

    rightBracket=HoverButton(frame, text=" ) ",padx=25,pady=15, borderwidth = 0,command=maths.rightBracket)
    rightBracket.grid(row=2,column=1)
    rightBracket.configure(bg=background,fg=text, font=('Comic San MS',20),activebackground=highlight,activeforeground=background)

    leftBracket=HoverButton(frame, text=" ( ",padx=25,pady=15, borderwidth = 0,command=maths.leftBracket)
    leftBracket.grid(row=2,column=0)
    leftBracket.configure(bg=background,fg=text, font=('Comic San MS',20),activebackground=highlight,activeforeground=background)

    log=HoverButton(frame, text="log",padx=20,pady=15, borderwidth = 0,command=maths.log)
    log.grid(row=2,column=2)
    log.configure(bg=background,fg=text, font=('Comic San MS',20),activebackground=highlight,activeforeground=background)

    sin=HoverButton(frame, text="sin",padx=20,pady=15, borderwidth = 0,command=maths.sin)
    sin.grid(row=3,column=0)
    sin.configure(bg=background,fg=text, font=('Comic San MS',20),activebackground=highlight,activeforeground=background)

    cos=HoverButton(frame, text="cos",padx=20,pady=15, borderwidth = 0,command=maths.cos)
    cos.grid(row=3,column=1)
    cos.configure(bg=background,fg=text, font=('Comic San MS',20),activebackground=highlight,activeforeground=background)

    tan=HoverButton(frame, text="tan",padx=19,pady=15, borderwidth = 0,command=maths.tan)
    tan.grid(row=3,column=2)
    tan.configure(bg=background,fg=text, font=('Comic San MS',20),activebackground=highlight,activeforeground=background)

    sinh=HoverButton(frame, text="sinh",padx=10,pady=15, borderwidth = 0,command=maths.sinh)
    sinh.grid(row=4,column=0)
    sinh.configure(bg=background,fg=text, font=('Comic San MS',20),activebackground=highlight,activeforeground=background)

    cosh=HoverButton(frame, text="cosh",padx=10,pady=15, borderwidth = 0,command=maths.cosh)
    cosh.grid(row=4,column=1)
    cosh.configure(bg=background,fg=text, font=('Comic San MS',20),activebackground=highlight,activeforeground=background)

    tanh=HoverButton(frame, text="tanh",padx=12,pady=15, borderwidth = 0,command=maths.tanh)
    tanh.grid(row=4,column=2)
    tanh.configure(bg=background,fg=text, font=('Comic San MS',20),activebackground=highlight,activeforeground=background)

    root=HoverButton(frame, text=" √ ",padx=25,pady=15, borderwidth = 0,command=maths.root)
    root.grid(row=5,column=0)
    root.configure(bg=background,fg=text, font=('Comic San MS',20),activebackground=highlight,activeforeground=background)

    pi=HoverButton(frame, text=" π ",padx=25,pady=15, borderwidth = 0, command=maths.pi)
    pi.grid(row=5,column=1)
    pi.configure(bg=background,fg=text, font=('Comic San MS',20),activebackground=highlight,activeforeground=background)

    square=HoverButton(frame, text=" xⁿ ",padx=22,pady=15, borderwidth = 0,command=maths.square)
    square.grid(row=5,column=2)
    square.configure(bg=background,fg=text, font=('Comic San MS',20),activebackground=highlight,activeforeground=background)

    voiceOver=HoverButton(frame, text=voiceOverText,padx=270,pady=15, borderwidth = 0,command=maths.voiceOver)
    voiceOver.grid(row=6,column=0,columnspan=8)
    voiceOver.configure(bg=background,fg=text, font=('Comic San MS',20),activebackground=highlight,activeforeground=background)
    
    calculator.mainloop()

def historyPage():
    HistoryFrame = tk.Tk()
    HistoryFrame.title("History")
    HistoryFrame.iconbitmap('./images/calculator2.ico')
    HistoryFrame.geometry("400x400")
    HistoryFrame.resizable(0, 0)

    HistoryFrame.configure(bg='white')
    historyLabel = tk.Listbox(HistoryFrame,justify=tk.LEFT,font=("Comic San MS", 18))
    historyLabel.pack(fill=tk.BOTH)

    for histories in history:
        historyLabel.insert(tk.END, " " + histories)
        