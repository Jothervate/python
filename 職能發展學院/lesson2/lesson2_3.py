import tkinter as tk

window=tk.Tk()
window.title("Hello Tkinter")
window.geometry("500x100")
label = tk.Label(window,text="Hello World",bg='yellow', fg='#263238', font=('Arial', 20))
label.pack()
window.mainloop()