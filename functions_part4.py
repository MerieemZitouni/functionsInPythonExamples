def factorial_number (number) :
 if (number == 0):
    return(1)
 elif (number < 0):
    print("You can't enter a negative number ! ") 
 else  :
    for i in range((number - 1),0,-1) :
      number = number*i
    return(number)
n = int(input("enter a non negative integer : "))
print(factorial_number(n))
