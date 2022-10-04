
# ******************************
# Make your Code
# ******************************

x=[]
maxlen=""
minlen="00000000000000000000000000000000000"
inp=input("String?")
while inp!="STOP" and inp!="stop":
  x+=[inp]
  if len(inp)>=len(maxlen):
      maxlen=inp
  if len(inp)<=len(minlen):
      minlen=inp
  inp=input("String?")
  while inp!="STOP" and inp!="stop":
    if len(inp)>=len(maxlen):
      maxlen=inp
      break
    if len(inp)<=len(minlen):
      minlen=inp
      break
  if inp=="stop" or inp=="STOP":
    break
print(maxlen+" "+minlen)
# Requirement
# No need to use list
# All input values are taken one by one separatively.
###
