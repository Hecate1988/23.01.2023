import string
a = input("Введите строку")
for i in  range(0, len(string.punctuation)):
    a = a.replace(string.punctuation[i], '')
print(a)
hash_tag = a.split(' ')

for i in range(0, len(hash_tag)):
    hash_tag[i] = hash_tag[i].title()

print(hash_tag)
print('#' + "".join(hash_tag)[:140])