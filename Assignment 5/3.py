#!/usr/bin/python3


import array
list=dict()
list["1"]=0
list["2"]=0
list["3"]=0
list["4"]=0
list["5"]=0
list["6"]=0
list["7"]=0
list["8"]=0
list["9"]=0
menu=dict()
menu["1"]="Chicken Strips"
menu["2"]="French Fries"
menu["3"]="Hamburger"
menu["4"]="Hotdog"
menu["5"]="Large Drink"
menu["6"]="Medium Drink"
menu["7"]="Milk Shake"
menu["8"]="Salad"
menu["9"]="Small Drink"

menu_=dict()
menu_["1"]=3.50
menu_["2"]=2.50
menu_["3"]=4.00
menu_["4"]=3.50
menu_["5"]=1.75
menu_["6"]=1.50
menu_["7"]=2.25
menu_["8"]=3.75
menu_["9"]=1.25


i=1
while i==1:
  print('\x1bc')
  print()
  print()
  print("1. Chicken Strips - $3.50\n2. French Fries - $2.50\n3. Hamburger - $4.00\n4. Hotdog - $3.50\n5. Large Drink - $1.75\n6. Medium Drink - $1.50\n7. Milk Shake - $2.25\n8. Salad - $3.75\n9. Small Drink - $1.25")
  print()
  print()
  order=input("PLease Enter your order sir : ")
  sum=0
  for i in order:
   list[i]+=1
  print()
  print("So,your order is : ")
  for i in list:
   if list[i]!=0:
      sum+=list[i]*menu_[i]
      print('\t'+(menu[i]+' '*20)[:20]," ->",list[i],"order")   
      list[i]=0   

  print()

  print("Total price : $"+str(sum))
  print()
  print()
  i=int(input("DO YOU WANT TO CONTINUE TO PLACE ORDERS (1 for YES  //  0 for NO)  : "))


