def add_one(nums):
    if __name__ == '__main__':
        s = ''.join(str(x) for x in nums)
    str1 = str(int(s) + 1)
    if __name__ == '__main__':
      return list(map(int, str1))

print(add_one([1, 2, 3, 4]))
print(add_one([9, 9, 9, 9]))
print(add_one([0]))
print(add_one([9]))

assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
assert add_one([9, 9, 9, 9]) == [1, 0, 0, 0, 0], 'Test2'
assert add_one([0]) == [1], 'Test3'
assert add_one([9]) == [1, 0], 'Test4'
print("ОК")