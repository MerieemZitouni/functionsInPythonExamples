def factorial_number (number) :
 if (number == 0): return(1)
 elif (number < 0): print("You can't enter a negative number ! ") 
 else  :
    i = number - 1
    while (i != 0) : 
      number = number*i
      i = i - 1
    return(number)
n = int(input("enter a non negative integer : "))
print(factorial_number(n))