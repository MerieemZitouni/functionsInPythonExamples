def prime_nb (number) :
 if (number > 0 ) :
   i = 2 
   verif = True
   while (i <= ((number // 2))) :
      if ((number % i) == 0) : 
        verif = False
      i = i + 1 
   return (verif)
 else :
   return(False)
n = int (input ("enter a number : "))
print(prime_nb(n))
