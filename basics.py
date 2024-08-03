# Learning the concepts from chatGPT 4o
"""
print("Hello, World!")

x = 5
y = 8

## Comparison operations
print("x == y:", x == y)
print("x != y:", x != y)
print("x > y:", x > y)
print("x < y:", x < y)
print("x >= y:", x >= y)
print("x <= y:", x <= y)

## List
numbers = [1,5,4,3,2]
number = 12,43
print(numbers)

## while
count = 0
while count < 5:
    count += 1
    print(count)
print("count outside = ",count)

## function
def firstFunc (name, age):
    return f"Hello {name} this is your {age} age"

result = firstFunc("kavi", "25")
print(result)

## advanced functions

def greet(greeting,name="marley"):
    return f"{greeting}, {name}!"

print(greet(greeting="alas!"))          # Uses default greeting
print(greet(name="Bob",greeting="Hi"))      # Uses provided greeting

def print_numbers(*args):
    for number in args:
        print(number)
print_numbers(1,3,4,60,"data")

def print_info(**kwargs):
    for key,value in kwargs.items():
         # print(f"Key = {key} / Value = {value}")
         print(f"{key}={value}")
print_info(name="kavi", age=27.0)


## Lambda functions
data = 1,55,6
list_data = list(data)
print(f"Tuple data = {data}")
print (f"List data = {list_data}")
print (f"List data = {list(data)}")
# -----------------------------------------------#

## Function to square a number
def square(x):
    return x * x

# List of numbers
numbers = [1, 2, 3, 4, 5]

# Apply the function to each item in the list
squared_numbers = map(square, numbers)

# Convert the result to a list and print it
print(list(squared_numbers))  # Output: [1, 4, 9, 16, 25]
print(squared_numbers)

# -----------------------------------------------#

# List of numbers
numbers = (5, 3, 8, 1, 2)

# Sort the list
sorted_numbers = sorted(numbers)

print(sorted_numbers)  # Output: [1, 2, 3, 5, 8]

# -----------------------------------------------#
## list, map, sorted, lambda

# List of tuples
pairs = [(1, 'one'), (3, 'three'), (2, 'two')]

# Sort by the first item in each tuple
sorted_pairs_first = sorted(pairs, key=lambda pair: pair[0])
sorted_pairs_second = sorted(pairs, key=lambda pair: pair[1])

print(sorted_pairs_first)  # Output: [(1, 'one'), (2, 'two'), (3, 'three')]
print(sorted_pairs_second)
# -----------------------------------------------#

"""

number_tuple = [1,2,4] # immutable
number_list = (1,2,3) # mutable
number_set = { 1,3,4} # set: unordered collection unique elements

## Dictionary: unordered collections of key-value pairs
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
print(person)
print(person["name"])
