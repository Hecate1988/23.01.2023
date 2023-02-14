def find_unique_value(list):
   a = list[0]
   if(list.count(a) == 1):
       return a

   for i in list:
       if(a != i):
           return i


print(find_unique_value([1, 2, 1, 1]))
print(find_unique_value([2, 3, 3, 3]))
print(find_unique_value([5, 5, 5, 0.5]))

assert find_unique_value([1, 2, 1, 1]) == 2, 'Test1'
assert find_unique_value([2, 3, 3, 3]) == 2, 'Test2'
assert find_unique_value([5, 5, 5, 0.5]) == 0.5, 'Test3'
print("ОК")