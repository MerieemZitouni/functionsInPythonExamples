def max_three_numbers (n1 , n2 , n3): 
    if (n1 > n2 > n3): maximum = n1
    if (n1 > n3 > n2): maximum = n1
    if (n2 > n3 > n1): maximum = n2 
    if (n2 > n1 > n3): maximum = n2
    if (n3 > n2 > n1): maximum = n3 
    if (n3 > n1 > n2): maximum = n3
    return maximum
a = int(input("enter a : "))
b = int(input("enter b : "))
c  = int(input("enter c : "))
print(max_three_numbers(a,b,c))