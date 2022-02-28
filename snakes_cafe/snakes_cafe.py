def cafe():
 print(   """
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************

Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears


***********************************
** What would you like to order? **
***********************************
    """)
 order=''
 c=0
 allorders=[]
 while order!="quit":
     order=input()
     if order=="quit":
         break
     allorders.append(order)
     c+=1
     print(f"** {allorders.count(order)} order of {order} have been added to your meal **")
      
cafe()