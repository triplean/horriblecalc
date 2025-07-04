import dbf
t=dbf.Table("operations.dbf",'operation C(20);result C(20)')
t.open(mode=dbf.READ_WRITE)
O="+-* /"
def f(x,y,o):
 try:
  if o=="+":r=str(int(x)+int(y))
  elif o=="-":r=str(int(x)-int(y))
  elif o=="*":r=str(int(x)*int(y))
  elif o=="/":r=str(int(int(x)/int(y))) if int(y)!=0 else "ERR"
  else:r="ERR"
 except:r="ERR"
 return r

a=1
b=1
while True:
 for c in O:
  op=str(a)+c+str(b)
  res=f(a,b,c)
  print("APPENDING:", op, "=>", res)
  try: t.append((op,res))
  except Exception as e: print("ERROR APPENDING", op, ":", e)
 b+=1
 if b>999: b=1; a+=1
 if a>999: a=1
