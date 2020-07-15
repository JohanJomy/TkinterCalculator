import tkinter
import views
import math

def voiceOver():
    if views.voiceOverText == " Voice Over OFF ":
        views.voiceOverText = " Voice Over ON "
        views.standerd()
    elif views.voiceOverText == " Voice Over ON ":
        views.voiceOverText = " Voice Over OFF "
        views.standerd()

def buttonClick(number):
    current=views.enter.get()
    views.enter.delete(0,views.tk.END)
    views.enter.insert(0, str(current) + str(number))

def dot():
    current=views.enter.get()
    views.enter.delete(0,views.tk.END)
    views.enter.insert(0, str(current) + '.')

def add():
    current=views.enter.get()
    views.enter.delete(0,views.tk.END)
    views.enter.insert(0,str(current) + '+')

def subtract():
    current=views.enter.get()
    views.enter.delete(0,views.tk.END)
    views.enter.insert(0,str(current) + '-')

def multiply():
    current=views.enter.get()
    views.enter.delete(0,views.tk.END)
    views.enter.insert(0,str(current) + '*') 

def divide():
    current=views.enter.get()
    views.enter.delete(0,views.tk.END)
    views.enter.insert(0,str(current) + '/')

def clear():
    views.enter.delete(0,views.tk.END)
    views.enter2.delete(0,views.tk.END)

def equal():

    equation = views.enter.get()
    views.enter2.delete(0,views.tk.END)
    views.enter2.insert(0,equation)
    result=eval(views.enter.get())
    views.enter.delete(0,views.tk.END)
    resultString = str(result)
    if views.voiceOverText == " Voice Over ON ":
        views.speak(resultString)
    resultLength = len(resultString)    
    if resultString[resultLength-2:] =='.0':
        result = str(resultString[:resultLength-2])

    views.enter.insert(0,result)

    views.history.append(f'{equation} = {result}')

def delete():
    current=len(views.enter.get())
    last = current - 1
    views.enter.delete(last,views.tk.END)

def percent():
    firstNumber=float(views.enter.get())
    views.enter.delete(0,views.tk.END)
    views.enter2.delete(0,views.tk.END)
    views.enter.insert(0,firstNumber / 100 )
    views.enter2.insert(0,f'{firstNumber}/100' )
    views.history.append(f'{firstNumber}/100 = {firstNumber / 100}')

def plusMinus():
    current=views.enter.get()
    plus = current[0:1]
        
    if plus == '0' or plus == '1' or plus == '2' or plus == '3' or plus == '4' or plus == '5' or plus == '6' or plus == '7' or plus == '8' or plus == '9':  
        views.enter.insert(0,'-')
    else:
        views.enter.delete(0,1)

def root():
    current=views.enter.get()
    views.enter.delete(0,views.tk.END)
    views.enter2.delete(0,views.tk.END)
    root = math.sqrt(float(current))
    views.enter.insert(0,root)   
    equation = f'√{current}'
    views.enter2.insert(0,equation)
    views.history.append(f'{equation} = {root}')
    if views.voiceOverText == " Voice Over ON ":
        views.speak(root)

def sin():
    current=views.enter.get()
    views.enter.delete(0,views.tk.END)
    views.enter2.delete(0,views.tk.END)
    sin = math.sin(float(current))
    views.enter.insert(0,sin)   
    equation = f'sin({current})'
    views.enter2.insert(0,equation)
    views.history.append(f'{equation} = {sin}')
    if views.voiceOverText == " Voice Over ON ":
        views.speak(sin)

def cos():
    current=views.enter.get()
    views.enter.delete(0,views.tk.END)
    views.enter2.delete(0,views.tk.END)
    cos = math.cos(float(current))
    views.enter.insert(0,cos)   
    equation = f'cos({current})'
    views.enter2.insert(0,equation)
    views.history.append(f'{equation} = {cos}')
    if views.voiceOverText == " Voice Over ON ":
        views.speak(cos)

def tan():
    current=views.enter.get()
    views.enter.delete(0,views.tk.END)
    views.enter2.delete(0,views.tk.END)
    tan = math.tan(float(current))
    views.enter.insert(0,tan)   
    equation = f'tan({current})'
    views.enter2.insert(0,equation)
    views.history.append(f'{equation} = {tan}')
    if views.voiceOverText == " Voice Over ON ":
        views.speak(tan)

def sinh():
    current=views.enter.get()
    views.enter.delete(0,views.tk.END)
    views.enter2.delete(0,views.tk.END)
    sinh = math.sinh(float(current))
    views.enter.insert(0,sinh)   
    equation = f'sinh({current})'
    views.enter2.insert(0,equation)
    views.history.append(f'{equation} = {sinh}')
    if views.voiceOverText == " Voice Over ON ":
        views.speak(sinh)

def cosh():
    current=views.enter.get()
    views.enter.delete(0,views.tk.END)
    views.enter2.delete(0,views.tk.END)
    cosh = math.cosh(float(current))
    views.enter.insert(0,cosh)   
    equation = f'cosh({current})'
    views.enter2.insert(0,equation)
    views.history.append(f'{equation} = {cosh}')
    if views.voiceOverText == " Voice Over ON ":
        views.speak(cosh)

def tanh():
    current=views.enter.get()
    views.enter.delete(0,views.tk.END)
    views.enter2.delete(0,views.tk.END)
    tanh = math.tanh(float(current))
    views.enter.insert(0,tanh)   
    equation = f'tanh({current})'
    views.enter2.insert(0,equation)
    views.history.append(f'{equation} = {tanh}')
    if views.voiceOverText == " Voice Over ON ":
        views.speak(tanh)

def leftBracket():
    current=views.enter.get()
    views.enter.delete(0,views.tk.END)
    views.enter.insert(0, str(current) + '(' )

def rightBracket():
    current=views.enter.get()
    views.enter.delete(0,views.tk.END)
    views.enter.insert(0, str(current) + ')' )

def log():
    current=views.enter.get()
    views.enter.delete(0,views.tk.END)
    log = str(math.log10(float(current)))
    views.enter.insert(0, log )
    equation = f'log({current})'
    views.enter2.insert(0,equation)
    views.history.append(f'{equation} = {log}')
    if views.voiceOverText == " Voice Over ON ":
        views.speak(log)

def pi():
    current=views.enter.get()
    views.enter.delete(0,views.tk.END)
    pi = str(math.pi)
    views.enter.insert(0, str(current) + pi )

def square():
    current=views.enter.get()
    views.enter.delete(0,views.tk.END)
    views.enter.insert(0, str(current) + '**' )