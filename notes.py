
#! Displaying information w/ print
print("Hello World")
# output => Hello World

#! Dictionary and indexing
d = {"k1": {"innerkey": [1, 2, 3]}}
print(d["k1"]["innerkey"])
# output => [1, 2, 3]

#! Boolean
True or False

#! Array
my_list = [1, 2, 3]

#! Indexing
my_string = ['a','b','c','d','e','f','g','h','i','j','k']
print(my_string[3])
# output => d
print(my_string[:3])
# output => ['a','b','c']
print(my_string[3:])
# output => ['d','e','f','g','h','i','j','k']
print(my_string[::3])
# output => ['a','d','g','j']
print(my_string[::-1])
# output => ['k', 'j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a']

#! Tuples -  Similar to array, but uses parenthesis and is IMMUTABLE
my_list = (1, 2, 3)

#! Set - Similar to dictionary, but only contains unique elements
print({1, 1, 1, 2, 2, 3, 4, 5, 6})
# output => {1,2,3,4,5,6}

#! Comparison Operators
print(1 >= 2)
print(1 <= 2)
print(1 == 2)
print(1 == 1)
print(1 == 1 and 2 < 3)
print(1 == 1 or 2 > 3)

#! If Elif Else
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

#! For Loops
sequence = [1,2,3,4,5]
for num in sequence:
  print(num)
# output => 1
# output => 2
# output => 3
# output => 4
# output => 5

#! While Loops
i = 1
while i < 5:
  print('i is:{}'.format(i))
  i = i + 1
# output => i is: 1
# output => i is: 2
# output => i is: 3
# output => i is: 4

#! Range
for num in range(0,5):
  print(num)
# output => 0
# output => 1
# output => 2
# output => 3
# output => 4
print(list(range(10)))
# output => [0,1,2,3,4,5,6,7,8,9]

#! List Comprehension (First example is with a for loop and second is list comprehension, both do the same)
x = [1,2,3,4]
out = []
for num in x:
  out.append(num**2)
print(out)
# output => [1,4,9,16]
print([num**2 for num in x])
# output => [1,4,9,16]
"""
List comprehension basically took the for loop and logically did it backwards
Every number in our x array will be squared is how line 84 is read
"""

#! Functions (names should be lower case, functions also take in parameter/s)
def my_func(name):
  print('Hello ' + name)

my_func('Chad')
# output => Hello Chad

def square(num):
  return num**2

output = square(2)
print(output)
# output => 4

score = [1,2,3,4,5]

def print_score():
  return score

print(print_score())
# output => [1,2,3,4,5]

# just a little for loop so you dont forget ;)
for num in score:
  print(num)
# output => 1
# output => 2
# output => 3
# output => 4
# output => 5

#! Map/Filter and Lamda Expressions
def times2(var):
  return var*2
""" 
The above function can be rewritten as a lambda expression,
or also known as an anonymous function. Below will show you the
iterpretation of a lamda expression
"""
t = lambda var:var*2

print(times2(5))

my_list = [1,2,3,4,5]
print(
  list(map(times2, my_list))
  )
# output => [2, 4, 6, 8, 10]

# map w/ lambda expression
my_list = [1,2,3,4,5]
print(
  list(map(lambda num: num*3, my_list))
  )
# output => [3, 6, 9, 12, 15]

# filter
print(
  list(filter(lambda num: num%2 == 0, my_list))
)
# output => [2, 4] this filter showed only values that were truthful and returned only even values

#! Other calls
s = 'hello my name is Ryan'
print(s.lower())
# output => hello my name is ryan
print(s.upper())
# output => HELLO MY NAME IS RYAN
print(s.split())
# output => ['hello', 'my', 'name', 'is', 'Ryan']
print(my_list.pop())
# output => 5
print(my_list)
# output => [1, 2, 3, 4]
my_list.append(5)
print(my_list)
# output => [1, 2, 3, 4, 5]

#! Dictionary Calls
d = {'k1':1,'k2':2 }
print(d.items())
# output => dict_items([('k1', 1), ('k2', 2)])
print(d.values())
# output => dict_values([1, 2])

#! Tuple Unpacking
x = [(1,2),(3,4),(5,6)]
print(x[0][0])

for item in x:
  print(item)
# output => (1, 2)
# output => (3, 4)
# output => (5, 6)

for a,b in x:
  print(a)
# output => 1 ,3, 5