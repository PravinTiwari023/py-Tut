"""
Streamlit Cheat Sheet

App to summarise Python docs v3+


17 Jan 2024

Contributor:
    @PravinTiwari : https://github.com/PravinTiwari023

"""

import streamlit as st
from pathlib import Path
import base64

# Initial page config

st.set_page_config(
    page_title='Streamlit cheat sheet',
    layout="wide",
    initial_sidebar_state="expanded",
)


def main():
    cs_sidebar()
    cs_body()

    return None


# sidebar

def cs_sidebar():
    st.sidebar.header(':sunglasses: :green[py-Tut]')
    st.sidebar.header(':blue[Python cheat sheet]')


    st.sidebar.markdown('''Python is the most popular programming language in data science. It is easy to learn and comes with a wide array of powerful libraries for data analysis.''')

    st.sidebar.code('''
# Import convention
>>> import streamlit as st
>>> install pandas as pd
>>> from pandas import DataFrame
''')

    st.sidebar.markdown('__Accessing help and getting object types__')
    st.sidebar.code('''
1 + 1 # Everything after the hash symbol is ignored by Python
help(max) # Display the documentation for the max function
type('a') # Get the type of an object — this returns str
    ''')

    st.sidebar.markdown('__The working directory__')
    st.sidebar.code('''
import os # Import the operating system package
os.getcwd() # Get the current directory
os.setcwd("new/working/directory") # Set the working directory to a new file path
''')

    st.sidebar.markdown('__Command line__')
    st.sidebar.code('''
$ python --version
$ pip install library-name
    ''')

    st.sidebar.markdown('__The working directory__')
    st.sidebar.code('''
import os # Import the operating system package
os.getcwd() # Get the current directory
os.setcwd("new/working/directory") # Set the working directory to a new file path
    ''')
    st.sidebar.markdown(
        '<small>Learn more about [Python Fundamentals](https://www.w3schools.com/python/)</small>',
        unsafe_allow_html=True)

    st.sidebar.markdown('''<hr>''', unsafe_allow_html=True)
    st.sidebar.markdown(
        '''<small>[Cheat sheet](https://www.datacamp.com/cheat-sheet/getting-started-with-python-cheat-sheet)  | Aug 2023 | [Pravin Tiwari](https://github.com/PravinTiwari023)</small>''',
        unsafe_allow_html=True)

    return None


##########################
# Main body of cheat sheet
##########################

def cs_body():
    st.header(':sunglasses: :green[py-Tut]')
    col1, col2, col3 = st.columns(3)

    #######################################
    # COLUMN 1
    #######################################

    # Display text

    col1.header(':violet[Operators]')
    col1.subheader('Arithmetic operators')
    col1.code('''
102 + 37 #Add two numbers with +
102 - 37 # Subtract a number with -
4 * 6 # Multiply two numbers with *
22 / 7 # Divide a number by another with /
22 // 7 # Integer divide a number with //
3 ** 4 # Raise to the power with **
22 % 7 # Returns 1 # Get the remainder  after division with %
    ''')

    # Display data

    col1.subheader('Assignment operators')
    col1.code('''
a = 5 # Assign a value to a
x[0] =1 # Change the value of an item in a list
    ''')

    # Display media

    col1.subheader('Numeric comparison operators')
    col1.code('''
3 == 3 # Test for equality with ==
3 != 3 # Test for inequality with !=
3 > 1 # Test greater than with >
3 >= 3 # Test greater than or equal to with >=
3 < 4 # Test less than with <
3 <= 4 # Test less than or equal to with <=
    ''')

    # Columns

    col1.subheader('Logical operators')
    col1.code('''
~(2 == 2) # Logical NOT with ~
(1 != 1) & (1 < 1) # Logical AND with &
(1 >= 1) | (1 < 1) # Logical OR with |
(1 != 1) ^ (1 < 1) # Logical XOR with ^
''')

    # Tabs
    col1.header(':violet[Getting started with lists]')
    col1.subheader('Creating lists')
    col1.code('''
    # Create lists with [], elements separated by commas
x = [1, 3, 2]
    ''')

    col1.subheader('List functions and methods')
    col1.code('''
# Return a sorted copy of the list x
sorted(x) # Returns [1, 2, 3]

# Sort the list in-place (replaces x)
x.sort() # Returns None

# Reverse the order of elements in x
reversed(x) # Returns [2, 3, 1]

# Reverse the list in-place
x.reversed() # Returns None

# Count the number of element 2 in the list
x.count(2)
''')

    # Control flow

    col1.subheader('Selecting list elements')
    col1.code('''
# Define the list 
x = ['a', 'b', 'c', 'd', 'e']

# Select the 0th element in the list
x[0] # 'a'

# Select the last element in the list
x[-1] # 'e'

# Select 1st (inclusive) to 3rd (exclusive)
x[1:3] # ['b', 'c']

# Select the 2nd to the end
x[2:] # ['c', 'd', 'e']

# Select 0th to 3rd (exclusive)
x[:3] # ['a', 'b', 'c']
''')

    # Personalize apps for users

    col1.subheader('Concatenating lists')
    col1.code('''
# Define the list x and y  
x = [1, 3, 6] 
y = [10, 15, 21]

# Concatenate lists with +
x + y # [1, 3, 6, 10, 15, 21]

# Repeat list n times with *
3 * x # [1, 3, 6, 1, 3, 6, 1, 3, 6]
''')

    col1.subheader('If-Else conditional')
    col1.code('''
    if age < 4:
        ticket_price = 0 
    elif age < 18:
        ticket_price = 10 
    elif age < 65:     
        ticket_price = 40 
    else:     
        ticket_price = 15

    ''')

    col1.subheader('Function')
    col1.code('''
    # First function with return statement
def my_function():
    return "Hello from a function"

print(my_function())

# Arguments
def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")

# For number of arguments
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

# number of arguments are known
def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")

# Function with default perameter
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
''')

    #######################################
    # COLUMN 2
    #######################################

    # Display interactive widgets

    col2.subheader('While & For Loop')
    col2.code('''
    # Simple while loop
# While Loop
i = 1
while i < 6:
  print(i)
  i += 1

# For Loop
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  
# using break statement
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1
  
# using continue statement
# While Loop
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)
  
# For Loop
for x in fruits:
  if x == "banana":
    continue
  print(x)
  
# using else statement
# While Loop
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")
  
# For Loop
for x in range(6):
  print(x)
else:
  print("Finally finished!")
    ''')

    col2.header(':violet[Getting started with dictionaries]')
    col2.subheader('Creating dictionaries')
    col2.code('''
# Create a dictionary with {}
{'a': 1, 'b': 4, 'c': 9}
    ''')

    col2.subheader('Dictionary functions and methods')
    col2.code('''
# Define the dictionary
a = {'a': 1, 'b': 2, 'c': 3}

# Get the keys
x.keys() # dict_keys(['a', 'b', 'c'])

# Get  the values
x.values() # dict_values([1, 2, 3])

# Get a value from a dictionary by specifying the key
x['a'] # 1
    ''')

    col2.header(':violet[NumPy arrays]')
    col2.subheader('Creating arrays')
    col2.code('''
# Convert a python list to a NumPy array
np.array([1, 2, 3]) # array([1, 2, 3])

# Return a sequence from start (inclusive) to end (exclusive)
np.arange(1,5) # array([1, 2, 3, 4])

# Return a stepped sequence from start (inclusive) to end (exclusive)
np.arange(1,5,2) # array([1, 3])

# Repeat values n times
np.repeat([1, 3, 6], 3) # array([1, 1, 1, 3, 3, 3, 6, 6, 6])

# Repeat values n times
np.tile([1, 3, 6], 3) # array([1, 3, 6, 1, 3, 6, 1, 3, 6])
              ''')

    # Build chat-based apps

    col2.subheader('Maths functions and methods')
    col2.code('''
# Calculate logarithm of an array
np.log(x) 
# Calculate exponential of an array
np.exp(x)
# Get maximum value of an array
np.max(x)
# Get minimum value of an array
np.min(x)
# Calculate sum of an array
np.sum(x)
# Calculate mean of an array
np.mean(x)
# Calculate q-th quantile of an array x
np.quantile(x, q)
# Round an array to n decimal places
np.round(x, n)
# Calculate variance of an array
np.var(x)
# Calculate standard deviation of an array
np.std(x)         
''')


    # Mutate data

    col2.header(':violet[Getting started with characters and strings]')
    col2.subheader('Introduction')
    col2.code('''
# Create a string variable with single or double quotes
"DataCamp"

# Embed a quote in string with the escape character \
"He said, \"DataCamp\""

# Create multi-line strings with triple quotes
"""
A Frame of Data
Tidy, Mine, Analyze It
Now You Have Meaning
Citation: https://mdsr-book.github.io/haikus.html
"""

# Get the character at a specific position
str[0] 

# Get a substring from starting to ending index (exclusive)
str[0:2]

''')

    # Display code


    #######################################
    # COLUMN 3
    #######################################

    # Connect to data sources

    col3.subheader('Combining and splitting strings')

    col3.code('''
# Concatenate strings with +
"Data" + "Framed" # 'DataFramed'

# Repeat strings with *
3 * "data " # 'data data data '

# Split a string on a delimiter
"beekeepers".split("e") # ['b', '', 'k', '', 'p', 'rs']
              ''')

    # Optimize performance

    col3.subheader('Mutate strings')
    col3.code('''
# Create a string named str
str = "Jack and Jill"

# Convert a string to uppercase
str.upper() # 'JACK AND JILL'

# Convert a string to lowercase
str.lower() # 'jack and jill'

# Convert a string to title case
str.title() # 'Jack And Jill' 

# Replaces matches of a substring with another
str.replace("J", "P") # 'Pack and Pill'
    ''')

    col3.header(':violet[Getting started with DataFrames]')
    col3.subheader('Creating DataFrames')
    col3.code('''
# Create a dataframe from a dictionary
pd.DataFrame({
    'a': [1, 2, 3],
    'b': np.array([4, 4, 6]),
    'c': ['x', 'x', 'y']
})

# Create a dataframe from a list of dictionaries
pd.DataFrame([
    {'a': 1, 'b': 4, 'c': 'x'},
    {'a': 1, 'b': 4, 'c': 'x'},
    {'a': 3, 'b': 6, 'c': 'y'}
])
    ''')

    col3.subheader('Selecting DataFrame Elements')
    col3.code('''
# Select the 4th row
df.iloc[3]

# Select one column by name
df['col']

# Select multiple columns by names
df[['col1', 'col2']]

# Select 3rd column
df.iloc[:, 2]

# Select the element in the 4th row, 3rd column
df.iloc[3, 2]
    ''')

    # Display progress and status

    col3.subheader('Manipulating DataFrames')
    col3.code('''
# Concatenate DataFrames vertically
pd.concat([df, df])

# Concatenate DataFrames horizontally
pd.concat([df,df],axis="columns")

# Get rows matching a condition
df.query('logical_condition')

# Drop columns by name
df.drop(columns=['col_name'])

# Rename columns
df.rename(columns={"oldname": "newname"})

# Add a new column
df.assign(temp_f=9 / 5 * df['temp_c'] + 32)

# Calculate the mean of each column
df.mean()

# Get summary statistics by column
df.agg(aggregation_function)

# Get unique rows
df.drop_duplicates()

# Sort by values in a column in ascending order
df.sort_values(by='col_name')

# Get the rows with the n largest values of a column
df.nlargest(n, 'col_name')
    ''')

    col3.subheader('Loading data')
    col3.code('''
pd.read_csv(filename) # From a CSV file

pd.read_table(filename) # From a delimited text file (like TSV)

pd.read_excel(filename) # From an Excel file

pd.read_sql(query, connection_object) # Reads from a SQL table/database

pd.read_json(json_string) # Reads from a JSON formatted string, URL or file.

pd.read_html(url) # Parses an html URL, string or file and extracts tables to a list of dataframes

pd.read_clipboard() # Takes the contents of your clipboard and passes it to read_table()

pd.DataFrame(dict) # From a dict, keys for columns names, values for data as lists
    ''')

    col3.subheader('Lambda function')
    col3.code('''
# Simple Lambda progran
x = lambda a : a + 10
print(x(5))

# Summarize argument
x = lambda a, b, c : a + b + c
print(x(5, 6, 2))

# Use case 
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))

# Same Example
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))
                  ''')

    return None

# Run main()

if __name__ == '__main__':
    main()