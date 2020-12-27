不同排序算法的总结： 
1.	选择排序：  
def selectSort(arr):  
        minVal = arr[0]
        for i in range(len(arr) - 1):  
            minIndex = I  
            for j in range(i + 1, len(arr)):  
                if arr[j] < arr[minIndex]:  
                    minIndex = j  
            temp = arr[i]  
            arr[i] = arr[minIndex]  
            arr[minIndex] = temp  
        return arr  
  
2.	插入排序  
def insertSort(arr):  
      for i in range(1, len(arr)):  
          preIndex = i – 1  
          current = arr[i]  
          while preIndex >= 0 and arr[preIndex] > current:  
              arr[preIndex + 1] = arr[preIndex]  
              preIndex -= 1  
          arr[preIndex + 1] = current  
      return arr

3.	冒泡排序  
def bubbleSort(arr):  
      for i in range(len(arr) - 1):  
          for j in range(i + 1, len(arr)):  
              if arr[i] > arr[j]:  
                  arr[i], arr[j] = arr[j], arr[i]  
      return arr  

4.	快速排序  
def partition(arr, begin, end):  
      pivot = end  
      counter = begin  
      for i in range(begin, end):  
          if arr[i] < arr[pivot]:  
              arr[counter], arr[i] = arr[i], arr[counter]  
              counter += 1  
      arr[pivot], arr[counter] = arr[counter], arr[pivot]  
      return counter  
  
  
  def quickSort(arr, begin, end):  
      if end <= begin:  
          return  
      pivot = partition(arr, begin, end)  
      quickSort(arr, begin, pivot - 1)  
      quickSort(arr, pivot + 1, end)  

5.	归并排序  
def merge(array, left, mid, right):  
      temp = [0] * (right - left + 1)  
      i = left
      j = mid + 1
      k = 0
      while i <= mid and j <= right:  
          if array[i] <= array[j]:  
              temp[k] = array[i]  
              k += 1  
              i += 1  
          else:
              temp[k] = array[j]  
              k += 1  
              j += 1  
      while i <= mid:
          temp[k] = array[i]  
          k += 1  
          i += 1  
      while j <= right:  
          temp[k] = array[j]  
          k += 1  
          j += 1  
      for p in range(len(temp)):  
          array[left + p] = temp[p]  
  
  
  def mergeSort(array, left, right):  
      if right <= left:  
          return  
      mid = (left + right) >> 1  
      mergeSort(array, left, mid)  
      mergeSort(array, mid + 1, right)  
      merge(array, left, mid, right)  
      return array  


  
