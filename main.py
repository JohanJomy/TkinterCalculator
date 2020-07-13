import tkinter
import views

view= views.tk.Menu(views.myMenu, tearoff = False, background = 'white', foreground = 'black',)
views.myMenu.add_cascade(label = 'View',menu = view)

view.add_command(label = 'Light' ,command=views.colourLight)
view.add_command(label = 'Dark' ,command=views.colourDark )
view.add_command(label = 'Gold' ,command=views.colourGold)
view.add_command(label = 'Silver' ,command=views.colourSilver)

history = views.tk.Menu(views.myMenu, tearoff = False, background = 'white', foreground = 'black',)
views.myMenu.add_cascade(label = 'History',menu = history)
history.add_command(label = 'History' ,command= views.historyPage)

views.standerd()