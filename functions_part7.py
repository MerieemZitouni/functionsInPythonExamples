def max_of_two( n1, n2 ):
    if n1 > n2:
        return n1
    return n2
def max_of_three( n1, n2, n3 ):
    return max_of_two( n1, max_of_two( n2, n3 ) )
a = int(input("enter a : "))
b = int(input("enter b : "))
c  = int(input("enter c : "))
print(max_of_three(a,b,c))
