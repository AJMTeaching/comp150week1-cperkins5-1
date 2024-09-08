## Lab 1:

### Lab Exercise 1: Lists in Python

1. Create a list called my_list with the values [1, 5, 'apple', 20.5].
my_list = [1, 5,'apple', 20.5]
2. Using indexing, print the value 'apple' from my_list.
my_list.index('apple'):
return my_list_element['apple']
3. Add the value 10 to the end of my_list using the append() method. Print the updated list. 
my_list.append(10)
return my_list
4. Remove the value 20.5 from my_list using the remove() method. Print the updated list.
    if 20.5 in a lst:
        lst.remove(20.5)
    return lst
5. Reverse the order of the elements in my_list using a method. Print the reversed list.
    my_list.reverse(my_list[1, 5, 'apple', 20.5])
    return my_list_revered

### Lab Exercise 2: Dictionaries in Python

1. Create a dictionary called person with keys 'name', 'age', 'job' and values 'John', 30, 'teacher'.
key: ['name', 'age', 'job']
value: ['John', 30, 'teacher']
my_dict_person[key] = value

2. Print the value corresponding to the 'job' key.
try:
    return my_dict_person['job']
    except KeyError:
        return "Key not found"
3. Add a new key-value pair: 'city': 'Paris' to the person dictionary. Print the updated dictionary.
my_dict_person['city'] = 'Paris'
return my_dict_person

4. Remove the 'age' key-value pair from person. Print the updated dictionary.
if key in my_dict:
    del my_dict_person['age']
return my_dict_person
5. Iterate through the person dictionary and print out each key-value pair on a separate line.
for key, value in my_dict.items():
print(f"Key: {keys}, Value: {value}")
