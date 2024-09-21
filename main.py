# ------------------------------------------------------------------------

# Lab 1
# Problem 1: Create a list called my_list
my_list = [1, 5, 'apple', 20.5]
print(my_list[0])
# Problem 2: Using index, print element 'apple' from my_list
for apple in my_list:
    print(my_list.index(apple))
# Tuesday: ask exactly how to print just 'apple' back.
# Problem 3: Add 10 value to the end of my_list
my_list.append(10)
print(my_list)
# Problem 4: Remove 20.5 from my_list using remove()
if 20.5 in my_list:
        my_list.remove(20.5)
print(my_list)
# Problem 5: Reverse the element order in my_list
list.reverse(my_list)
print(my_list)

# Lab 1 part 2:
# Problem 1
person = [{}]
key: {('name', 'age', 'job')}
value: {('John', 30, 'teacher')}
person = [{'name':'John', 'age':30, 'job':'teacher'}]

# Problem 2 
try:
    print(person,{'job'})
except KeyError:
    print("Key not found")
# Problem 3     
#person['city'] = 'Paris'
print(person)
# Problem 4
#for key in person:
#    del person['age']
#print(person)
# Problem 5
#for key, value in person.items():
#   print(f"key: {key}, value: {value}")
pass
# -----------------------------------------------------------------------------


# Importing sys for test function
from audioop import add
import sys


# Custom Test Function
def test(did_pass):
    """ Print the result of a test. """
    linenum = sys._getframe(1).f_lineno  # Get the caller's line number.
    msg = f"Test at line {linenum} {'PASSED' if did_pass else 'FAILED'}."
    print(msg)


# Function 1: count_vowels
def count_vowels(s: str) -> int:
    """
    Count the number of vowels in a string.

    Parameters:
    - s (str): The input string

    Returns:
    - int: The number of vowels in the string
    """
    # TODO: Implement this function
    pass


    # vowels: ['a','e','i','o','u','A','E','I','O','U']
    vowels: str = "aeiouAEIOU"
    vowel_count: int = 0
    for letter in s:
        if letter in vowels:
            vowel_count += 1
    return vowel_count
    

# Unit Tests for count_vowels
def test_count_vowels():
    test(count_vowels("hello") == 2)
    test(count_vowels("why") == 0)
    test(count_vowels("aeiou") == 5)
    test(count_vowels("") == 0)
    test(count_vowels("bcdfg") == 0)
    test(count_vowels("aeiouAEIOU") == 10)
    test(count_vowels("HELLO") == 2)
    test(count_vowels("aEiOu") == 5)
    test(count_vowels("a e i o u") == 5)
    test(count_vowels("rhythm") == 0)


# Function 2: merge_lists
def merged_lists(list1: list, list2: list) -> list:
    """
    Merge two sorted lists into a single sorted list.

    Parameters:
    - list1 (list): The first sorted list
    - list2 (list): The second sorted list

    Returns:
    - list: A new sorted list containing all elements from list1 and list2
    """
    # TODO: Implement this function
    pass

# CANNOT use 'sorted()' 'sort()' 'list.extend()' 'list concatentation(+)'
    if len(list1) == 0:
        return list2
    if len(list2) == 0:
        return list1
    while len(merged_lists) != (''):
        if not list1:
            return add_remaining_items_to_merged_list(list2)
        if not list2:
            return add_remaining_items_to_merged_list(list1)
        merged_lists.append(list1[list2])
        if index1 + 1 == len(list1):
            return add_remaining_items_to_merged_list(list2)
        else:
            index1 += 1
    else:
        merged_lists.append(list2[index2])
        if index2 + 1 == len(list2):
            return add_remaining_items_to_merged_list(list1)
        else:
            index2 += 1
    return merged_lists
    pass
        
    
# Unit Tests for merge_lists
def test_merge_lists():
    list1 = [1, 3, 5]
    list2 = [2, 4, 6]
    merged = merged_lists(list1, list2)
    test(merged == [1, 2, 3, 4, 5, 6])
    test(merged_lists([], []) == [])
    test(merged_lists([1], [2]) == [1, 2])
    test(merged_lists([1, 1], [2, 2]) == [1, 1, 2, 2])
    test(merged_lists([1, 3, 5], []) == [1, 3, 5])
    test(merged_lists([], [2, 4, 6]) == [2, 4, 6])
    test(merged_lists([1, 2, 3], [4, 5, 6]) == [1, 2, 3, 4, 5, 6])
    test(merged_lists([1, 3, 5, 7, 9], [2, 4, 6, 8, 10]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    test(merged_lists([1, 1, 2, 3], [1, 2, 2, 3]) == [1, 1, 1, 2, 2, 2, 3, 3])


# Function 3: word_lengths
def word_lengths(words: list) -> list:
    """
    Get the lengths of words in a list.

    Parameters:
    - words (list): The list of words

    Returns:
    - list: A list containing the lengths of the words
    """
    # TODO: Implement this function
    pass
# words = []
# lengths = word_lengths(words)

    word_lengths: list = []
    for word in words:
        word_lengths.append(len(word))
    return word_lengths


# Unit Tests for word_lengths
def test_word_lengths():
    words = ["hello", "world", "python"]
    lengths = word_lengths(words)
    test(lengths == [5, 5, 6])
    test(word_lengths([]) == [])
    test(word_lengths(["word"]) == [4])
    test(word_lengths(["short", "mediummm", "longesttttt"]) == [5, 8, 11])
    test(word_lengths(["", "a", "ab", "abc"]) == [0, 1, 2, 3])
    test(word_lengths(["  ", "a b", " c "]) == [2, 3, 3])


# Function 4: reverse_string
def reverse_string(s: str) -> str:
    """
    Reverse a string.

    Parameters:
    - s (str): The input string

    Returns:
    - str: The reversed string
    """
    # TODO: Implement this function
    pass
    s = str
    text = []
    for text in str:
        reverse_string(text)
    return s[::-1]


# Unit Tests for reverse_string
def test_reverse_string():
    text = "python"
    reversed_text = reverse_string(text)
    test(reversed_text == "nohtyp")
    test(reverse_string("") == "")
    test(reverse_string("a") == "a")
    test(reverse_string("aaa") == "aaa")
    test(reverse_string("Hello, World!") == "!dlroW ,olleH")
    test(reverse_string("12345") == "54321")
    test(reverse_string("  spaces  ") == "  secaps  ")


# Function 5: intersection
def intersection(list1: list, list2: list) -> list:
    """
    Find the intersection of two lists.

    Parameters:
    - list1 (list): The first list
    - list2 (list): The second list

    Returns:
    - list: The intersection of the two lists
    """
    # TODO: Implement this function
    pass

    inter_list = []
    for i in list1:
        if i in list2:
            inter_list
    return inter_list

# Unit Tests for intersection
def test_intersection():
    list1 = [1, 2, 3, 4]
    list2 = [3, 4, 5, 6]
    result = intersection(list1, list2)
    test(result == [3, 4])
    test(intersection([], []) == [])
    test(intersection([1, 2], [3, 4]) == [])
    test(intersection([1, 2], [1, 2]) == [1, 2])
    test(intersection([1, 2, 2, 3], [2, 2, 3, 4]) == [2, 3])
    test(intersection([1, 2, 3], [4, 5, 6]) == [])
    test(intersection([1, 2, 3], [1, 2, 3]) == [1, 2, 3])


# Test Suite
def test_suite():
    print(f"Count Vowels Test Results:")
    test_count_vowels()
    print(f"Merge Lists Test Results:")
    test_merge_lists()
    print(f"Word Lengths Test Results:")
    test_word_lengths()
    print(f"Reverse String Test Results:")
    test_reverse_string()
    print(f"Intersection Test Results:")
    test_intersection()


test_suite()