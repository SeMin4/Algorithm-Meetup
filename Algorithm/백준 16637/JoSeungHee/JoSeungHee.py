N=int(input())
expression = list(input())

operator=[]
operand= []

def cal(num1, num2, op):

  if op =='+':
    return num1+num2
  elif op=='-':
    return num1-num2
  elif op =='*':
    return num1*num2
    
for i in expression:
  if i =='+' or '-' or '*':
    operator.append(i)
  else:
    operand.append(i)

def dfs():

