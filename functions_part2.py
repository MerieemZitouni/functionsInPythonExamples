def prime_nb (number) :
 if (number > 0 ) :
   i = 2 
   verif = True
   for i in range(2,(number // 2)) :
      if ((number % i) == 0) : 
        verif = False
   return (verif)
 else :
   return(False)
n = int (input ("enter a number : "))
print(prime_nb(n))
