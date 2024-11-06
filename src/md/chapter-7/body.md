This chapter provides a crash course on the fundamentals of Python
programming. You'll learn to write and execute Python scripts and use
the interactive Python interpreter. You'll also use Python to do math,
define variables, work with strings and Boolean logic, loop through
lists of items, and use functions. Future
chapters rely on your understanding of these basic skills.


### Exercise 7-1: Install Python

Some operating systems, including most versions of Linux and macOS, come
with Python preinstalled, and it's common to have multiple versions of
Python installed at once. This book uses Python 3. After you follow the
Python installation instructions for your operating system in this
exercise, you should be able to run Python scripts with the
`python3` (for Linux and Mac)
or `python` (for Windows)
command.


#### Windows

Download and install the latest version of Python 3 for Windows from
[https://www.python.org](https://www.python.org).
During installation, check the box **Add Python 3.*x*** **to PATH**
(where **3.*x*** is the latest Python 3 version), which allows you to
run the `python` command in
PowerShell without using the Python program's absolute path.

Wherever this chapter instructs you to open a terminal,
use PowerShell instead of an Ubuntu terminal. You can also learn to use
Python in Ubuntu with WSL by following this chapter's Linux
instructions, but running Python directly in Windows makes reading and
writing data on your Windows-formatted USB disk much faster.

Windows users should replace all instances of `python3` with `python` when running the example code in this
chapter.



#### Linux

Open a terminal and make sure the `python3`, `python3-pip`, and `python3-venv` packages are installed, using this
`apt` command:

```sh
sudo apt install python3 python3-pip python3-venv
```

This command either installs the latest version of Python 3 available in
the Ubuntu repositories (as well as a few related packages you'll need
for this chapter) or does nothing if the packages are already installed.



#### macOS

Open a terminal and run the following Homebrew command to make sure
`python3` is installed:

```sh
brew install python3
```

This command either installs the latest version of Python 3 available in
Homebrew or does nothing if it's already installed.




### Exercise 7-2: Write Your First Python Script

Now that you've downloaded Python, you'll write and run a simple Python
script that displays some text in your terminal.

In your text editor, create a new file called *exercise-7-2.py* (all
Python scripts end in *.py*). The first time you open a Python script in
VS Code, it asks if you want to install the Python extension. I
recommend doing so in order to enable VS Code to make suggestions as
you're typing. The extension also has various features for highlighting
syntax errors and helping you format your code nicely.

Enter the following code (or copy and paste it from
[https://github.com/micahflee/hacks-leaks-and-revelations/blob/main/chapter-7/exercise-7-2.py](https://github.com/micahflee/hacks-leaks-and-revelations/blob/main/chapter-7/exercise-7-2.py)),
then save the file:

```py
print("hacks")
print("leaks")
revelations = "revelations".upper()
print(revelations)
```

As with shell scripts, Python scripts run instructions one line at a
time, starting at the top. When you run this code,
`print("hacks")` calls a
function called `print()` and
passes the string `hacks` into
it, displaying `hacks` in your
terminal window. The second line similarly displays `leaks`. (I'll explain strings in greater
detail in the Python Basics section on page 172, and
functions in the Functions section on page 192.)

Next, the script defines a variable called `revelations` and sets its value to the uppercase
version of the string `revelations`. To find the uppercase version of that
string, the program calls the `upper()` method, which is a type of function.
The final line then displays what's stored in the `revelations` variable: `REVELATIONS`.

**NOTE** *I have fond memories of retyping snippets of code from books. When I
was a teenager, I taught myself web and video game development by
reading programming books and typing the code samples I found into my
own editor. I always found that actually retyping the code, rather than
copying and pasting it, helped make the concepts stick, so I recommend
doing that for the exercises in this book.*

In a terminal, change to your *exercises* folder and run the script you
just created with the following command (Windows users, remember to
replace `python3` with
`python`):

```
micah@trapdoor chapter-7 % python3 exercise-7-2.py
```

The argument in this command is the path to the script that you want to
run, *exercise-7-2.py*. You should get the following output:

```
hacks
leaks
REVELATIONS
```

Try making the following changes to your
script, running it after each change to see the results:

-   Change the text in the `print()` functions.
-   Add new `print()` functions to display more text.
-   Use the string methods `lower()` and `capitalize()` instead of `upper()`.



### Python Basics

In this section, you'll learn to write code in the interactive Python
interpreter, comment your code, start doing simple math in Python, and
use strings and lists. This gentle introduction to Python syntax will
let you quickly try out some code on your own, before you dive into more
advanced topics.

As you read, don't be shy about searching online for answers to any
Python questions you might have beyond what this book covers. I
frequently find solutions to Python problems on websites like Stack
Overflow, a forum where people can ask technical questions and others
can answer them.


#### The Interactive Python Interpreter

The *Python interpreter* is a command line program that lets you run
Python code in real time, without writing scripts first, allowing you to
quickly test commands. To open the Python interpreter, you run the
`python3` command without any
arguments, like so:

```
micah@trapdoor ~ % python3
--snip--
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

The interpreter starts by telling you exactly which version of Python
you're using. Similar to a command line interface, it gives you the
prompt `>>>` and waits for you
to enter a Python command.

Run the following command:

```py
>>> print("Hello World!")
Hello World!
>>>
```

Entering `print("Hello World!")` and pressing **ENTER** should
immediately run your code, displaying `Hello World!` on the next line. Exit the interpreter
and return to the shell by running `exit()` or pressing
**CTRL**[-D]{.Character_20_style}.

In the remainder of this book, if my examples include the `>>>` prompt, that means they're running in
the Python interpreter. Run the same code in your own interpreter as you
follow along.



#### Comments

Writing code can be confusing even to experienced programmers, so it's
always a good idea to *comment* your code: add inline notes to yourself
or to others who might read your program. If you describe the purpose of
a specific portion of code in plain English (or whatever language you
speak), whoever looks at this code in the future can understand the gist
of what it's doing at a glance.

If a line of code starts with a hash mark (`#`), the whole line is a comment. You can
also add a hash mark after some code, followed by your comment. For
example, run the following lines of code:

```py
>>> # This is a comment
>>> x = 10 # This sets the variable x to the value 10
>>> print(x)
10
```

This is exactly the same as comments in shell scripting, which you
learned about in Chapter 3. Python ignores
comments, since they're intended for humans.



#### Math with Python

Computers, which are technically complicated calculators, are great at
doing math. It might not be immediately apparent, but investigating
datasets means constantly dealing with basic math: calculating disk
space, counting files, searching for keywords, and sorting lists. Here's
how a few basic mathematical operations work in Python:

**Operators**

The arithmetic operators for addition (+), subtraction
([−]{.listplain_symbol}), multiplication ([×]{.listplain_symbol}), and
division (/) are mostly the same in Python: `+`, `-`, and `/`, with an asterisk `*` for multiplication.

**Variables**

In math, a variable is a placeholder, normally a letter like *x*.
Variables in math often represent something unknown and it's your job to
solve for it, but Python variables are never unknown---they always have
a value. Name your Python variables something descriptive like
`price` or
`number_of_retweets` rather
than single letters without clear meanings. Variables in Python can
represent much more than just numbers, as you'll see later in this
chapter.

**Expressions**

An expression is a bit like a sentence made up of numbers, variables,
and operators. For example, here are a few expressions:

```
1 + 1
100 / 5
x * 3 + 5
```

Like sentences, expressions need to have the
correct syntax. Just like "potato the inside" isn't a valid sentence, 1
1 + isn't a valid expression. Enter the following expressions in the
Python interpreter to see how it evaluates them:

```py
>>> 1 + 1
2
>>> 100 / 5
20.0
>>> 3.14 * 2
6.28
```

Just like a calculator, Python respects the order of operations. It also
supports using parentheses:

```py
>>> 100 - 12 * 2
76
>>> (100 - 12) * 2
176
```

As in the rest of math, Python won't allow you to divide by zero:

```py
>>> 15 / 0
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
```

You define a variable in Python by saving a value inside that variable
with the equal sign (`=`). Try
defining `price` and
`sales_tax` variables and then
using them in an expression:

```py
>>> price = 100
>>> sales_tax = .05
>>> total = price + (price * sales_tax)
>>> print(total)
105.0
```

You can't use variables that you haven't yet defined. For example, if
you use an undefined variable `x` in an expression, you'll get an error:

```py
>>> x * 10
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'x' is not defined
```

Instead of just setting a variable equal to some value, you'll often
want to modify its existing value by a certain amount. For example, if
you're keeping track of the total price of items in a shopping cart in
the `total`
variable and want to add 10 dollars to that
total, you would define the variable like so:

```py
total = total + 10
```

Python's `+=` operator
performs the same operation:

```py
total += 10
```

The `+=` operator adds the
number on the right to the variable on the left. The Python operators
`-=`, `*=`, and `/=` work the same way. In your Python
interpreter, define a variable, then try changing its value using these
operators.



#### Strings

A *string* is a sequence of characters. Any time you need to load,
modify, or display text, you store it in a string. If you load the
contents of a text file into a variable in Python (for example, a 5MB
EML file that includes attachments), that's a string. But strings are
also often very short: in Exercise 7-2, you used the strings
`"hacks"`, `"leaks"`, and `"revelations"`.

In Python, strings must be enclosed in either single quotes (`'`) or double quotes (`"`). Run the following examples, which
demonstrate how to use each type of quote. Here is a string with double
quotes:

```py
>>> "apple" 
'apple'
```

Here is the same string with single quotes:

```py
>>> 'apple' # The same string with single quotes
'apple'
```

Use double quotes if you have single quotes within the string:

```py
>>> "She's finished!"
"She's finished!"
```

Use single quotes if you have double quotes within the string:

```py
>>> 'She said, "Hello" '
'She said, "Hello" '
```

Some of the same techniques you learned in Chapter
3 to work with strings in your shell also
apply to strings in Python. If your string uses double quotes, you can
escape them like so:

```py
>>> "She said, \"Hello\" "
```

You can similarly escape single quotes in a
single-quote string:

```py
>>> 'She\'s finished!'
```

Like numbers, strings can be stored in variables. Run the following code
to define `first_name` and
`last_name` variables,
replacing my name with yours:

```py
>>> first_name = "Micah"
>>> last_name = "Lee"
```

In Python, *f-strings* are strings that can contain variables. To use an
f-string, put the letter `f`
before the quotes, then put variable names in braces (`{`and}). For example, run the following
commands to display the values of the variables you just defined:

```py
>>> print(f"{first_name} {last_name}")
Micah Lee
>>> full_name = f"{first_name} {last_name}"
>>> print(f"{first_name}'s full name is {full_name}, but he goes by {first_name}")
Micah's full name is Micah Lee, but he goes by Micah
```

Place expressions inside f-strings in order to evaluate them:

```py
>>> print(f"1 + 2 + 3 + 4 + 5 = {1 + 2 + 3 + 4 + 5}")
1 + 2 + 3 + 4 + 5 = 15
```

Python will evaluate the expression for you, in this case `1 + 2 + 3 + 4 + 5`, and just print the result, which is
`15`.




### Exercise 7-3: Write a Python Script with Variables, Math, and Strings

In this exercise, you'll practice the concepts you've learned so far by
writing a simple Python script that uses variables and a few basic math
expressions and prints some strings. The script calculates how old a
person is in months, days, hours, minutes, and seconds, given their name
and an age (in years), and then displays this information. In your text
editor, create a new file called *exercise-7-3.py* and define these two
variables:

```py
name = "Micah"
age_years = 38
```

Replace the values of `name`
and `age_years` with your own
name and age.

Next, define some more variables that represent age in different units:
months, days, hours, minutes, and seconds. Start with months:

```py
age_months = age_years * 12
```

Add a days variable:

```py
age_days = age_years * 365
```

Finally, define variables for hour, minutes, and seconds:

```py
age_hours = age_days * 24
age_minutes = age_hours * 60
age_seconds = age_minutes * 60
```

Now that you've defined the variables, you can display them to the user.
Since the numbers in this exercise are going to get big, you'll include
commas to make them easier to read. For example, run this code in the
interpreter to display the variable `number` with commas using an f-string, adding
`:,` after the variable name
within the braces:

```py
>>> number = 1000000
>>> print(f"the number is: {number}")
the number is: 1000000
>>> print(f"the number is: {number:,}")
the number is: 1,000,000
```

Back in the Python script, add code to display all of the values, like
this:

```py
print(f"{name} is {age_years:,} years old")
print(f"That would be {age_months:,} months old")
print(f"Which is {age_days:,} days old")
print(f"Which is {age_hours:,} hours old")
print(f"Which is {age_minutes:,} minutes old")
print(f"Which is {age_seconds:,} seconds old")
```

This code uses `{name}` to
display the value of the name variable. That variable is a string, so it
doesn't make sense to try to separate it with commas. The rest of the
variables are numbers, though, so the code includes `:,` inside the braces for all of them to
include commas in the output. (The `age_years` values don't need commas, unless you
happen to be older than 1,000, but it doesn't hurt to use the
`:,` syntax---it adds a comma
only if one is needed.)

Save the file in your text editor. (A complete copy of the script is
available at
[https://github.com/micahflee/hacks-leaks-and-revelations/blob/main/chapter-7/exercise-7-3.py](https://github.com/micahflee/hacks-leaks-and-revelations/blob/main/chapter-7/exercise-7-3.py).)
In a terminal, change to your *exercises* folder for this exercise and
run the script. Here's what happens when I do so:

```
micah@trapdoor chapter-7 % python3 exercise-7-3.py
Micah is 38 years old
That would be 456 months old
Which is 13,870 days old
Which is 332,880 hours old
Which is 19,972,800 minutes old
Which is 1,198,368,000 seconds old
```

When you run the script with your name and age,
try changing the age and running it again to see how the numbers change.



### Lists and Loops

You'll often need to manage lists when investigating datasets. For
example, you might work with lists of filenames or rows in a
spreadsheet. In this section, you'll learn how to store lists as
variables and loop through those lists in order to run the same code for
each list item. You did something similar in Chapter
4 with `for` loops in the shell, but this time
you'll be working in Python.


#### Defining and Printing Lists

In Python, lists are defined with brackets (`[`and\]), with each item in the list
separated by commas (`,`). You
might have a list of numbers:

```py
[1, 2, 3]
```

Or of strings:

```py
["one", "two", "three"]
```

Or an empty list:

```py
[]
```

Just as variables can contain numbers or strings, they can also contain
lists. Use this line of code to store a list of letters in the Hebrew
alphabet, spelled out using Latin characters, in the
`hebrew_letters` variable:

```py
>>> hebrew_letters = ["aleph", "bet", "gimel", "dalet", "he", "vav", "zayin",
"chet", "tet", "yod", "kaf", "lamed", "mem", "nun", "samech", "ayin", "pe",
"tsadi", "qof", "resh", "shin", "tav"]
```

Now use the `print()` function
to display the items in the `hebrew_letters` variable:

```py
>>> print(hebrew_letters)
['aleph', 'bet', 'gimel', 'dalet', 'he', 'vav', 'zayin', 'chet', 'tet', 'yod',
'kaf', 'lamed', 'mem', 'nun', 'samech', 'ayin', 'pe', 'tsadi', 'qof', 'resh',
'shin', 'tav']
```

You can make long lists easier to read by entering each item in the list
on its own line, indented, like this:

```py
hebrew_letters = [
    "aleph",
--snip--
    "tav"
]
```

Each item in a list has an *index*, a number
that represents where in the list that item is located. The index of the
first item is 0, the second is 1, the third is 2, and so on. To select a
list item, you append brackets with the item's index to the end of the
list. For example, to select the first letter in the
`hebrew_letters` list, use
`hebrew_letters[0]`:

```py
>>> print(hebrew_letters[0])
aleph
>>> print(hebrew_letters[1])
bet
```

The first line of code uses the `print()` function to display the item from the
`hebrew_letters` list at index
0 (`aleph`), and the second
line displays the item at index 1 (`bet`).

Now use negative numbers to select items starting from the end of the
list, like so:

```py
>>> print(hebrew_letters[-1])
tav
>>> print(hebrew_letters[-2])
shin
```

You can use the `len()`
function to count the number of items in a list. For example, run the
following code to get the number of items in the
`hebrew_letters` list:

```py
>>> print(len(hebrew_letters))
22
```

This code uses the `print()`
function to display the output of the `len()` function. You could get the same
result by storing the output of the `len()` function in a variable:

```py
>>> length_of_hebrew_alphabet = len(hebrew_letters)
>>> print(length_of_hebrew_alphabet)
22
```

The first line of code runs `len(hebrew_letters)` and stores the result in the
`length_of_hebrew_alphabet`
variable. The second line uses the `print()` function to display that result.

You don't have to store a list in a variable to select items from it.
For example, run this code to display the second item (at index 1) in
the list `[1,2,3]`:

```py
>>> print([1,2,3][1])
2
```

The `append()` method lets you add items to lists.
For example, run the following code to add a new color to a list of
favorites:

```py
>>> favorite_colors = ["red", "green", "blue"]
>>> favorite_colors.append("black")
>>> print(favorite_colors)
['red', 'green', 'blue', 'black']
```

This code defines the variable `favorite_colors` as a list of strings containing
`red`, `green`, and `blue`. It then adds another string,
`black`, to the list by using
the `append()` method, before
finally displaying the value of the `favorite_colors` variable, using the `print()` function.

When writing code that analyzes datasets, you'll often create an empty
list and then append items to that list to make the data easier to work
with. For example, you'll learn in Chapter
13 about the code I wrote while investigating
America's Frontline Doctors, an anti-vaccine group. To properly analyze
a dataset of hundreds of thousands of files containing patient
information, I wrote code that created an empty list, opened each file,
and appended the pertinent patient data to that list.



#### Running for Loops

In Chapter 4, you used a `for` loop to unzip each BlueLeaks ZIP file.
Python also has `for` loops,
and they work the same way they do in shell scripting: by running a
snippet of code, called a *block*, on each item in a list. A
`for` loop has the following
syntax:

```py
for variable_name in list_name:
```

This syntax is followed by a block of indented code. Once you choose a
new variable to define in `variable_name`, you can use it in your code
block.

For example, run the following code to loop through the
`hebrew_letters` list, store
each item in the variable `letter`, and then display that item:

```py
>>> for letter in hebrew_letters:
...     print(letter)
...
```

After you enter the `for`
loop, which ends in a colon (`:`), the Python interpreter changes the
prompt from `>>>` to
`…` and waits for you to enter
the code block that will run for each item. Indent every line in your
block with the same number of spaces, then end your block with a blank
line. In this example, the code block that runs is just one line:
`print(letter)`.

The code should return the following output:

```
aleph
bet
--snip--
shin
tav
```

In this example, the `for` loop runs 22 times, once for each item
in the list, and stores the item in the variable `letter`. The first time it loops, the value of
`letter` is `aleph`. The second time, the value is
`bet`, and so on.

**NOTE** *Indentation tells Python which lines of code are part of your code
blocks. If some lines are indented with four spaces, but others with two
or three spaces, your Python code won't work. To keep things simple, I
recommend always indenting with four spaces. When writing scripts in VS
Code, you can indent multiple lines of code by selecting them with your
mouse and then pressing **TAB** (which indents four spaces for
you) or unindent by selecting a line and pressing
**SHIFT-TAB**.*

The following, slightly more complicated, example uses the
`len()` function to count not
the number of items in a list but characters in a string:

```py
>>> for letter in hebrew_letters:
...     count = len(letter)
...     print(f"The letter {letter} has {count} characters")
...
The letter aleph has 4 characters
The letter bet has 3 characters
The letter gimel has 5 characters
--snip--
The letter resh has 4 characters
The letter shin has 4 characters
The letter tav has 3 characters
```

This code tells you how many characters are used to spell the word for
each Hebrew letter in the Latin alphabet.

You can use `for` loops to
loop through strings as well, since a string is essentially a list of
characters:

```py
>>> word = "hola"
>>> for character in word:
...     print(character)
...
h
o
l
a
```

You can run a single `for`
loop as many times as you need for the dataset you're working on. For
example, in Chapter 9, you'll write code
that can open each of the hundreds of spreadsheets in the BlueLeaks
dataset and uses a `for` loop
to run your block of code on each row.

In the next section, you'll learn to make your programs more dynamic and
useful by determining which blocks of code should run under which
circumstances.




### Control Flow

Python scripts start at the top and run one line of code at a time, but
they don't always run these lines consecutively. In `for` loops, for example, the same block of
code might run over and over again before the loop completes and the
program continues to the next line. The order in which your lines of
code run is your program's *control flow*.

As you start writing code, you'll often alter the control flow by
telling your computer to do different things in different situations. If
you write a program that loops through a list of files in a dataset, for
instance, you may want to run different code when the program reaches a
PDF document than when it encounters an MP4 video.

This section teaches you how to run certain blocks of code under certain
conditions. To do this, you'll learn how to compare values, use
`if` statements based on these
comparisons, and express arbitrarily complicated conditions using
Boolean logic, all of which allow you to control the flow of your
program. You'll need this sort of logic whenever you write code that
searches a dataset for something specific and then responds according to
what it finds.


#### Comparison Operators

As mentioned earlier in this chapter, expressions that use the
arithmetic operators `+`,
`-`, `/`, and `*` generally evaluate to numbers:
`1 + 1` evaluates to `2`, for example. Expressions in Python
also use the following *comparison operators* to compare terms:

`<` Less than

`<=` Less than or equal to

`>` Greater than

`>=` Greater than or equal to

`==` Equal to (not to be
confused with a single equal sign (`=`), which defines a variable)

`!=` Not equal to

A *Boolean* is a type of variable that is either `True` or `False`. Expressions that use comparison
operators evaluate to Booleans instead of numbers, as in the following
examples:

```py
>>> 100 > 5
True
>>> 100 < 5
False
>>> 100 > 100
False
>>> 100 >= 100
True
>>> 0.5 < 1
True
>>> 0.999999 == 1
False
```

You can use these same operators to compare
strings, too. In Python, saying that one string is less than another
means that the former comes before the latter in alphabetical order, as
in the following examples:

```py
>>> "Alice" == "Bob"
False
>>> "Alice" != "Bob"
True
>>> "Alice" < "Bob"
True
>>> "Alice" > "Bob"
False
```

Strings are case sensitive. If you don't care about capitalization and
want to just see whether the strings are made up of the same words, make
them both lowercase before you compare them:

```py
>>> name1 = "Vladimir Putin"
>>> name2 = "vladimir putin"
>>> name1 == name2
False
>>> name1.lower() == name2.lower()
True
```

This technique allows you to determine whether the data you're
evaluating fulfills a given condition. For example, in Chapter
11, you'll write code to analyze the metadata
of over a million videos uploaded to the far-right social network
Parler. Using comparison operators, you'll determine which videos were
filmed on January 6, 2021, in Washington, DC, during the insurrection
after Trump lost the 2020 election.



#### if Statements

You use `if` statements to
tell your code to do something under certain conditions but not others.
The syntax for an `if`
statement is `if`
`expression``:` followed by an indented block of code.
If the expression evaluates to `True`, then the code block runs. If the
expression evaluates to `False`, the code doesn't run, and the flow
moves on to the next line.

For example, run the following code:

```py
>>> password = "letmein"
>>> if password == "letmein":
...     print("ACCESS GRANTED")
...     print("Welcome")
...
ACCESS GRANTED
Welcome
>>>
```

This code sets the value of the
`password` variable to
`letmein`. That means the
expression in the `if`
statement (`password`
`== "letmein"`) evaluates to `True` and the code block runs, so it
displays `ACCESS GRANTED` and
`Welcome`.

Now try including the wrong password in your `if` statement:

```py
>>> password = "yourefired"
>>> if password == "letmein":
...     print("ACCESS GRANTED")
...     print("Welcome")
...
>>>
```

This time, because you set the password to `"yourefired"`, the expression `password == "letmein"` evaluates to `False`, and Python doesn't run the
`if` statement's code block.

An `if` statement can
optionally incorporate an `else` block so that if the condition is
true, one code block runs, and if it's false, another block runs:

```py
if password == "letmein":
    print("ACCESS GRANTED")
    print("Welcome")
else:
    print("ACCESS DENIED")
```

You can also incorporate `elif` blocks, short for "else if." These let
you make another comparison if the first comparison is false, as shown
in Listing 7-1.

```py
if password == "letmein":
    print("ACCESS GRANTED")
    print("Welcome")
elif password == "open sesame":
    print("SECRET AREA ACCESS GRANTED")
else:
    print("ACCESS DENIED")
```
*Listing 7-1: Comparing `if`, `elif`, and `else` statements*

In this code, the `if`
statement evaluates the `password == "letmein"` expression. If it evaluates to
`True`, the code block runs
and displays the `ACCESS GRANTED` and `Welcome` messages. If the expression evaluates
to `False`, the program moves
on to the `elif` block, which
evaluates the `password`
`== "open sesame"` expression. If that evaluates to
`True`, it runs the block of
code that displays `SECRET AREA ACCESS GRANTED`. If it evaluates to `False`, the program moves on to the
`else` code block, which
displays `ACCESS DENIED`.



#### Nested Code Blocks

You can also accomplish the results of Listing 7-1 with multiple `if` statements and no `elif`, using *nested* code blocks, or
indented blocks of code inside other indented blocks of code:

```py
if password == "letmein":
    print("ACCESS GRANTED")
    print("Welcome.")
else:
    if password == "open sesame":
        print("SECRET AREA ACCESS GRANTED")
    else:
        print("ACCESS DENIED")
```

This code is functionally the same as Listing 7-1.

The more complicated your code, the more nested code blocks may come in
handy. You might include `for`
loops inside your `if`
statement code blocks, or `if`
statements inside `for` loops,
or even `for` loops inside
`for` loops.

You might prefer `elif`
statements to nested `if`
statements purely for readability purposes: it's easier to read and
write code with 100 `elif`
statements than code that's indented 100 times because it has 100 nested
`if` statements.



#### Searching Lists

The Python `in` operator,
which tells you whether an item appears in a list, is useful for working
with lists. For example, to check whether the number 42 appears in a
list of numbers, you can use `in` as follows:

```py
favorite_numbers = [7, 13, 42, 101]
if 42 in favorite_numbers:
    print("life, the universe, and everything")
```

To the left of the `in`
operator is a potential item inside a list, and to the right is the
list. If the item is in the list, then the expression evaluates to
`True`. If not, it evaluates
to `False`.

You can also use `not in` to
check if an item *isn't* in a list:

```py
if 1337 not in favorite_numbers:
    print("mess with the best, die like the rest")
```

Additionally, you can use `in`
to search for smaller strings inside of larger strings:

```py
sentence = "What happens in the coming hours will decide how bad the Ukraine
crisis gets for the vulnerable democracy in Russian President Vladimir Putin's
sights but also its potentially huge impact on Americans and an already deeply
unstable world."
if "putin" in sentence.lower():
    print("Putin is mentioned")
```

This code defines the variable
`sentence`, then checks to see
if the string `putin` is
inside the lowercase version of that sentence.



#### Logical Operators

It's possible to describe any scenario, no matter how complicated, using
the *logical operators* `and`,
`or`, and `not`. Like comparison operators, logical
operators also evaluate to `True` or `False`, and they let you combine comparisons.

For example, say you like astronomy and want to know if it's a good time
for stargazing. Let's set this up as a logical expression: if ((it's
dark out) **and** (it's **not** raining) **and** (it's **not** cloudy))
**or** (you have access to the James Webb Space Telescope), then yes.
Otherwise, no. Logical operators let you define this sort of logic in
your Python code.

Like other operators, the `and` and `or` operators compare an expression on the
left with an expression on the right. With `and`, if both sides are true, the whole
expression is true. If either is false, the whole expression is false.
For example:

- `True and True == True`
- `True and False == False`
- `False and True == False`
- `False and False == False`

With `or`, if either
expression is true, the whole expression is true. The whole expression
is false only when both expressions are false. For example:

- `True or True == True`
- `True or False == True`
- `False or True == True`
- `False or False == False`

The `not` expression differs
from the others in that it doesn't use an expression to the left, just
to the right. It flips true to false, and false to true. For example:

- `not True == False`
- `not False == True`

In sum, use `and` to determine
whether two things are both true, use `or` to determine whether at least one of
two things is true, and use `not` to change a true to a false or vice
versa. For example, consider this code:

```py
if country == "US" and age >= 21:
    print("You can legally drink alcohol")
else:
    if country != "US":
        print("I don't know about your country")
    else:
        print("You're too young to legally drink alcohol")
```

The first `if` statement has an expression that
compares two other expressions, `country == "US"` and `age >= 21`. If `country` is `US` and `age` is greater than or equal to
`21`, the expression
simplifies to `True and True`.
Since both Booleans are true, this evaluates to simply `True`, and the code block after the
`if` statement runs, printing
`You can legally drink alcohol` to the screen.

The first `else` block
determines what happens if that expression evaluates to `False`. For example, if `country` is `Italy`, but `age` is `30`, the expression simplifies to
`False and True`. Since at
least one of the Booleans is false, this evaluates to simply
`False`, so the code block
after `else` runs. Likewise,
if `country` is `US` but `age` is `18`, then the expression simplifies to
`True and False`. This, too,
evaluates to `False`, so the
code block after `else` runs.

Inside the second `else` block
is a simple `if` statement
without Boolean logic: if `country` isn't `US`, the screen displays
`I don't know about your country`. Otherwise (meaning `country` is `US`), it displays
`You're too young to legally drink alcohol`.

Just like with math, you can use parentheses in `if` statements to compare multiple
expressions. For example, the drinking age in the US is 21 and the
drinking age in Italy is 18. Let's add Italy to this program, this time
incorporating an `or`
operator:

```py
if (country == "US" and age >= 21) or (country == "Italy" and age >= 18):
    print("You can legally drink alcohol")
else:
    if country not in ["US", "Italy"]:
        print("I don't know about your country")
    else:
        print("You're too young to legally drink alcohol")
```

In plain English, the first `if` statement tells the program that if
your country is the US and you're at least 21 *or* if your country is
Italy and you're at least 18, then you can legally drink. In either
case, the whole expression in the `if` statement is true, and the program
prints `You can legally drink alcohol`. If just one of those is true and not
the other (for instance, if you're a 19-year-old Italian), the whole
statement is still true. That's what `or` means: if either of the things you're
comparing is true, then the whole expression is true.

Use the operator `not` to turn
`True` values into
`False` or `False` values into `True`. For example:

```py
if country == "US" and not age >= 21:
    print("Sorry, the drinking age in the US is 21")
```

You could replace `not age`
`>= 21` with `age < 21` for the same result.



#### Exception Handling

Python programs may abruptly quit with an error called an *exception*.
This is typically known as "throwing an exception." *Exception handling*
ensures that your Python code will run
another code block when your code catches an exception, instead of
quitting with an error.

You've seen a few examples of exceptions already in this chapter, like
when you tried dividing by zero (something you can't do in math) or
using a variable that hasn't been defined:

```py
>>> 15 / 0
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
>>> x * 10
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'x' is not defined
```

In these cases, Python threw a `ZeroDivisionError` exception and a `NameError` exception, respectively.

You can write code that catches exceptions when they're thrown, allowing
you to handle them gracefully. For example, let's say you have a list of
names called `names`, and you
want display the first name in the list:

```py
>>> names = ["Alice", "Bob", "Charlie"]
>>> print(f"The first name is {names[0]}")
The first name is Alice
```

This code displays the value at `names[0]`, or the first item in the
`names` list. This works as
expected if there are a few names in the list. But what if
`names` is empty?

```py
>>> names = []
>>> print(f"The first name is {names[0]}")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
```

In this case, since the index 0 doesn't exist because the list is empty,
Python throws an `IndexError`
exception.

You can catch this exception using `try` and `except` statements, like this:

```py
try:
    print(f"The first name is {names[0]}")
except:
    print("The list of names is empty")
```

This code first runs a `try`
statement, followed by a code block. It attempts to run the code in that
block, and if it succeeds without hitting an exception, it moves on to
the next line of code after the `except` block. However, if it hits an
exception, then it runs the code in the `except` block before moving on.

Here's what it looks like when there's no
exception:

```py
>>> names = ["Alice", "Bob", "Charlie"]
>>> try:
...     print(f"The first name is {names[0]}")
... except:
...     print("The list of names is empty")
...
The first name is Alice
```

In this case, the code block after the `try` statement ran successfully, so the
control flow moved on past the `except` block.

Here's what it looks like when the exception is thrown, but the code
catches it and handles it gracefully:

```py
>>> names = []
>>> try:
...     print(f"The first name is {names[0]}")
... except:
...     print("The list of names is empty")
...
The list of names is empty
```

The code block after the `try`
statement ran, but Python threw an `IndexError` exception when it evaluated
`names[0]`. Instead of
crashing and displaying an error, this code caught the exception and the
`except` block ran. In this
case, the `except` statement
runs if any exception is thrown in the `try` block, but you can get more granular
than that by using different `except` statements for different types of
exceptions. Consider the following example:

```py
try:
    --snip--
except ZeroDivisionError:
    # This catches ZeroDivisionError exception
    --snip--
except NameError:
    # This catches NameError exceptions
    --snip--
except IndexError:
    # This catches IndexError exceptions
    --snip--
except:
    # This catches any other exceptions that haven't been caught yet
    --snip--
```

By using `except`
`Exception``:`, where you replace `Exception` with a specific exception
you're interested in catching, you can write different code to handle
different types of exceptions. You'll revisit exception handling in
Chapter 10, when you learn how to work with
JSON data, and in the Chapter 14 case study
on neo-Nazi chat logs.

Now that you know how control flow works in
Python, you'll practice some basic Python syntax and make comparisons
using `if` statements and
Boolean logic in the next exercise.




### Exercise 7-4: Practice Loops and Control Flow

In social media slang, a common form of mockery is to employ
*alternating caps*, or switching from uppercase to lowercase and back to
uppercase, when quoting people. For example, here's the text of a viral
tweet from the now-suspended Twitter account @BigWangTheoryy:

> \*failing classes\*  
> Me: "Can I get some extra credit?"  
> Professor: "cAn i GEt SomE eXtRa creDiT?"

In this exercise, you'll write a Python script that starts with some
text and converts it into alternating caps style, using the control flow
concepts you learned in the previous section.

In your text editor, create a new file called *exercise-7-4.py*, and
start by defining the variable `text`, like this:

```py
text = "One does not simply walk into Mordor"
```

The simplest way to write this script is to start with an empty string,
called `alternating_caps_text`, and then loop through the characters
in `text`, adding characters
to `alternating_caps_text` one
at a time and alternating their capitalization as you do so. Add a
second line to your script defining that variable, like this:

```py
alternating_caps_text = " "
```

Next, you'll define a Boolean variable called
`should_be_capital`. Each time
you loop through a character in `text`, you'll use this Boolean to keep track
of whether the current character should be capital or lowercase. For
this example, start with a capital letter:

```py
should_be_capital = True
```

Beneath that line, add the main part of the script:

```py
for character in text:
    if should_be_capital:
        alternating_caps_text += character.upper()
         should_be_capital = False
    else:
         alternating_caps_text += character.lower()
         should_be_capital = True
```

Using a `for` loop, this code loops through the
characters in `text`, storing
each character in the `character` variable. It then adds these
characters to `alternating_caps_text`, switching between upper- and
lowercase.

During each iteration of the `for` loop, `character` is another character in `text`, the variable containing the
`"One does not simply walk into Mordor"` string. The first time the code loops,
`character` is `O`. When the code reaches the
`if` statement,
`should_be_capital` evaluates
to `True` for this character,
so the code block runs. The `+=` operator adds
`character.upper()` (or the
uppercase version of `character`) to `alternating_caps_text`. Since the code began by adding a
capital letter, you want it to add a lowercase letter next, so you set
`should_be _capital` to
`False`. The code block ends,
and the code starts its second loop.

During the second iteration, `character` is `n` and `should_be_capital` evaluates to `False`. When the code reaches the
`if` statement, the expression
evaluates to `False`, so the
`else` block runs. This is
similar to the other block, except that it appends the lowercase version
of character, `character.lower()`, to `alternative_caps_text` and sets `should_be_capital` back to `True`. So far,
`alternating_caps_text` is
`On`.

During the third iteration, `character` is `e` and `should_be_capital` evaluates to `True`. When the code reaches the
`if` statement, the expression
evaluates to `True`, so that
code block runs again, adding a capital `E` to `alternating _caps_text` and setting
`should_be_capital` to
`False` again. The code
continues in this way for the rest of the characters in `text`. Note that the uppercase and lowercase
versions of the space character, `" ".upper()` and `" ".lower()`, are identical. The `upper()` and `lower()` methods also don't change punctuation
characters like `,`,
`.`, `!`, and so on.

When this `for` loop is
finished, all you have left to do is display the value of
`alternating_caps_text` by
adding this line to your script:

```py
print(alternating_caps_text)
```

Your Python script is complete (you can also find a complete copy at
[https://github.com/micahflee/hacks-leaks-and-revelations/blob/main/chapter-7/exercise-7-4.py](https://github.com/micahflee/hacks-leaks-and-revelations/blob/main/chapter-7/exercise-7-4.py)).
Run your script. Here's the output I get:

```
micah@trapdoor chapter-7 % python3 exercise-7-4.py
OnE DoEs nOt sImPlY WaLk iNtO MoRdOr
```

Now change the value of `text`
and run the script again. For example, I changed the value to
`"There are very fine people on both sides"`:

```
micah@trapdoor chapter-7 % python3 exercise-7-4.py
ThErE ArE VeRy fInE PeOpLe oN BoTh sIdEs
```

You've gained a beginner's understanding of using lists and loops and
controlling the flow of execution. I'll conclude the chapter with one
more fundamental programming skill: breaking your code down into simpler
chunks using functions.



### Functions

The more complicated your programs get, the more important it is to
break the problems you're trying to solve down into smaller chunks and
work on them individually. This allows you to focus on the bigger
picture, using those smaller chunks of code as building blocks. In this
section, you'll learn how to do this using functions.

*Functions*, fundamental building blocks of programming, are reusable
chunks of code. They take *arguments*---the variables that you pass into
a function---as input and can *return* a value after they finish
running. You've already used a few functions that come with Python, like
`print()` and `len()`, but you can also define your own
function and use it as many times as you want without having to rewrite
that code. You'll learn how to do that in this section.


#### The def Keyword

You can define a new function using the `def` keyword. For example, this code
defines a function called `test()`, which prints a string to your
terminal:

```py
>>> def test():
...     print("this is a test function")
...
>>> test()
this is a test function
```

Function definition lines end with a colon and are followed by an
indented code block that defines exactly what the function does: in this
case, it displays the string `this is a test function`. This `test()` function doesn't include any
arguments, which means every time you run it, it will do the exact same
thing.

Listing 7-2 defines a slightly more complicated function, `sum()`, that adds two numbers together.

```py
def sum(a, b):
    return a + b
```
*Listing 7-2: Defining an example function*

This new function takes `a`
and `b` as arguments and
returns the sum of those two variables. For any function that takes more
than one argument, like this one, you separate the arguments with commas
(`,`).

Each variable has a *scope*, which describes which parts of your code
can use that variable. The arguments of a function (in this case,
`a` and `b`), as well as any variables defined
inside the function, have a scope that can be accessed only by code in
that function's code block. In other words, you can use these
`a` and `b` variables only inside the
`sum()` function, and they
won't be defined outside of that code block.

You can think of defining a function as telling Python, "I'm making a
new function with this name, and here's what it does." However, the
function itself won't run until you *call* it. Consider the following
Python script:



```py
def sum(a, b):
    return a + b

red_apples = 10
green_apples = 6
total_apples = sum(red_apples, green_apples)

print(f"There are {total_apples} apples")
```

First, the code defines a function called `sum()` to be a code block with just a
`return` statement. This
function doesn't run yet. The code then defines the `red_apples` variable, setting its value to
`10`, and the
`green_apples` variable,
setting its value to `6`.

The next line starts with `total_apples =`, but before Python can set the value
of that variable, it needs to learn what that value should be. To do
that, the code first calls the `sum()` function, passing in the arguments
`red_apples` and
`green_apples` as `a` and `b`. Now that the code is finally calling
this function, `return a`
`+ b` runs. In this function call,
`a` is `red_apples` and `b` is `green_apples`. The function returns `a + b`, which is `16`. Now that the `sum()` function has returned, the code
defines a variable called `total_apples`, setting its value to the return value
of the `sum()` function,
`16`.

Finally, the code calls the `print()` function, passing in an f-string as an
argument, which displays the `total_apples` variable. It will display the message
`There are 16 apples`.



#### Default Arguments

Function definitions can also have *default arguments*, which means
defining their value is optional. If you haven't passed in any values
for them when the function is called, the default value is used instead.

For example, consider this function, which, given a number and
optionally a number of exclamation marks and question marks, prints a
greeting using its arguments:

```py
def greet(name, num_exclamations=3, num_questions=2):
    exclamations = "!" * num_exclamations
    questions = "?" * num_questions
    print(f"Hello {name}{exclamations}{questions}")
```

The argument `name` is a
*positional argument*, which means when you call this function, the
first argument you pass in always has to be `name`. However, `num_exclamations` and `num_questions` are default arguments, so passing
values in for those is optional. The `greet()` function defines the strings
`exclamations` and
`questions` and sets them to a
series of exclamation points and question marks. (In Python, when you
multiply a string by a number, you get the original string repeated
multiple times; for example, `"A" * 3` evaluates to the string `AAA`.) The code then displays
`Hello`, followed by the value
of `name`, followed by the
number of exclamation points and question marks passed into the
function.

This function has one positional argument
(`name`) and two default
arguments (`num_exclamations`
and `num_questions`). You can
call it just passing in `name`, without passing values in for the
default arguments, and they will automatically be set to 3 and 2,
respectively:

```py
>>> greet("Alice")
Hello Alice!!!??
```

You can also keep the default value for one of the default arguments,
but choose a value for another. When you manually choose a value for a
default argument, you're using a *keyword argument*. For example:

```py
>>> greet("Bob", num_exclamations=5, num_questions=5)
Hello Bob!!!!!?????
>>> greet("Charlie", num_questions=0)
Hello Charlie!!!
>>> greet("Eve", num_exclamations=0)
Hello Eve??
```

The first function call uses keyword arguments for both
`num_exclamation` and
`num_questions`; the second
function call uses a keyword argument only for `num_questions` and uses the default argument for
`num_exclamations`; and the
third function call uses a keyword argument for
`num_exclamations` and uses
the default argument for `num_questions`.



#### Return Values

Functions become a lot more useful when they take some input, do some
computation, and then return a value, known as the *return value*. The
`greet()` function just
described displays output, but it doesn't return a value that I could
save in a variable or pass into further functions. However, the
`len()` function you used
earlier takes input (a list or a string), does some computation
(calculates the length of the list or string), and returns a value (the
length).

Here's an example of a function that takes a string `s` as an argument and returns the number
of vowels in the string:

```py
def count_vowels(s):
    number_of_vowels = 0
    vowels = "aeiouAEIOU"
    for c in s:
        if c in vowels:
            number_of_vowels += 1

    return number_of_vowels
```

This function brings together many of the concepts covered in this
chapter so far: it defines the variable `number_of_vowels` as `0`, then defines the variable
`vowels` as a string
containing lowercase and uppercase English vowels. Next, it uses a
`for` loop to loop through
each character in `s`, the
string that's passed into the function.

In each loop, the code uses an `if` statement to check whether the
character is a vowel (since `vowels` contains both lowercase and uppercase
letters, this code considers both `a` and `A` to be vowels). If the character is a
vowel, the code increases the `number_of_vowels` variable by one. Finally, it returns
`number_of_vowels`, which
equals however many vowels it counted in `s`.

Here are a few examples of calling this function and passing in
different strings:

```py
>>> count_vowels("THINK")
1
>>> count_vowels("lizard")
2
>>> count_vowels("zzzzzzz")
0
>>>
```

When you define a variable, you can set its value to the return value of
a function just by setting the variable equal to that function call:

```py
>>> num_vowels_think = count_vowels("THINK")
>>> num_vowels_lizard = count_vowels("lizard")
```

This code defines the variable `num_vowels_think` and sets its value to the return value
of `count_vowels("THINK")`, or
the number of vowels in the string `THINK`. It also defines the variable
`num_vowels_lizard` and sets
its value to the return value of `count_vowels("lizard")`.

You can then use those variables to define new variables:

```py
>>> total_vowels = num_vowels_think + num_vowels_lizard
>>> print(total_vowels)
3
```

This code adds those two variables together, saving their sum in a new
variable called `total_vowels`. It then prints the value of
`total_vowels` to the
terminal.

When a `return` statement
runs, the function immediately ends, so `return` is also useful if you want to stop a
function early. For example, the following `is_exciting()` function loops through all the
characters in a string `s` to
check whether the character is an exclamation point:

```py
def is_exciting(s):
    for character in s:
        if character == "!":
            return True

    return False
```

If the function finds an exclamation point, it returns `True`, immediately stopping the function. If
it checks each character and finds no exclamation points, it returns
`False`. For example, if you
call this function and pass in the
string `!@#$`, the function
will return `True` during the
first iteration of the loop and immediately end---it will never even get
to the second iteration. If you pass in the string `hello!`, it won't return `True` until the last iteration of the loop,
since it doesn't find the `!`
until the end of the string. And if you pass in the string
`goodbye`, it will loop
through the entire string and not find an exclamation point, so it will
return `False`.



#### Docstrings

In *self-documenting* code, documentation is defined as part of the code
as docstrings rather than in a separate document. *Docstrings* are
strings enclosed by three double quotes (`"""`) or three single quotes (`'``''`) on either side, placed as the first
line of code after a function definition. When you run the function, the
program ignores the docstring, but Python can use it to pull up
documentation about the function on request. Docstrings are optional,
but they can help other people understand your code.

For example, here's how you'd define the `sum()` function with a docstring:

```py
>>> def sum(a, b):
...     """This function returns the sum of a and b"""
...     return a + b
```

This is exactly the same as the `sum()` function defined in Listing
7-2, except it includes a docstring.

If you run the `help()`
function, passing in the name of a function (without arguments) as the
argument, the Python interpreter will display documentation for that
function. For example, running `help(sum)` gives you the following output:

```
Help on function sum in module __main__:

sum(a, b)
    This function returns the sum of a and b
```

The `help()` function works
for any function, though it's useful only if the programmer who wrote
that function included a docstring. In this case, it tells you that it's
showing you help for the function called `sum()` in the `__main__` module. You'll learn more about
modules in Chapter 8, but they're
essentially functions you write yourself. Try running
`help(print)` or
`help(len)` to view the
docstrings for the `print()`
and `len()` functions.

Press Q to get out of the help interface and back to the Python
interpreter.




### Exercise 7-5: Practice Writing Functions

In this exercise, you'll turn the script you wrote in Exercise 7-4 into
a function. You can then call this function multiple times, passing text
into it so that it returns an alternating caps version of that text each
time.

In your text editor, create a new file called
*exercise-7-5.py* and create a new function called
`alternating_caps()`, which
takes in the argument `text`,
like this:

```py
def alternating_caps(text):
    """Returns an aLtErNaTiNg cApS version of text"""
```

Next, copy the code from Exercise 7-4 and paste it into this function,
making sure to indent it so that it aligns with the docstring. Delete
the line that defines the `text` value; instead, define `text` by passing it into the function as an
argument. Also change the last line of the Exercise 7-4 code from
`print(alternating_caps_text)`
to `return alternating_caps_text`. This function shouldn't display the
alternating caps version of a string; it should create a variable
containing this version of a string and return it.

Your complete function should look like this (you can also find a copy
at
[https://github.com/micahflee/hacks-leaks-and-revelations/blob/main/chapter-7/exercise-7-5.py](https://github.com/micahflee/hacks-leaks-and-revelations/blob/main/chapter-7/exercise-7-5.py)):

```py
def alternating_caps(text):
    """Returns an aLtErNaTiNg cApS version of text"""
    alternating_caps_text = " "
    should_be_capital = True

    for character in text:
        if should_be_capital:
            alternating_caps_text += character.upper()
            should_be_capital = False
        else:
            alternating_caps_text += character.lower()
            should_be_capital = True

    return alternating_caps_text
```

Now that you have a function---a reusable chunk of code---you can use it
as many times as you want. Call this function a few times, remembering
to display its return value using the `print()` function, like this:

```py
print("Hacks, Leaks, and Revelations")
print(alternating_caps("This book is amazing"))
print(alternating_caps("I'm learning so much"))
```

You can change the text that you pass in to the
`alternating_caps()` function
calls to whatever you want.

Here's what it looks like when I run this script:

```
micah@trapdoor chapter-7 % python3 exercise-7-5.py
Hacks, Leaks, and Revelations
ThIs bOoK Is aMaZiNg
I'M LeArNiNg sO MuCh
```

While the output of this script is displayed in
a mocking tone, I hope that the sentiment is true for you!



### Summary

This chapter has covered several basic Python programming concepts
you'll rely upon in future investigations. You learned to write simple
Python scripts that incorporate the major features of the language,
including variables, `if`
statements, `for` loops, and
functions. You're ready to continue your Python programming journey in
the next chapter, this time writing code to directly investigate
datasets.