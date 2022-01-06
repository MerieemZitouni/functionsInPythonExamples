def number_in_range (number,start_lim,end_lim) : 
    verif = False 
    if (start_lim <= number <= end_lim) : 
        verif = True
    return(verif)
n = int(input("enter an integer : "))
a = int(input("enter a : "))
b = int (input("enter b (b<a) : "))
print(number_in_range(n,a,b))
