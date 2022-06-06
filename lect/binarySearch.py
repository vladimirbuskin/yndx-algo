import bisect
ar = [1,2,3,4,5,6,7,8,9,10]
#ar = [1,2,2,2,5,6,7,8,9,10]
ar = [10,9,8,7,6,5,4,3,2,1]


def binarySearch(ar, x, left, right):
  # exit
  if left >= right:
    return -1
  
  # med
  med = (right + left) // 2
  print("left=%s right=%s med=%s" % (left, right, med))

  # found
  if ar[med] == x:
    return med
  # [left, med)
  elif x < ar[med]:
    return binarySearch(ar, x, left, med)
  # [med, right)
  else:
    return binarySearch(ar, x, med+1, right)

# print(10 + 5 // 2)

def binarySearchTop(ar, x):
  #return bisect.bisect_left(ar, x)
  return binarySearch(ar, x, 0, len(ar))

print(binarySearchTop(ar, 10))