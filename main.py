from tkinter import messagebox
from tkinter import *


WINDOW_HEIGHT = 300
WINDOW_WIDTH = 200


def process_choices():
    messagebox.showinfo("Great choice!", f"You've chosen {choice.get()}")


window = Tk()

# TODO: add title
window.title("")
window.geometry(f'{WINDOW_HEIGHT}x{WINDOW_WIDTH}')
window.resizable(width=False, height=False)

center_frame = Frame(window)

label = Label(center_frame, text="Please select a quiz")

choice = StringVar()
r1 = Radiobutton(center_frame, text='Choice 1', variable=choice, value='choice_1')
r2 = Radiobutton(center_frame, text='Choice 2', variable=choice, value='choice_2')

show_btn = Button(center_frame, text='Submit', command=process_choices)
quit_btn = Button(center_frame, text='Quit', command=window.quit)


center_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

label.pack()
r1.pack()
r2.pack()
show_btn.pack()
quit_btn.pack()
window.mainloop()
