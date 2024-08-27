
print("Welcome to Python Deliveries!")
price=0;
size = input("What size pizza do you want? S, M or L : ")
if size == "S":
  price=15
  pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
  if pepperoni == "Y":
    price+=2
  elif pepperoni == "N":
    price+=0;
elif size == "M":
  price=20
  pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
  if pepperoni == "Y":
    price+=3
  elif pepperoni == "N":
    price+=0;
elif size == "L":
  price=25
  pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
  if pepperoni == "Y":
    price+=3
  elif pepperoni == "N":
    price+=0;
else :
  print("You are type the wrong input")
  
extra_cheese = input("Do you want extra cheese? Y or N: ")
if extra_cheese == "Y":
  price+=1
elif extra_cheese == "N":
  price+=0;

print(f"Your final bill is :$ {price}.")
