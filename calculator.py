from tkinter import *
root=Tk()
def click(event):
   
    global scvalue
    text=event.widget.cget("text")
    if text=="=":
       if scvalue.get().isdigit():
          value=int(scvalue.get())
       else:
          value=eval(screen.get())
       scvalue.set(value)
       screen.update()
    elif text=="AC":
       scvalue.set("")
       screen.update()
    else:
       scvalue.set(scvalue.get()+text)
       screen.update()

root.geometry("400x670")
root.title("Calculator")
root.config(bg="black")
scvalue=StringVar()
scvalue.set("")
screen=Entry(root,textvariable=scvalue,font="lucida 40 bold",background="black",fg="white")
screen.pack(fill=X,ipadx=5,ipady=5,padx=5)

f=Frame(root,bg="black")
b=Button(f,text="AC",font="sanfrancisco 30 bold",background="gray45",fg="white")
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>",click)
b=Button(f,text="+/-",font="sanfrancisco 30 bold",background="gray45",fg="white")
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>",click)
b=Button(f,text="%",font="sanfrancisco 30 bold",background="gray45",fg="white")
b.pack(side=LEFT,padx=10,pady=5)
b.bind("<Button-1>",click)
b=Button(f,text="/",font="sanfrancisco 35 bold",background="darkorange",fg="white")
b.pack(side=LEFT,padx=10,pady=5)
b.bind("<Button-1>",click)
f.pack()
f=Frame(root,bg="black")
b=Button(f,text="7",font="sanfrancisco 35 bold",background="gray11",fg="white")
b.pack(side=LEFT,padx=10,pady=5)
b.bind("<Button-1>",click)
b=Button(f,text="8",font="sanfrancisco 35 bold",background="gray11",fg="white")
b.pack(side=LEFT,padx=10,pady=5)
b.bind("<Button-1>",click)
b=Button(f,text="9",font="sanfrancisco 35 bold",background="gray11",fg="white")
b.pack(side=LEFT,padx=10,pady=5)
b.bind("<Button-1>",click)
b=Button(f,text="*",font="sanfrancisco 35 bold",background="darkorange",fg="white")
b.pack(side=LEFT,padx=10,pady=5)
b.bind("<Button-1>",click)
f.pack()

f=Frame(root,bg="black")
b=Button(f,text="4",font="sanfrancisco 35 bold",background="gray11",fg="white")
b.pack(side=LEFT,padx=10,pady=5)
b.bind("<Button-1>",click)
b=Button(f,text="5",font="sanfrancisco 35 bold",background="gray11",fg="white")
b.pack(side=LEFT,padx=10,pady=5)
b.bind("<Button-1>",click)
b=Button(f,text="6",font="sanfrancisco 35 bold",background="gray11",fg="white")
b.pack(side=LEFT,padx=10,pady=5)
b.bind("<Button-1>",click)
b=Button(f,text="-",font="sanfrancisco 35 bold",background="darkorange",fg="white")
b.pack(side=LEFT,padx=15,pady=5)
b.bind("<Button-1>",click)
f.pack()

f=Frame(root,bg="black")
b=Button(f,text="1",font="sanfrancisco 35 bold",background="gray11",fg="white")
b.pack(side=LEFT,padx=10,pady=5)
b.bind("<Button-1>",click)
b=Button(f,text="2",font="sanfrancisco 35 bold",background="gray11",fg="white")
b.pack(side=LEFT,padx=10,pady=5)
b.bind("<Button-1>",click)
b=Button(f,text="3",font="sanfrancisco 35 bold",background="gray11",fg="white")
b.pack(side=LEFT,padx=10,pady=5)
b.bind("<Button-1>",click)
b=Button(f,text="+",font="sanfrancisco 35 bold",background="darkorange",fg="white")
b.pack(side=LEFT,padx=10,pady=5)
b.bind("<Button-1>",click)
f.pack()

f=Frame(root,bg="black")
b=Button(f,text="0",font="sanfrancisco 35 bold",background="gray11",fg="white",width=6)
b.pack(side=LEFT,padx=7,pady=5)
b.bind("<Button-1>",click)
b=Button(f,text=".",font="sanfrancisco 35 bold",background="gray11",fg="white")
b.pack(side=LEFT,padx=7,pady=5)
b.bind("<Button-1>",click)
b=Button(f,text="=",font="sanfrancisco 35 bold",background="darkorange",fg="white")
b.pack(side=LEFT,padx=7,pady=5)
b.bind("<Button-1>",click)
f.pack()
root.mainloop()