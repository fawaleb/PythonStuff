from typing import Set

list_of_numbers = [1, 1, 3, 4, 6, 6, 10, 11, 11, 14]
s = {'blueberry', 'raspberry', 'apple'}

print(s)

s.add('strawberry')
print(s)
s.add('blueberry')
print(s)
print(list_of_numbers)
list_of_numbers = list(set(list_of_numbers))
print(list_of_numbers)

library1 = {'Harry Potter', 'Hunger Games', 'Lord of the Rings'}
library2 = {'Harry Potter', 'Romeo and Juliet'}

at_both_libraries: Set[str] = library1.intersection(library2)

all_books_in_town: Set[str] = library1.union(library2)
print(all_books_in_town)
print(at_both_libraries)
