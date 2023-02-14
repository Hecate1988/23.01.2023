def add_one(x):
y = (int(''.join(map(str, x)))) + 1

z = [int(a) for a in str(y)]

print(z)


add_one([1, 2, 3, 4])
add_one([9, 9, 9, 9])
add_one([0])
add_one([9])

#assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
#assert add_one([9, 9, 9, 9]) == [1, 0, 0, 0, 0], 'Test2'
#assert add_one([0]) == [1], 'Test3'
#assert add_one([9]) == [1, 0], 'Test4'
print("ОК")