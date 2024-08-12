immutable_var = 1, 2, 'a', 'b'
print(immutable_var)
immutable_var[1] = 3
print(immutable_var)
#кортеж не поддерживает обращение по элементам.
mutable_list = [1, 2, 'a', 'b', 'Modified']
mutable_list[0] = 2
print(mutable_list)