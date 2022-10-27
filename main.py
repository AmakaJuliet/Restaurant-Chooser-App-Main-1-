name= input('Enter your name')
age= input('Enter your age')
age= int(age)

if age < 15:
   print("Hello {} you are less than 15 years old and we     currently do not have kids & teens retaurant options".   format (name)) 
cash= input('Enter the amount of money you have')
cash= int(cash)

if cash <= 10:
   print("Hello {} We recommend Pizza Hut".format (name))
elif cash >= 100 and cash <=250:
     print("Hello {} We recommend Xhi Chinese Restaurant".     format (name))
elif cash >= 300 and cash <=600:
     print("Hello {} We recommend Tiana\'s Deluxe Lounge".     format (name))
else :
    print("Hello {} We do not have anyrecommendations at the moment". format(name))