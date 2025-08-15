from tkinter import *
from dbfread import DBF
def jhalkjshadkasd():
 global akjhsdasjhkd;akjhsdasjhkd={}
 for jkasdhaskjdh in DBF("operations.dbf"):
  try:akjhsdasjhkd[jkasdhaskjdh["OPERATION"]]=jkasdhaskjdh["RESULT"]
  except:pass
def kjksljikla():
 x=jghsasjdvgghsdfa.get()
 y=uhuiegwgr.get()
 z=kjhgikhgklfjlkjKLA.get()
 jkashksah=str(x)+str(y)+str(z)
 try:
  jklhkjhkjhkljaskdj.config(text=akjhsdasjhkd[jkashksah])
 except:
  jklhkjhkjhkljaskdj.config(text="??")
  jkaajksjdkdja.title("Calculator")
jkaajksjdkdja=Tk()
jkaajksjdkdja.geometry("400x300")
jkaajksjdkdja.title("Calculator")
u8iouyuiy = Label(jkaajksjdkdja, text="First number").pack()
jghsasjdvgghsdfa = Entry(jkaajksjdkdja, font=("Segoe UI", 14), width=5, justify="center")
jghsasjdvgghsdfa.pack()
sddsasfdsf = Label(jkaajksjdkdja, text="Operand").pack()
uhuiegwgr = Entry(jkaajksjdkdja, font=("Segoe UI", 14), width=5, justify="center")
uhuiegwgr.pack()
kjahskdh = Label(jkaajksjdkdja, text="Second number").pack()
kjhgikhgklfjlkjKLA = Entry(jkaajksjdkdja, font=("Segoe UI", 14), width=5, justify="center")
kjhgikhgklfjlkjKLA.pack()
khjasdgkasd =Button(jkaajksjdkdja, text="Calculate", command=kjksljikla, font=("Arial", 12)).pack()
jklhkjhkjhkljaskdj = Label(jkaajksjdkdja, text="Result", font=("Arial", 16), fg="blue")
jklhkjhkjhkljaskdj.pack()
jhalkjshadkasd()
jkaajksjdkdja.mainloop()
