import art 
from replit import clear
print(art.logo)

def dosomething(n1,n2,operation):
  if operation == "+":
    result = n1+n2
    print(f"{n1} + {n2} = {result}")
    return result
  elif operation == "-":
    result = n1-n2
    print(f"{n1} - {n2} = {result}")
    return result
  elif operation == "*":
    result = n1*n2
    print(f"{n1} * {n2} = {result}")
    return result
  elif operation == "/":
    result = n1/n2
    print(f"{n1} / {n2} = {result}")
    return result

def my_function():
  done = 'y'
  n1 = float(input("whats the first number?\n"))
  while done =='y':
    operation = input("from +,-,*,/ pick one operation.\n")
    n2 = float(input("whats the second number?\n"))
    res = dosomething(n1,n2,operation) 
    done = input(f"Type 'y' to continue calculating with {res}, or type 'n' to start a new calculation:")
    n1 = res
  clear()
  my_function()
    

my_function()

  
