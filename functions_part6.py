def sum_list(list):
    sum = 0
    j = 0
    for i in list :
      sum = sum + list[j]
      j = j + 1
    return sum
print(sum_list([4,87,10,9]))