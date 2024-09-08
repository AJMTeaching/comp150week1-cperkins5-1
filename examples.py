from main import merge_lists


a = [22,33,43,55,70]
# printing each number in a list on a new line.
for number in a:
    print(number)


# add a\\ all numbers in the list together
print("add a\\ the numbers in the list together")
sum = 0
for number in a:
    sum = sum + number
    print(f"the sum in the middle of the processing is: {sum}")
    print(sum)

# only return the odd numbers in my list
print("only the odd numbers")
for number in a:
    if number %2 == 1:
        print(f"I found an odd number! which is (number)")
        odd_numbers.append(number)
        print(odd_numbers)

# merge two sorted list into one list
def test_merge_list():
    list1 = [1,3,5]
    list2 = [2,4,6]
    merged = merge_lists(list1, list2)
    for element in list1:
        print(list1.append([list2]))
    return merge_lists(list1, list2)

