"""
Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which the letters occur in alphabetical order. For example, if s = 'azcbobobegghakl', then your program should print

Longest substring in alphabetical order is: beggh
In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print

Longest substring in alphabetical order is: abc

"""

store_data = ''
current_char = ''
longest_string = ''
for char in s:
    if char >= current_char:
        store_data = store_data + char
    else:
        store_data = '' #clear list if not in order
        store_data = char
    current_char = char
    if len(store_data) > len(longest_string):
        longest_string = store_data

print("Longest substring in alphabetical order is:", longest_string)
