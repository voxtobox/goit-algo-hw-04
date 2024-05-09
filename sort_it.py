def sort_insertion(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

def merge_arr(left, right):
    leftIn = 0
    rightIn = 0
    res = []
    
    while leftIn < len(left) and rightIn < len(right):
      if left[leftIn] < right[rightIn]:
        res.append(left[leftIn])
        leftIn += 1
      else:
        res.append(right[rightIn])
        rightIn += 1
    
    while leftIn < len(left):
      res.append(left[leftIn])
      leftIn += 1
      
    while rightIn < len(right):
      res.append(right[rightIn])
      rightIn += 1
    
    return res

def sort_merge(arr):
  n = len(arr)
  if (n <= 1):
    return arr
  mid = n // 2
  left_half = arr[:mid]
  right_half = arr[mid:]
  
  return merge_arr(sort_merge(left_half), sort_merge(right_half))