import tkinter as tk
from tkinter import messagebox
t=0
def set_timer():
    global t
    t=t+int(entry1.get())
    return t

def countdown():
    global t
    if t>0:
        label1.config(text=t)
        t=t-1
        label1.after(1000,countdown)
    elif t==0:
        print("end")
        messagebox.showinfo("Time Up","Your Time is Over!!!! ")
        root.destroy()
root=tk.Tk()
root.title("Timer")
root.geometry("250x150")
label1 = tk.Label(root,font="times 24")
label1.grid(row=1,column=2)
times=tk.StringVar()
entry1 = tk.Entry(root,textvariable=times)
entry1.grid(row=3,column=2)
btn1 = tk.Button(root,text='SET',width=20,command=set_timer)
btn1.grid(row=4,column=2,padx=20)
btn2 = tk.Button(root,text="START",width=20,command=countdown)
btn2.grid(row=6,column=2,padx=20)

root.mainloop()