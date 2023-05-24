list_whole_numbers = [0, 1, 2, 3, 4, 5]  # lists are ordered, changeable
wn_squared = list(map(lambda x: x ** 2, list_whole_numbers))  # ensures iterable is converted to a list
print(wn_squared)

tuple_natural_numbers = (1, 2, 3, 4, 5, 6, 7)  # tuples are ordered, unchangeable
tuple_nn_squared = tuple(map(lambda x: x ** 2, tuple_natural_numbers))
# tuple_nn_squared[0] = 5 # this should not work as tuples are immutable
print(tuple_nn_squared)
