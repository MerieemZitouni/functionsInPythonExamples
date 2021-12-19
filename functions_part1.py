def palindrome (str) :
  conf = True 
  cnt1 = 1
  cnt2 = len(str)
  while ( (cnt1 != ((len(str)) // 2) + 1) and (cnt2 != ((len(str))- (len(str) // 2)  )) ) :
    if (str[cnt1 - 1] != str[cnt2 - 1]) : conf = False
    cnt1 = cnt1 + 1
    cnt2 = cnt2 - 1
  return (conf)