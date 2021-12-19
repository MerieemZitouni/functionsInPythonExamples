def reverse_string (str):
    ch = str[len(str) - 1]
    outp = ''
    i = 1
    while (i != len(str) + 1 ) :
      outp = outp + ch
      i = i + 1
      ch =  str[len(str) - i] 
    return(outp)
c  = input("enter a string : ")
print(reverse_string(c))