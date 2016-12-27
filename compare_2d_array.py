# input --> arr1 has length n , arr2 has length m
# output --> person who displays in both arr1 and arr2

#test case:
# [1,2,3,4]
#[2,4,5,6]
#[2,4]


#[1,2,2,3,4]
#[1,3,3,5]
#[1, 3]

def compare_numbers(arr1, arr2):
   duplicate_ssn = []
   for i in arr1:
      for num in arr2:
         if i == num:
            duplicate_ssn.append(i)
   return duplicate_ssn
            
def compare_again(arr1, arr2):
#    compare_ssn = 
   count_dict = {}
   compare_ssn = []
   arr3 = arr1 + arr2
   #[1,2,3,4,2,4,5,6]
   arr3.sorted()
   #[1,2,2,3,4,4,5,6]
   for num in arr3:
      count_dict[num] = count_dict.get(num, 0) + 1
      # {1:1, 2:2, 3:1, 4:2, 5:1, 6:1}
   
   for key, value in count_dict:
      if value > 1:
         compare_ssn.append(key)
         
   return compare_ssn
         
# arr1 = [1,2,3,4,10] length n
# arr2 = [1,5,6,7,8,9,10] length m
# check to see if value at array1 index 0 is greater than/less than/ or equal to value at array2 index 0 
def one_more_time(arr1, arr2):
   
   # index for arr1
   i = 0
   
   # index for arr2
   j = 0
   
   # duplicates to return
   append_list = []
   
   # while we haven't fallen off the end of either
   while i < len(arr1) and j < len(arr2):
      if arr1[i] < arr2[j]:
         i += 1
      elif arr1[i] > arr2[j]:
         j += 1
      else:
         append_list.append(arr1[i])
         j += 1
         i += 1
      
one_more_time(arr1, arr2)
one_more_time(arr2, arr1)
         
      
      