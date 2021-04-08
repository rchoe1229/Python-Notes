print("Hello World")
# output => Hello World

d = {"k1": {"innerkey": [1, 2, 3]}}
print(d["k1"]["innerkey"])
# output => [1, 2, 3]

# Boolean
True or False

# Array
my_list = [1, 2, 3]

# Tuples -  Similar to array, but uses parenthesis and is IMMUTABLE
my_list = (1, 2, 3)

# Set - Similar to dictionary, but only contains unique elements
print({1, 1, 1, 2, 2, 3, 4, 5, 6})
# output => {1,2,3,4,5,6}

# Comparison Operators
print(1 >= 2)
print(1 <= 2)
print(1 == 2)
print(1 == 1)
print(1 == 1 and 2 < 3)
print(1 == 1 or 2 > 3)

# If Elif Else
if 1 < 2:
  print('Hell Yeah!')

if 1 == 2:
  print('This is broken')
elif 3 == 3:
  print('Threes!')
else:
  print('correct')
# output => Hell Yeah! and Threes! 
# Hell Yeah! is true because 1 is less than 2, so would print the string under. 
# Threes! is true because 1 != 2, so the next condition is if 3 == 3, which is true. This prints the string underneath

# For Loops

sequence = [1,2,3,4,5]

for num in sequence:
  print(num)
# output => 1
# output => 2
# output => 3
# output => 4
# output => 5

# While Loops

i = 1
while i < 5:
  print('i is:{}'.format(i))
  i = i + 1
# output => i is: 1
# output => i is: 2
# output => i is: 3
# output => i is: 4

#  Range
for num in range(0,5):
  print(num)
# output => 0
# output => 1
# output => 2
# output => 3
# output => 4
print(list(range(10)))
# output => [0,1,2,3,4,5,6,7,8,9]

# List Comprehension(First example is with a for loop and second is list comprehension, both do the same)
x = [1,2,3,4]
out = []
for num in x:
  out.append(num**2)
print(out)
# output => [1,4,9,16]
print([num**2 for num in x])
# output => [1,4,9,16]
