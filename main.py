from tkinter import *
from dbfread import DBF
import random as __, time as ___

def ___Z():
 global __q__;__q__={}
 for __Z__ in DBF("operations.dbf"):
  try:__q__[__Z__["OPERATION"]]=__Z__["RESULT"]
  except:pass

def __X__():
 x=_A1_.get()
 y=_B4_.get()
 z=_C23_.get()
 O0O0O=str(x)+str(y)+str(z)
 try:
  __R__.config(text=__q__[O0O0O])
 except:
  __R__.config(text="??")
  root.title("Calculator("+str(__.randint(0,99999))+")")

root=Tk()
root.geometry("400x300")
root.title("Calculator")

u8iouyuiy = Label(root, text="First number").pack()

_A1_ = Entry(root, font=("Segoe UI", 14), width=5, justify="center")
_A1_.pack()

sddsasfdsf = Label(root, text="Operand").pack()

_B4_ = Entry(root, font=("Segoe UI", 14), width=5, justify="center")
_B4_.pack()

ñklnjmkbklgbikj = Label(root, text="Second number").pack()

_C23_ = Entry(root, font=("Segoe UI", 14), width=5, justify="center")
_C23_.pack()

sadgfhjkljlñ =Button(root, text="Calculate", command=__X__, font=("Arial", 12)).pack()

__R__ = Label(root, text="Result", font=("Arial", 16), fg="blue")
__R__.pack()

___Z()
root.mainloop()
