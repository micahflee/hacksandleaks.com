We'll go over some more advanced Python topics, like how to use modules,
how to traverse the filesystem, and how to create your own command line
programs in Python. You'll write programs that look through all of the
files in a folder, including the hundreds of thousands of files in the
BlueLeaks dataset, and learn to add arguments to your programs. You'll
also start working with a new type of variable in Python, the
dictionary, which will prove handy for working with data that's too
complex to store in simple lists. As with the previous chapter, future
chapters rely on your understanding of the topics covered here.


### Modules

As you learned in Chapter 7, functions are
reusable blocks of code that you can run as many times as you want
without having to rewrite any code. Python *modules* are similar, but
instead of making a single block of code reusable, they make an entire
Python file (or multiple files) reusable. You can think of a module as a
separate Python file that you can load into the file you're currently
working on.

Python includes a wealth of features, but most of them aren't available
to every Python script by default. Instead, they're stored in *built-in*
modules, those that come with Python. Once you import a module into your
script using an `import`
statement, you can access all of the functions, variables, and other
Python objects defined in that module using the syntax
`module_name`
`.``item_name`.

For example, the `time` module
includes the function `time.sleep()` (pronounced "time dot sleep"), which
makes your program wait a given number of seconds before continuing to
the next line of code. Run the following commands to import the
`time` module and then have it
tell Python to wait five seconds:

```py
>>> import time
>>> time.sleep(5)
```

Your Python interpreter should wait five seconds before the prompt
appears again.

Here are a few of the built-in modules I use the most:

`os` Includes useful functions
for browsing the filesystem, like `os.listdir()` and `os.walk()`. It also includes the submodule
`os.path`, which is full of
functions to inspect files. For example, it includes
`os.path.isfile()` and
`os.path.isdir()`, which help
determine whether a specific path is a file or a folder.

`csv` Lets you work with CSV
spreadsheet data.

`json` Lets you work with JSON
data.

`datetime` Includes useful
Python features for working with dates and times. For example, it allows
you to convert strings like `February 24, 2022 5:07:20 UTC+3` (the exact time that Russia invaded
Ukraine) into a timestamp that Python can understand and compare with
other timestamps, then convert it back into strings of any format you
choose.

You'll use the `os` module
extensively later in this chapter, the `csv` module in Chapter 9, and the `json` module in Chapter 11. You'll briefly see how `datetime` works later in this chapter when you
take a look at chat logs from a ransomware gang, as well as in the
Chapter 14 case study, where you'll analyze
leaked neo-Nazi chat logs.

As your programs get more complex, you might find it useful to split
them up into multiple files, with each file containing a different part
of your code. When you do this, you're creating your own modules. The
name of the module is the same as its filename. For
example, if you define some functions in a file called *helpers.py*,
another Python file can access those functions by importing the
`helpers` module. The
*helpers.py* file could contain the following code:

```py
def get_tax(price, tax_rate):
    return price * tax_rate

def get_net_price(price, tax_rate):
    return price + get_tax(price, tax_rate)
```

This module contains two functions for calculating sales tax,
`get_tax()` and
`get_net_price()`. The
following Python script, *price.py*, imports it like so:

```py
import helpers
total_price = helpers.get_net_price(50, 0.06)
print(f"A book that costs $50, and has 6% sales tax, costs ${total_price}")
```

The first line, `import helpers`, makes the functions defined in the
`helpers` module accessible to
this script. The second line calls the
`helpers.get_net _price()`
function from that module and stores the return value in the variable
`total_price`. The third line
displays the value of `total_price`.

Here's what it looks like when I run this script:

```
micah@trapdoor module % python3 price.py
A book that costs $50, and has 6% sales tax, costs $53.0
```

Running the *price.py* script executes the code defined in the
`helpers` module. Inside that
module, the `get_net_price()`
function calls `get_tax()` and
uses its return value to calculate the net price, then returns *that*
value back into the *price.py* script.

Before you write your first advanced Python script in Exercise 8-1,
let's look at the best way to start new Python scripts.



### Python Script Template

I use the same basic template for all my Python scripts, putting my code
into a function called `main()`, then calling that function at the
bottom of the file. This isn't required (you didn't do this for any of
the scripts you wrote in Chapter 7, after
all), but it's a good way to organize your code. Here's what it looks
like:

```py
def main():
    pass

if __name__ == "__main__":
    main()
```

The template defines the `main()` function with a `pass` statement that tells Python, "Skip
this line." I later replace `pass` with the real body of the script.

Next, the `if` statement tells
Python under which conditions it should run `main()`. Python automatically defines the
`__name__` variable, and the
definition differs depending on what Python file is being run. If you're
running the currently executing Python file directly, then Python sets
the value of `__name__` to the
`__main__` string. But if you
imported the currently executing Python file from another script, Python
sets the value of `__name__`
to the name of the imported module. Using the example from the previous
section, if you run the *helpers.py* script directly, the value of
`__name__` inside that script
will be `__main__`, but if you
run the *price.py* script, then the value of `__name__` will be `__main__` inside *price.py* and the value of
`__name__` will be
`helpers` inside *helpers.py*.

In short, if you run your script directly, the `main()` function will run. But if you import
your script as a module into another script or into the Python
interpreter, the `main()`
function won't run unless you call it yourself. This way, if you have
multiple Python scripts in the same folder, you can have one script
import another script to call the functions defined within it without
worrying about calling the latter script's `main()` function.

After I create this template script, I start filling in the
`main()` function with
whatever I want the script to do. Putting the main logic of your script
inside a function allows you to use the `return` statement to end `main()` early, which will quit the script
early. You can't use `return`
when you're not in a function.

In the following exercise, you'll put this into practice by writing a
script to start investigating BlueLeaks.



### Exercise 8-1: Traverse the Files in BlueLeaks

To efficiently investigate datasets, you need to be able to write code
that looks through large collections---sometimes thousands or
millions---of files for you. In this exercise, you'll learn various ways
to traverse the filesystem in Python using functions in the `os` module, working with the BlueLeaks
dataset. You'll also rely on the foundational skills you learned in
Chapter 7, like using variables,
`for` loops, and `if` statements.

As you read along and run the scripts, feel free to modify the code
however you'd like and try running those versions too. You might
discover revelations I didn't think to look for.


#### List the Filenames in a Folder

Start by using `os.listdir()`
to list the files in the *BlueLeaks-extracted* folder. In your text
editor, create a file called *list-files1.py* and enter this short
script (or copy and paste it from
[https://github.com/micahflee/hacks-leaks-and-revelations/blob/main/chapter-8/list-files1.py](https://github.com/micahflee/hacks-leaks-and-revelations/blob/main/chapter-8/list-files1.py)):



```py
import os

def main():
    blueleaks_path = "/Volumes/datasets/BlueLeaks-extracted"
    for filename in os.listdir(blueleaks_path):
        print(filename)

if __name__ == "__main__":
    main()
```

First, the script imports the `os` module. It then defines the variable
`blueleaks_path` with the path
of the *BlueLeaks-extracted* folder (update the script to include the
path of this folder on your own computer). The `os.listdir()` function takes the path to the folder
as an argument and returns a list of filenames in that folder. The code
uses a `for` loop to loop
through the output of `os.listdir(blueleaks_path)`, displaying each filename.

**NOTE** *Windows paths include the backslash character (`\`), which Python strings
consider an escape character. For example, if your `BlueLeaks-extracted` folder is located at `D:\BlueLeaks-extracted`, Python will misinterpret the string `"D:\BlueLeaks-extracted"`, assuming that `\B` is a special character. To
escape your backslashes for any Windows path you store as a string, use `\\` instead of `\`. In this case,
set the `blueleaks_path` string to `"D:\\BlueLeaks-extracted"`.*

Run this script. Here's what the output looks like on my computer:

```
micah@trapdoor chapter-8 % python3 list-files1.py
211sfbay
Securitypartnership
acprlea
acticaz
akorca
--snip--
```

Next, you'll try something slightly more advanced. Instead of just
listing the filenames in BlueLeaks, you'll check each filename to see
whether it's a folder, and if so, you'll open each of those folders and
count how many files and subfolders they contain.



#### Count the Files and Folders in a Folder

Create a file called *list-files2.py* and enter the following code (or
copy and paste it from
[https://github.com/micahflee/hacks-leaks-and-revelations/blob/main/chapter-8/list-files2.py](https://github.com/micahflee/hacks-leaks-and-revelations/blob/main/chapter-8/list-files2.py)):

```py
import os

def main():
    blueleaks_path = "/Volumes/datasets/BlueLeaks-extracted"
  ❶ for bl_folder in os.listdir(blueleaks_path):
        bl_folder_path = os.path.join(blueleaks_path, bl_folder)

      ❷ if not os.path.isdir(bl_folder_path):
            continue

      ❸ files_count = 0
        folders_count = 0
      ❹ for filename in os.listdir(bl_folder_path):
            filename_path = os.path.join(bl_folder_path, filename)

          ❺ if os.path.isfile(filename_path):
                files_count += 1

            if os.path.isdir(filename_path):
                folders_count += 1

      ❻ print(f"{bl_folder} has {files_count} files, {folders_count} folders")

if __name__ == "__main__":
    main()
```

This script counts the number of files and folders it finds within each
BlueLeaks folder. It starts like *list-files1.py* does, importing
`os` and defining the
`blueleaks_path` variable
(remember to update the variable's value to match the correct path on
your computer).

The first `for` loop cycles
through the filenames in your *BlueLeaks-extracted* folder, this time
saving each filename in the `bl_folder` variable, so its value will be
something like `miacx` or
`ncric` ❶. The script then sets the value of the new
`bl_folder_path` variable
accordingly. The `os.path.join()` function connects filenames together
to make complete paths. Its first argument is the starting path, and it
adds all other arguments to the end of that path. For example, if the
value of `bl_folder` is
`miacx`, then this function
will return the string
`/Volumes/datasets/BlueLeaks-extracted/miacx` on my computer (the output will be
different if your `blueleaks_path` is different or if you're using
Windows and your filenames use backslashes instead of slashes).

Since you want to look inside `bl_folder_path` and count the number of files and
folders it contains, the script needs to check that it's actually a
folder and not a file, using the `os.path.isdir()` function ❷. If `bl_folder_path` isn't a folder, the script runs the
`continue` statement. This
statement, which can run only inside of loops, tells Python to
immediately continue on to the next iteration of the loop. In short, if
the script comes across a file instead of a folder, it ignores it and
moves on.

The script then prepares to count the number of files and folders within
each individual BlueLeaks folder as the code loops by defining the
variables `files_count` and
`folders_count` with a value
of `0` ❸.

A second `for` loop loops
through the files in the BlueLeaks folder from the first `for` loop, saving each filename in the
`filename` variable
❹. Inside this loop, the
script defines `filename_path`
as the absolute path for the filename under consideration. For instance,
if the value of `filename` is
a string like `Directory.csv`,
then the value of `filename_path` would be a string like
`/Volumes/datasets/BlueLeaks-extracted/211sfbay/Directory.csv`.

The script then checks to see if this absolute
path is a file or a folder, using the `os.path.isfile()` and `os.path.isdir()` functions ❺. If the path is a file, the script increments
the `files_count` variable by
1; if it's a folder, the script increments `folders_count` by 1. When the second `for` loop finishes running, these two
variables should contain the total count of files and folders for the
BlueLeaks folder you're currently looping through in the first
`for` loop. Finally, the
script displays an f-string that shows these numbers ❻.

Try running the script. The output should show how many files and
folders are contained in each BlueLeaks folder, potentially with the
list of folders in a different order:

```
micah@trapdoor chapter-8 % python3 list-files2.py
bostonbric has 506 files, 10 folders
terrorismtip has 207 files, 0 folders
ociac has 216 files, 1 folders
usao has 0 files, 84 folders
alertmidsouth has 512 files, 10 folders
chicagoheat has 499 files, 10 folders
--snip--
```

So far, you've combined various functions in the `os` module to make a list of filenames in
your BlueLeaks folder and check whether each name actually refers to a
file or to another folder. Now it's time to learn to write code that can
also traverse the BlueLeaks folder's nested folders.




### Traverse Folders with os.walk()

Let's say you want to write a program that displays all of the files in
a folder and its subfolders, and its subsubfolders, and so on. When you
have nested folders but don't actually know how deep the folder
structure goes, listing all of the filenames just by using
`os.listdir()`,
`os.path.isfile()`, and
`os.path .isdir()` isn't so
simple. Python's `os.walk()`
function solves this problem.

The `os.walk()` function takes
a path to a folder as an argument and returns a list of *tuples*, or
multiple values contained in a single value. To define a tuple, you
place all of the values, separated by commas, within parentheses. For
example, `(3, 4)` is a tuple,
as is `("cinco", "seis", "siete")`. Tuples can also contain mixed types
like `(1, "dos")` and can
contain any number of values.

The `os.walk()` function
returns a list of tuples where each tuple contains three values:

```py
(dirname, subdirnames, filenames)
```

where `dirname` is a string,
`subdirnames` is a list of
strings, and `filenames` is a
list of strings. For example, the following code loops through the
return value of `os.walk(path)`:

```py
for dirname, subdirnames, filenames in os.walk(path):
    print(f"The folder {dirname} has subfolders: {subdirnames} and files: {filenames}")
```

When you use `for` loops to loop through lists, you
normally assign just a single variable to each item in the list.
However, since each item is a tuple, you can assign three variables to
it: `dirname`,
`subdirnames`, and
`filenames`. In each loop, the
values for this set of variables will be different: the value of
`dirname` is the path to a
folder, the value of `subdirnames` is a list of subfolders inside that
folder, and the value of `filenames` is a list of files inside that folder.

For example, suppose you have a folder called *example* that contains
these subfolders and files:

```
example
├── downloads
│   ├── screenshot.png
│   └── paper.pdf
└── documents
    ├── work
    │   └── finances.xlsx
    └── personal
```

This folder has two subfolders: *downloads* (containing *screenshot.png*
and *paper.pdf*) and *documents*. The *documents* folder has its own
subfolders: *work* (containing *finances.xlsx*) and *personal*.

The following commands loop through the return value of
`os.walk ("./example")`, where
*./example* is the path to this *example* folder, to find the values of
`dirname`,
`subdirnames`, and
`filenames` for each loop:

```py
>>> for dirname, subdirnames, filenames in os.walk("./example"):
...     print(f"The folder {dirname} has subfolders: {subdirnames} and files: {filenames}")
...
```

Running this command returns the following output:

```
The folder ./example has subfolders: ['documents', 'downloads'] and files: []
The folder ./example/documents has subfolders: ['personal', 'work'] and files: []
The folder ./example/documents/personal has subfolders: [] and files: []
The folder ./example/documents/work has subfolders: [] and files: ['finances.xlsx']
The folder ./example/downloads has subfolders: [] and files: ['paper.pdf', 'screenshot.png']
```

This code loops once for each folder, including all subfolders, with the
path to that folder stored in `dirname`. The list of subfolders in that folder
is stored in `subdirnames`,
and the list of files is stored in `filenames`. Once you've looped through the folder
and all of its subfolders, the `for` loop ends.

Any time you need to traverse all of the files in a dataset that
contains lots of nested folders, you'll want to use `os.walk()`. With a single `for` loop, you'll be able to write code
that inspects each file in the entire dataset. The `os.walk()` function has many uses, including
figuring out which files are the largest or smallest, as you'll see
next.



### Exercise 8-2: Find the Largest Files in BlueLeaks

In this exercise, you'll use `os.walk()` to write a script that looks through
all the files, folders, and subfolders in BlueLeaks; measures the size
of each file; and displays the filenames for files over 100MB. This code
allows you to loop through all of the files in a folder, no matter how
deep the folder structure.

Create a file called *find-big-files.py* and enter the following code
(or copy and paste it from
[https://github.com/micahflee/hacks-leaks-and-revelations/blob/main/chapter-8/find-big-files.py](https://github.com/micahflee/hacks-leaks-and-revelations/blob/main/chapter-8/find-big-files.py)):

```py
import os

def main():
    blueleaks_path = "/Volumes/datasets/BlueLeaks-extracted"
    for dirname, subdirnames, filenames in os.walk(blueleaks_path):
        for filename in filenames:
            absolute_filename = os.path.join(dirname, filename)
            size_in_bytes = os.path.getsize(absolute_filename)
            size_in_mb = int(size_in_bytes / 1024 / 1024)
            if size_in_mb >= 100:
                print(f"{absolute_filename} is {size_in_mb}MB")

if __name__ == "__main__":
    main()
```

Inside the `main()` function,
the script first defines the `blueleaks_path` variable as the path of the
*BlueLeaks-extracted* folder and loops through all of the files in the
entire BlueLeaks dataset using the `os.walk()` function. Inside each loop in the
first `for` loop are the
`dirname`,
`subdirnames`, and
`filenames` variables. Each
item in the list that `os.walk()` returns represents a different folder
or subfolder in the BlueLeaks dataset, so by the time this loop
finishes, the code will have traversed the entire dataset.

To find the biggest files, the next step is to look at each file with
another `for` loop, this time
looping through `filenames`.
Inside this second `for` loop,
the script defines `absolute_filename` to be the absolute path to the
filename. Since `dirname`
tells the script which folder it's looking in, and `filename` tells the script which file it's
looking at, the script passes these values into `os.path.join()` to combine them, creating the absolute
path to the filename.

A new function, `os.path.getsize()`, returns the size, in bytes, of the
file under consideration and stores it in the variable
`size_in_bytes`. The script
then converts this value from bytes to megabytes (storing that in the
variable `size_in_mb`) and
checks if it's greater than or equal to 100MB. If it is, the output
displays its filename and file size in megabytes with the
`print()` function.

Try running the script. It will take longer than the previous scripts in
this chapter, because this time, you're measuring the size of every
single file in BlueLeaks. Here's what the output looks like when I run
it (your output may be displayed in a different order):

```
micah@trapdoor chapter-8 % python3 find-big-files.py
/Volumes/datasets/BlueLeaks-extracted/usao/usaoflntraining/files/VVSF00000/001.mp4 is 644MB
/Volumes/datasets/BlueLeaks-extracted/chicagoheat/html/ZA-CHICAGO HEaT_LR-20160830-034_Final
Files.pdf is 102MB
/Volumes/datasets/BlueLeaks-extracted/nmhidta/files/RFIF300000/722.pdf is 148MB
/Volumes/datasets/BlueLeaks-extracted/nmhidta/files/RFIF200000/543.pdf is 161MB
/Volumes/datasets/BlueLeaks-extracted/nmhidta/files/RFIF100000/723.pdf is 206MB
/Volumes/datasets/BlueLeaks-extracted/fbicahouston/files/VVSF00000/002.mp4 is 145MB
/Volumes/datasets/BlueLeaks-extracted/fbicahouston/files/PSAVF100000/009.mp4 is 146MB
/Volumes/datasets/BlueLeaks-extracted/fbicahouston/files/PSAVF100000/026.mp4 is 105MB
--snip--
```

The script should display the absolute paths of the 101 files in
BlueLeaks that are at least 100MB, along with each file's size.



### Third-Party Modules

In addition to built-in modules, Python also supports third-party
modules that you can easily incorporate into your own code. Most Python
scripts that I write, even simple ones, rely on at least one third-party
module (when a Python program depends on third-party modules, they're
called *dependencies*). In this section, you'll learn how to install
third-party modules and use them in your own scripts.

The Python Package Index (PyPI) contains hundreds of thousands of
third-party Python *packages*, or bundles of Python modules, and
subpackages. Pip, which stands for Package Installer for Python, is a
package manager similar to Ubuntu's apt or macOS's Homebrew used to
install packages hosted on PyPI. You can search for packages on PyPI's
website
([https://pypi.org](https://pypi.org)),
then install a package by running the `python3 -m pip install package_name` command.

For example, I frequently use a package called Click, which stands for
Command Line Interface Creation Kit. The `click` Python module makes it simple to add
command line arguments to your scripts. To see what happens when you try
importing this module before you've installed it, open a Python
interpreter and run `import click`. Assuming you don't already have the
package installed, you should see a `ModuleNotFoundError` error message:

```py
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'click'
>>>
```

Now exit the Python interpreter and install `click` with pip by running the following
command:

```
micah@trapdoor ~ % python3 -m pip install click
Collecting click
  Using cached click-8.1.3-py3-none-any.whl (96 kB)
Installing collected packages: click
Successfully installed click-8.1.3
```

Open the Python interpreter again and try
importing `click` once more:

```py
>>> import click
>>>
```

If no error messages pop up, you've successfully imported the
`click` module, and its
additional features are now available for you to use.

The command to uninstall a package is `python3 -m pip uninstall  package_name`. Try uninstalling
`click`:

```
micah@trapdoor ~ % python3 -m pip uninstall click
Found existing installation: click 8.1.3
Uninstalling click-8.1.3:
  Would remove:
    /usr/local/lib/python3.10/site-packages/click-8.1.3.dist-info/*
    /usr/local/lib/python3.10/site-packages/click/*
Proceed (Y/n)? y
  Successfully uninstalled click-8.1.3
```

As you can see, when I ran this command, the output listed the files
that pip would need to delete to uninstall the `click` module, then asked if I wanted to
proceed. I entered `y` and
pressed **ENTER**, and the files were deleted and the module
uninstalled.

You can install multiple Python packages at once like so:

```sh
python3 -m pip install package_name1 package_name2 package_name3
```

The same is true of uninstalling.

It's common to define the Python packages that your script requires
inside a file called *requirements.txt*, then install all of them at
once with the `python3 -m pip install -r requirements.txt` command. For example, suppose in
addition to using `click`, you
want to use the HTTP client `httpx` to load web pages inside Python and
the `sqlalchemy` module to
work with SQL databases. To include all three in your Python script,
first create a *requirements .txt* file with each package name on its
own line:

```
click
httpx
sqlalchemy
```

Then run the following command to install them simultaneously:

```
micah@trapdoor chapter-8 % python3 -m pip install -r requirements.txt
Collecting click
  Using cached click-8.1.3-py3-none-any.whl (96 kB)
Collecting httpx
  Using cached httpx-0.23.0-py3-none-any.whl (84 kB)
--snip--
Successfully installed anyio-3.6.1 certifi-2022.9.24 click-8.1.3 h11-0.12.0 httpcore-0.15.0
httpx-0.23.0 idna-3.4 rfc3986-1.5.0 sniffio-1.3.0 sqlalchemy-1.4.41
```

As you can see, this command installs more than
just those three Python packages: `rfc3986`, `certifi`, `sniffio`, and so on are also included. That's
because `click`,
`httpx`, and
`sqlachemy` have dependencies
of their own. For example, `httpcore` is a dependency of the `httpx` package, so it installs that as well.
To summarize, the *requirements.txt* file defines your project's
dependencies, each of which might depend on its own list of packages.

**NOTE** *To learn more about how to use* *httpx* *and other Python modules to automate interacting with websites, check out Appendix B. I recommend waiting until you complete Chapters 7, 8, 9, and 11, however, since the instructions covered in Appendix B rely on the skills you'll pick up in those chapters.*

> #### VIRTUAL ENVIRONMENTS
> 
It’s not unusual to have multiple versions of Python and multiple versions of the same dependencies for different projects installed on the same computer. If you routinely install Python packages with pip for various projects, this can get very messy over time. For example, different projects might depend on different versions of the same module to work, but you can’t have two versions of a module installed at the same time—at least not without *virtual environments*, which are like stand-alone folders containing your Python dependencies for a specific project. This way, different projects’ dependencies won’t trip each other up.
> 
> To keep things simple, this book doesn’t use virtual environments, and it uses only pip to install Python packages. As long as you don’t have multiple Python projects requiring specific versions of the few third-party modules this book uses, you should be fine without using a virtual environment.
> 
> You can learn more about virtual environments at [https://docs.python.org/3/tutorial/venv.html](https://docs.python.org/3/tutorial/venv.html). For larger Python projects, you might also consider using Python package management programs such as Poetry ([https://python-poetry.org](https://python-poetry.org)) or Pipenv ([https://github.com/pypa/pipenv](https://github.com/pypa/pipenv)), which handle the complicated parts of keeping track of Python packages and virtual environments for you.

Now that you know how to install third-party modules, you'll practice using Click.


### Exercise 8-3: Practice Command Line Arguments with Click

As you learned in the previous section, the Click package makes it
simple to add command line arguments to your scripts. You can use it to
define variables to pass into your `main()` function from the terminal, without
having to define those variables in your code. In this exercise, you'll
learn how to use Click by writing a sample script in preparation for
using this module in later exercises.

First, install the Click package with pip again
by running `python3 -m pip install click`. Next, open your text editor and enter
the following Python script, *exercise-8-3.py* (or copy and paste it
from
[https://github.com/micahflee/hacks-leaks-and-revelations/blob/main/chapter-8/exercise-8-3.py](https://github.com/micahflee/hacks-leaks-and-revelations/blob/main/chapter-8/exercise-8-3.py)):

```py
import click

@click.command()
@click.argument("name")
def main(name):
    """Simple program that greets NAME"""
    print(f"Hello {name}!")

if __name__ == "__main__":
    main()
```

First, the script imports the `click` module. It then runs a few
*decorators*, function calls that begin with `@` and add functionality to another
function you're about to define---the `main()` function, in this case. The
`@click.command()` decorator
tells Click that `main()` is a
command, and the `@click .argument("name")` decorator tells Click that this
command has an argument called `name`.

Next, the script defines the `main()` function, which takes `name` as an argument. This function has a
docstring, `Simple program that greets NAME`. Click uses this docstring for its
commands when it builds the output for `--help`, as you'll see shortly. The
`main()` function simply
displays a string with the name you passed in as an argument.

Finally, the script calls the `main()` function. Notice that even though
`main()` requires an argument
(`name`), the script doesn't
explicitly pass that argument in when calling the function. This is
where the magic of the Click decorators comes in. When the script calls
`main()`, Click will figure
out what arguments it needs to pass in, find their values from the CLI
arguments, and pass them in for you.

Run the script as follows:

```
micah@trapdoor chapter-8 % python3 exercise-8-3.py
Usage: click-example.py [OPTIONS] NAME
Try 'click-example.py --help' for help.

Error: Missing argument 'NAME'.
```

When you run the program, if you don't pass in the correct CLI
arguments, Click tells you what you did wrong. As you can see, you're
missing the required `NAME`
argument. Click also tells you that you can get help by running the
script again with the `--help`
argument.

Try running the `--help` command:

```
micah@trapdoor chapter-8 % python3 exercise-8-3.py --help
Usage: click-example.py [OPTIONS] NAME

  Simple program that greets NAME

Options:
  --help  Show this message and exit.
```

This time, the output shows a description of the program based on the
docstring. Any CLI program that uses Click will display the docstring
for the command when you run it with `--help`.

Try running the command again, this time passing in a name. For example,
here's what happens when I pass in `Eve` as the name:

```
micah@trapdoor chapter-8 % python3 exercise-8-3.py Eve
Hello Eve!
```

**NOTE** *You can read more about using Click at [https://click.palletsprojects.com](https://click.palletsprojects.com).*



### Avoiding Hardcoding with Command Line Arguments

As you've seen in previous chapters, CLI arguments let you run the same
program in many different ways, targeting different data. For example,
in Chapter 4, you used the `du` command to estimate the disk space of
a folder by adding the folder's path as an argument. In
`du -sh --apparent-size`
`path`, the arguments
are `-sh`,
`--apparent-size`, and
`path`.

The `du` command would be much
less useful if it could measure disk space for only a single hardcoded
folder. *Hardcoding* means embedding information, like a path, directly
into source code. You can avoid hardcoding anything in your CLI programs
by having the user provide this information as arguments when running
them.

Passing paths into scripts, rather than hardcoding them, makes for a
better user experience. In previous exercises in this chapter, you
hardcoded the path to your copy of the BlueLeaks dataset into your
Python scripts. If you were to pass the appropriate path in as an
argument, however, other people could use your script without editing
it---they could just pass in *their* path when they ran it.

Using arguments rather than hardcoding can also make your scripts more
universally useful. For example, in Exercise 8-2, you wrote a
script to find all of the files that are at least 100MB in the BlueLeaks
dataset. Using CLI arguments, you could make this script work for any
dataset you get your hands on, not just BlueLeaks, and for any minimum
file size, allowing you to run it in a variety of situations. You'd just
need to pass in the dataset path and the minimum file size as CLI
arguments. You'll try this out in the next exercise.



### Exercise 8-4: Find the Largest Files in Any Dataset

In this exercise, you'll modify the script you wrote in Exercise
8-2 to make it work for any dataset, and for any minimum file
size, using CLI arguments. In the following chapters, you'll write
simple Python scripts that use Click for CLI arguments, so you can
provide the paths to the datasets you'll be working with.

Create a new file called *exercise-8-4.py*, and copy and paste the
*exercise-8-2 .py* code into it. Next, make the following modifications
to the code, highlighted in bold (or find the full modified script at
[https://github.com/micahflee/hacks-leaks-and-revelations/blob/main/chapter-8/exercise-8-4.py](https://github.com/micahflee/hacks-leaks-and-revelations/blob/main/chapter-8/exercise-8-4.py)):

```py
import os
import click

@click.command()
@click.argument("path")
@click.argument("min_file_size", type=click.INT)
def main(path, min_file_size):
    """Find files in PATH that are at least MIN_FILE_SIZE MB big"""
    for dirname, subdirnames, filenames in os.walk(path):
        for filename in filenames:
            absolute_filename = os.path.join(dirname, filename)
            size_in_bytes = os.path.getsize(absolute_filename)
            size_in_mb = int(size_in_bytes / 1024 / 1024)
            if size_in_mb >= min_file_size:
                  print(f"{absolute_filename} is {size_in_mb}MB")

if __name__ == "__main__":
    main()
```

This code imports the `click`
module at the top of the file. Next, it adds Click decorators before the
`main()` function:
`@click.command()` makes the
`main()` function a Click
command, and `@click.argument()` adds `path` and `min_file_size` as arguments. The script specifies
with `type=click.INT` that the
`min_file_size` argument
should be an *integer*, or a whole number, as opposed to a string. Then
it adds `path` and
`min_file_size` as arguments
to the `main()` function and
adds a docstring that describes what this command does.

The new script uses arguments instead of hardcoded values. It deletes
the line that defines the `blueleaks_path` variable, and in the
`os.walk()` function call, it
changes `blueleaks_path` to
just `path`, which is the
argument. Finally, it changes `100` in `size_in_mb  >=  100` to `min_file_size`.

You can now use this program to find big files in any folder in the
BlueLeaks dataset or elsewhere. For example, here's what it looks like
when I search for all files that are at least 500MB in */Applications*
on my Mac:

```
micah@trapdoor chapter-8 % python3 exercise-8-4.py /Applications 500
/Applications/Dangerzone.app/Contents/Resources/share/container.tar.gz is 668MB
/Applications/Docker.app/Contents/Resources/linuxkit/services.iso is 602MB
```

As you can see, I have only two apps installed
that include files this big: Dangerzone and Docker Desktop.

Now that you've seen how to add CLI arguments to your Python scripts
using Click, you should be able to avoid hardcoding information like
dataset paths in your future programs.

Next, we'll switch gears and explore a new powerful type of Python
variable called dictionaries.



### Dictionaries

In the course of your investigations, sometimes you'll need to keep
track of data with more structure than a simple list. To do so, you can
use Python dictionaries. Instead of a collection of items, a
*dictionary* (*dict* for short) is a collection of keys that map to
values. *Keys* are labels that you use to save or retrieve information
in a dictionary, and *values* are the actual information being saved or
retrieved. Nearly every Python script I write that deals with data uses
dictionaries. In this section, you'll learn how to define dictionaries,
get values from them, add values to them, and update existing values in
them.


#### Defining Dictionaries

Dictionaries are defined using braces (`{`and `}`), sometimes referred to as curly
brackets. Inside the braces is a list of key-value pairs in the format
`key: value`, where each pair is separated
from the next by commas---for example,
`{"country": "Italy", "drinking_age": 18}`. For longer dictionaries, you can make
your code more readable by putting each key-value pair on its own line.

Listing 8-1 shows an example dictionary
stored in the variable `capitals`.

```py
capitals = {
    "United States": "Washington, DC",
    "India": "New Delhi",
    "South Africa": "Cape Town",
    "Brazil": "Brasília",
    "Germany": "Berlin",
    "Russia": "Moscow",
    "China": "Beijing"	
}
```
*Listing 8-1: A dictionary stored in the `capitals` variable*

In this case, the keys are country names and the values are the capitals
of those countries.

Each key in a dictionary can have only one value. If you try to set the
same key more than once, Python will save the version you last set. For
example, if you define a dictionary and use the `name` key more than once, the dictionary
will overwrite the previous value with the most recent one:



```py
>>> test_dict = {"name": "Alice", "name": "Bob", "hobby": "cryptography"}
>>> print(test_dict)
{'name': 'Bob', 'hobby': 'cryptography'}
```

However, you can also use lists, or other dictionaries, as values:

```py
>>> test_dict = {"names": ["Alice", "Bob"], "hobby": "cryptography"}
>>> print(test_dict)
{'names': ['Alice', 'Bob'], 'hobby': 'cryptography'}
```

In this case, the value for the key `names` is `['Alice', 'Bob']`, which itself is a list. You can use a
combination of lists and dictionaries to organize pretty much any type
of data, no matter how complicated, allowing you to more easily work
with it in Python.



#### Getting and Setting Values

To retrieve an item you've stored inside a dictionary, add square
brackets containing the item's key to the end of the dictionary name. If
you try to use a key you haven't defined, your script will crash with a
`KeyError`. For example,
here's how to look up the capitals of certain countries in the
`capitals` dictionary:

```py
>>> capitals["United States"]
'Washington, DC'
>>> capitals["China"]
'Beijing'
>>> capitals["Kenya"]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'Kenya'
```

When you run `capitals["Kenya"]`, Python throws the error message
`KeyError: 'Kenya'`. This
means that `Kenya` isn't a
valid key in the `capitals`
dictionary. You can see that the only keys defined in Listing
8-1 are `United States`, `India`, `South Africa`, `Brazil`, `Germany`, `Russia`, and `China`. Because `Kenya` isn't a key in this dictionary, you
can't retrieve its value.

You can add new key-value pairs to a dictionary, or update an existing
one, like this:

```py
>>> capitals["Kenya"] = "Nairobi"
>>> capitals["United States"] = "Mar-a-Lago"
>>> print(capitals)
{'United States': 'Mar-a-Lago', 'India': 'New Delhi', 'South Africa': 'Cape Town', 'Brazil': 'Brasília', 'Germany': 'Berlin', 'Russia': 'Moscow', 'China': 'Beijing', 'Kenya': 'Nairobi'}
```

This code defines a new key, `Kenya`, with the value `Nairobi`. It also updates an existing key,
`United States`, to have the
value `Mar-a-Lago`,
overwriting its old value, which used to be `Washington, DC`.




### Navigating Dictionaries and Lists in the Conti Chat Logs

You can combine dictionaries and lists in a single flexible data
structure that allows you to represent a wide variety of information. If
you're writing Python code to work with datasets, chances are you're
going to need both. You might directly load the data in this format, or
you might create your own dictionaries and lists to store aspects of the
data.

To describe how to use data structures that include a combination of
dictionaries and lists, I'll use an example from a real dataset. The day
after Russia invaded Ukraine on February 24, 2022, the notorious Russian
ransomware gang Conti, known for hacking companies around the world and
extorting millions of dollars from them, published a statement on its
website throwing its full support behind the Russian government. It
threatened any "enemy" who launched cyberattacks against Russia with
retaliation against their "critical infrastructure." Three days later, a
Ukrainian security researcher anonymously leaked 30GB of internal data
from Conti: hacking tools, training documentation, source code, and chat
logs. The Conti chat logs originally came in the form of JSON files,
which is structured data. When you load JSON files into Python, they'll
automatically be loaded as a combination of dictionaries and lists.

In this section, you'll look through some of these chat logs in order to
practice working with real leaked data stored in dictionaries and lists.
Using Python code, you'll learn how to navigate these structures to
access specific pieces of data as well as how to quickly loop through
the chat logs and select just the parts you're interested in.


#### Exploring Dictionaries and Lists Full of Data in Python

You can download the complete Conti dataset from
[https://ddosecrets.com/wiki/Conti_ransomware_chats](https://ddosecrets.com/wiki/Conti_ransomware_chats).
However, for this section, you'll use just one file from the dataset,
*2022-02-24-general.json*, which the Ukranian security researcher
extracted from a chat system called RocketChat.

Download *2022-02-24-general.json* from
[https://github.com/micahflee/hacks-leaks-and-revelations/blob/main/chapter-8/2022-02-24-general.json](https://github.com/micahflee/hacks-leaks-and-revelations/blob/main/chapter-8/2022-02-24-general.json).
Open a terminal, change to the folder where you stored this file, and
open a Python interpreter. Load this file into a dictionary with the
following commands:

```py
>>> import json
>>> with open("2022-02-24-general.json") as f:
...     data = json.load(f)
...
```

This code uses the `json`
module and loads the data from *2022-02-24-general.json* into the
`data` variable. The chat logs
from this file are too long to display in their entirety, but Listing
8-2 shows a snippet of the value of the
`data` dictionary that
demonstrates its structure.

```json
{
    "messages": [❶
        {
--snip--
        },
        {
            "_id": "FmFZbde9ACs3gtw27",
            "rid": "GENERAL",
            "msg": "Некоторые американские сенаторы предлагают помимо соцсетей блокировать в
Россииещё и PornHub!",
            "ts": "2022-02-24T22:02:38.276Z",
            "u": {"_id": "NKrXj9edAPWNrYv5r", "username": "thomas", "name": "thomas"},
            "urls": [],
            "mentions": [],
            "channels": [],
            "md": [
                {
                    "type": "PARAGRAPH",
                    "value": [
                        {
                            "type": "PLAIN_TEXT",
                            "value": "Некоторые американские сенаторы предлагают помимо
соцсетейблокировать в России ещё и PornHub!",
                        }
                  ],
                }
            ],
            "_updatedAt": "2022-02-24T22:02:38.293Z",
        },
        {
--snip--
        },
    ],
    "success": True ❷
}
```
*Listing 8-2: Conti chat logs from RocketChat*

The `data` variable is a
dictionary with two keys, `messages` and `success`. You access the value of the
`messages` key, which is a
list of dictionaries, using the expression `data["messages"]` ❶. You can tell that the value of
`data["messages"]` is a list
because it's enclosed in square brackets (`[` and `]`), and you can tell
that the items inside it are dictionaries because they're enclosed in
braces (`{`and `}`). Almost all
of the data in this file is stored in this list.

Each dictionary in the `data["messages"]` list describes a chat message. This
snippet of code includes only one of the dictionaries, the ninth chat
message in the list (I snipped out the first eight messages, so you
can't tell that it's the ninth without looking at the original file).
You can access the dictionary that contains that specific chat message
using the expression `data["messages"][8]`. (Remember, in programming we start
counting at 0, not 1, so the first item is at index 0, the second item
is at index 1, and so on.) If you run the command
`print(data["messages"][8])`
to display the dictionary for the ninth message, the
output should match the message in the listing. Notice that just as you
place index numbers within brackets to select from lists, you place keys
within brackets to select from dictionaries, like `["messages"]` or `["success"]`.

You can also access the value of the `success` key with `data["success"]`. Its value is the Boolean
`True` ❷. I'm not entirely sure what this means, but I
suspect that the `success` key
was left over from whatever system the Ukrainian researcher used to
export these chat messages from RocketChat, confirming that exporting
the data was successful and that there were no errors.

The file from which I loaded this code contained 604 different chat
messages, each in its own dictionary, that were sent in Conti's
\#general RocketChat channel on February 24, 2022. I discovered that
this list has 604 items by measuring its length with the `len()` function, like this:

```py
>>> len(data["messages"])
604
```

The dictionary for each chat message has many keys: `_id`, `rid`, `msg`, `u`, `urls`, and so on.

You can find out what types of data these keys contain using the
`for key_variable in dictionary` syntax, and you can determine
a variable's data type using the `type()` function. Try this out using the
following commands:

```py
>>> for key in data["messages"][8]:
...     print(f"{key}: {type(data['messages'][8][key])}")
...
```

This command loops through the `data["messages"][8]` dictionary and stores each key in the
`key` variable. Then, using
the `print()` function and an
f-string, it displays the key (`key`) and the type of data stored in that
key, as shown in the following output:

```
_id: <class 'str'>
rid: <class 'str'>
msg: <class 'str'>
ts: <class 'str'>
u: <class 'dict'>
urls: <class 'list'>
mentions: <class 'list'>
channels: <class 'list'>
md: <class 'list'>
_updatedAt: <class 'str'>
```

In the output, the values at the `_id`, `rid`, `msg`, `ts`, and `_updatedAt` keys are all strings. The value at the
`u` key is a dictionary. The
value at the `urls`,
`mentions`, `channels`, and `md` keys are lists.

You can get the value of the data at the key using
`data['messages'][8][key]`.
Remember that to retrieve the value of a key in a dictionary, you put
the key in square brackets. In this case, the key itself is stored in
the variable `key`, so you can
get its value by putting `key`
inside the square brackets. To find
out what type of data that is, then, just pass the value into the
`type()` function.



#### Selecting Values in Dictionaries and Lists

When working with datasets, you often end up with structures like this:
a mess of dictionaries and lists that you need to make sense of. Being
able to select the exact values you're looking for is an important
skill. To practice navigating through dictionaries and lists, take a
closer look at the value of just one of these keys, the `md` key, by running the following command:

```py
>>> print(data["messages"][8]["md"])
```

In the output, you can tell that this value is a list because it's
surrounded by square brackets:

```py
[{'type': 'PARAGRAPH', 'value': [{'type': 'PLAIN_TEXT', 'value': 'Некоторые американские сенаторы предлагают помимо соцсетей блокировать в России ещё и PornHub!'}]}]
```

The list's single item is a dictionary, which is surrounded by braces.
The dictionary has a `type`
key whose value is `PARAGRAPH`, as well as a `value` key. The value of `value` is another list with one item
containing another dictionary; that dictionary itself contains
`type` and `value` keys, where the value of
`type` is `PLAIN_TEXT`.

These data structures can have as many sublists and subdictionaries as
you'd like. To select specific values, after the `data` variable keep adding square brackets
containing an index (if it's a list) or a key (if it's a dictionary)
until you get to the value you're looking for. For example, use the
following command to access the value of the `value` key in the inner dictionary within the
inner list, which is in another `value` key in the outer dictionary in the
outer list:

```py
>>> print(data["messages"][8]["md"][0]["value"][0]["value"])
```

You already know that `data["messages"][8]` is a dictionary that represents a chat
message. To find the value of the `md` key in that dictionary, you
include`["md"]` in the
command. As you can tell from inspecting the structure in Listing 8-2, this is a list with one item, so adding
`[0]` selects that item. This
item is a dictionary, and you select the value of its `value` key by adding `["value"]`. This item is another list with one
item, so you again add `[0]`
to select that one item. This is yet another dictionary, so you can
select the value of the final inner `value` key by adding another
`["value"]`.

You should get the following output:

```
Некоторые американские сенаторы предлагают помимо соцсетей блокировать в России ещё и PornHub!
```

In English, the message that you just displayed says, "Some American
Senators suggest blocking PornHub in Russia in addition to social
networks!" It was posted right after Russia started its invasion of
Ukraine, and US and European leaders
immediately began imposing economic sanctions on Russia. After invading
Ukraine, the Russian government censored access to Twitter and Facebook
from the Russian internet. Rumors spread that PornHub, a popular
American porn website, would block access to Russian users (though this
didn't happen). This same user followed up their first post with "That's
it, we're done," and then "They will take away our last joys!"



#### Analyzing Data Stored in Dictionaries and Lists

Whenever I work with any sort of structured data, I find myself looping
through a list of dictionaries and selecting specific pieces of data. As
long as you understand its structure, you can write your own similar
code to quickly pull out the relevant information, no matter what
dataset you're working with. For example, you might want to view the
chat logs in the format `timestamp username``: message` in order to hide the
unimportant sections of data so that you can directly copy and paste the
relevant parts into machine translation systems like DeepL or Google
Translate. Run the following commands to display all of the messages in
`data["messages"]` in that
format:

```py
>>> for message in data["messages"]:
...     print(f"{message['ts']} {message['u']['username']}: {message['msg']}")
...
```

You should get the following output:

```
--snip--
2022-02-24T22:02:49.448Z thomas: последние радости у нас заберут
2022-02-24T22:02:44.463Z thomas: ну все, приплыли)
2022-02-24T22:02:38.276Z thomas: Некоторые американские сенаторы предлагают помимо соцсетей
блокировать в России ещё и PornHub!
2022-02-24T22:00:00.347Z thomas:
2022-02-24T21:58:56.152Z rags: угу :(
--snip--
```

Since `data["messages"]` is a
list, each time the `for` loop
in this command runs, it updates the value of the `message` variable to a different item in that
list. In this case, each item is a different dictionary. Inside the
`for` loop, the
`print()` function displays
three values: the timestamp (`message['ts']`), the username
(`message['u']['username']`),
and the message itself (`message['msg']`).

You can change this command to display whatever information you'd like
from each message. Maybe you're interested is the user's ID rather than
their username. In that case, you could display
`message['u']['_id']`.

The previous output shows the same messages about PornHub just
discussed, as well as a message posted just before that from another
user, `rags`. If you're
interested in seeing only the messages posted by `rags`, view those by running the following
commands:



```py
>>> for message in data["messages"]:
...     if message["u"]["username"] == "rags":
...         print(f"{message['ts']} {message['u']['username']}: {message['msg']}")
...
```

This code is similar to the previous example. A `for` loop loops through each message in
`data["messages"]`, and then a
`print()` statement displays
specific pieces of information from that message. This time, though,
each loop also contains an `if` statement. Each time the code finds
another message, it checks to see if the username is `rags` and, if so, displays the message.
Otherwise, it moves on to the next message. You should get the following
output:

```
2022-02-24T22:08:49.684Z rags: давай бро спокойной ночи
2022-02-24T22:03:50.131Z rags: сча посмотрю спасиб =)
2022-02-24T21:58:56.152Z rags: угу :(
--snip--
```

Finally, suppose you want to figure out how many messages each person
posted, perhaps to find the most active poster in the \#general chatroom
on this day. The simplest way to do this is to create a new empty
dictionary yourself and then write code to fill it up. Run the following
command to create an empty dictionary called `user_posts`:

```py
>>> user_posts = {}
```

The keys in this dictionary will be usernames, and the values will be
the number of posts from that user. Fill up the `user_posts` dictionary with the following code:

```py
>>> for message in data["messages"]:
...     username = message["u"]["username"]
...     if username not in user_posts:
...         user_posts[username] = 1
...     else:
...         user_posts[username] += 1
...
>>>
```

Again, this code uses a `for`
loop to loop through the messages. Next, it defines the
`username` variable as
`message["u"]["username"]`,
the username of the person who posted the message the code is currently
looping through. Next, using an `if` statement, the code checks to see if
this username is already a key in the `user_posts` dictionary. (It's not checking to see
if the string `username` is a
key, but rather if the *value* of the `username` variable, like `thomas` or `rags`, is a key.)

If this user doesn't exist in the `user_posts` dictionary, the program adds a key to
this dictionary and sets the value at that key to `1`, with the line
`user_posts[username] = 1`. Otherwise, it increases the value by
1, with `user_posts[username] += 1`. By the time the `for` loop finishes running, the
`user_posts` dictionary should
be complete. The keys should be all of the usernames found in the
messages, and the values should be the total number of messages for that
user.

Use the following code to display the information inside the
`user_posts` dictionary,
viewing the data you just collected:

```py
>>> for username in user_posts:
...     print(f"{username} posted {user_posts[username]} times")
...
```

You should get the following output:

```
weldon posted 64 times
patrick posted 62 times
rags posted 38 times
thomas posted 58 times
ryan posted 2 times
kermit posted 151 times
biggie posted 39 times
stanton posted 12 times
angelo posted 102 times
Garfield posted 61 times
jaime posted 2 times
grem posted 5 times
jefferson posted 1 times
elijah posted 6 times
chad posted 1 times
```

These are the users who posted in Conti's \#general chatroom, in their
RocketChat server, on the day Russia invaded Ukraine in 2022. The user
*kermit* posted 151 times, more than any other user.

In these examples, you looped through hundreds of chat messages, but the
same concepts would work with millions or billions of messages or with
data representing any sort of information.

> ##### REVELATIONS IN THE CONTI DATASET
> 
> This dataset includes far more chat logs than just a few messages worrying about a porn site getting blocked. The example I used in this section included the chat logs for the #general channel for a single day, but the logs for this RocketChat server span from July 24, 2021, to February 26, 2022. The leak also includes many logs from the chat service known as Jabber, including some where Conti hackers discuss hacking a contributor to the OSINT-based investigative journalism group Bellingcat. The hackers were hoping to find information about Alexei Navalny, the imprisoned Russian opposition leader who survived an FSB assassination attempt.
> 
> The anonymous Ukrainian researcher who leaked the Conti dataset told CNN, “I cannot shoot anything, but I can fight with a keyboard and mouse.” According to CNN, a few weeks after leaking the data, the researcher successfully slipped out of Ukraine during Russia’s invasion, laptop in hand.
> 
> From reading the chat logs, I learned that many of the Conti hackers are Russian ultranationalists. Many of them believe Putin’s conspiratorial lies about Ukraine, like that it’s run by a “neo-Nazi junta,” while at the same time making antisemitic comments about Volodymyr Zelenskyy, Ukraine’s Jewish president. You can see my full reporting on this dataset at [https://theintercept.com/2022/03/14/russia-ukraine-conti-russian-hackers/](https://theintercept.com/2022/03/14/russia-ukraine-conti-russian-hackers/).

In this section, you learned how to work with flexible data structures
that combine dictionaries and lists, including how to pick out specific
elements that you're interested in and how to quickly traverse them by
looping through them. These skills will often prove useful when you're
writing Python scripts to help you analyze data.

Now that you're familiar with data structures that combine dictionaries
and lists, it's time to create your own to map out the CSV files in
BlueLeaks.




### Exercise 8-5: Map Out the CSVs in BlueLeaks

Each folder in BlueLeaks includes data from a single hacked law
enforcement website in the form of hundreds of CSV files. These files
contain some of the most interesting information in all of BlueLeaks,
such as the contents of bulk email that fusion centers sent to local
cops, or "suspicious activity reports." In this exercise, you'll
construct a map of the contents of the dataset.

By manually looking in different BlueLeaks folders, I noticed that each
folder seems to have a file called *Company.csv* (each containing
different content), but only one folder, *ncric*, has a file called
*911Centers.csv*. Clearly, not all of the BlueLeaks sites have the same
data. Which CSV files are in every folder in BlueLeaks, which are in
some folders, and which are unique to a single folder? Let's write a
Python script to find out.

As with most programming problems, there are multiple ways you could
write a script that answers this question. If you feel comfortable
enough with Python by now that you'd like a challenge, try writing one
on your own. Otherwise, follow along with this exercise. Either way, the
program must meet the following requirements:

-   Make the script accept an argument called `blueleaks_path` using Click.
-   Create an empty dictionary called `csv_to_folders`. Your script should fill this
    dictionary with data. The keys should be CSV filenames,
    and the values should be lists of BlueLeaks
    folders that contain this CSV.
-   Loop through all of the files and folders in
    `blueleaks_path`. For each
    folder, loop through all of the files it contains. For each CSV
    file, add data to the `csv_to_folders` dictionary.
-   Display the contents of the `csv_to_folders` dictionary.

In each step that follows, I'll quote a snippet of code, explain how it
works, and give you a chance to run it as is. You'll then add more
features to that code and run it again. It's good practice to write code
in small batches, pausing frequently to test that it works as you
expect. This will help you catch bugs early, making the process of
debugging much simpler.


#### Accept a Command Line Argument

Create an *exercise-8-5.py* file and enter the Python template:

```py
def main():
    pass

if __name__ == "__main__":
    main()
```

Next, instead of hardcoding the path to the BlueLeaks data like you did
in Exercise 8-2, let's use Click to pass in the path as a command line
argument, `blueleaks_path`. To
do so, make the following modifications to your code (the added syntax
is highlighted in bold):

```py
import click

@click.command()
@click.argument("blueleaks_path")
def main(blueleaks_path):
    """Map out the CSVs in BlueLeaks"""
    print(f"blueleaks_path is: {blueleaks_path}")

if __name__ == "__main__":
    main()
```

This code modifies the template to import the `click` module, adds the correct decorators
before the `main()` function,
adds the `blueleaks_path`
argument to the `main()`
function, and adds a simple docstring to the `main()` function so that running this script
with `--help` will be more
useful. Finally, it includes a line to display the value of
`blueleaks_path`, so that you
can confirm the code is working when you run it.

Try running your script with `--help` to see if the help text works, and
with a value for `blueleaks_path` to see if the argument is successfully
sent to the `main()` function:



```
micah@trapdoor chapter-8 % python3 exercise-8-5.py --help
Usage: exercise-8-4.py [OPTIONS] BLUELEAKS_PATH

  Map out the CSVs in BlueLeaks

Options:
  --help  Show this message and exit.
micah@trapdoor chapter-8 % python3 exercise-8-5.py test-path
blueleaks_path is: test-path
```

If your output looks like this, everything is working correctly so far.



#### Loop Through the BlueLeaks Folders

Now that you can use the `blueleaks_path` CLI argument, make the following
modifications to your code to have it loop through all of the folders it
finds in that path:

```py
import click
import os

@click.command()
@click.argument("blueleaks_path")
def main(blueleaks_path):
    """Map out the CSVs in BlueLeaks"""
    for folder in os.listdir(blueleaks_path):
        blueleaks_folder_path = os.path.join(blueleaks_path, folder)

        if os.path.isdir(blueleaks_folder_path):
            print(f"folder: {folder}, path: {blueleaks_folder_path}")

if __name__ == "__main__":
    main()
```

First, you import the `os`
module in order to be able to list all of the files in the
*BlueLeaks-extracted* folder using the `os.listdir()` function. Inside the `main()` function, a `for` loop loops through the return value of
`os.listdir (blueleaks_path)`,
the list of filenames inside the folder at `blueleaks_path`.

Inside the loop, the code defines `blueleaks_folder_path` as the path of the specific BlueLeaks
folder for the current loop. For example, if the value of
`blueleaks_path` is
*/Volumes/datasets/BlueLeaks-extracted*, and at this point in the
`for` loop, the value of
`folder` is *icefishx*, then
the value of `blueleaks_folder_path` will be
*/Volumes/datasets/BlueLeaks-extracted/icefishx*.

You want to look inside subfolders in the *BlueLeaks-extracted* folder,
not inside files. If there are any files in that folder, you want to
skip them. To meet these requirements, the code includes an `if` statement that checks whether
`blueleaks_folder_path` is
actually a folder. Finally, the code displays the current value of
`folder` and
`blueleaks_folder_path`.

Run your script again. This time, pass in the
real path to your *BlueLeaks -extracted* folder:

```
micah@trapdoor chapter-8 % python3 exercise-8-5.py /Volumes/datasets/BlueLeaks-extracted
folder: bostonbric, path: /Volumes/datasets/BlueLeaks-extracted/bostonbric
folder: terrorismtip, path: /Volumes/datasets/BlueLeaks-extracted/terrorismtip
folder: ociac, path: /Volumes/datasets/BlueLeaks-extracted/ociac
--snip--
```

The output should show that the `folder` variable holds just the name of the
folder, like *bostonbric*, and the `blueleaks_folder_path` variable includes the full path to
that folder, like */Volumes/datasets/BlueLeaks-extracted/bostonbric*.
When you run this on your own computer, you may see these values in a
different order than what's shown here.



#### Fill Up the Dictionary

You now have a script that accepts `blueleaks_path` as an argument and then loops through
every folder in that path. Adding the code in bold creates the
`csv_to_folders` dictionary
and starts to fill it up with data:

```py
import click
import os

@click.command()
@click.argument("blueleaks_path")
def main(blueleaks_path):
    """Map out the CSVs in BlueLeaks"""
    csv_to_folders = {}

    for folder in os.listdir(blueleaks_path):
        blueleaks_folder_path = os.path.join(blueleaks_path, folder)

        if os.path.isdir(blueleaks_folder_path):
            for filename in os.listdir(blueleaks_folder_path):
                if filename.lower().endswith(".csv"):
                    if filename not in csv_to_folders:
                        csv_to_folders[filename] = []

                    csv_to_folders[filename].append(folder)

if __name__ == "__main__":
    main()
```

Your goal with this script is to map out which CSV files are in which
BlueLeaks folders. To store this data, the code creates the empty
dictionary `csv_to_folders` at
the top of the `main()`
function. The next step is to fill up that dictionary.

The code loops through all of the filenames in `blueleaks_path`, checking each to see if it's a
folder. Removing the `print()`
statement in the previous iteration of the code, this code instead adds
a second `for` loop that loops
through all of the files in that specific BlueLeaks folder.

In this second `for` loop, an `if` statement checks whether the filename
ends in *.csv*. This `if`
statement calls the `lower()`
method on the `filename`
string, which returns a lowercase-only version of the string. The code
then calls the `endswith()`
method on that lowercase string, which returns a Boolean describing
whether the string ends with the string that was passed in. If the
string `filename` ends with
*.csv*, *.CSV*, or *.cSv*, the `lower()` method will convert the file extension
to *.csv*, and `endswith()`
will return `True`. If
`filename` ends with anything
else, like *.docx*, then `endswith()` will return `False`.

Each time the code following this `if` statement runs, it means the program
has found a CSV (called `filename`) in the current BlueLeaks folder
(called `folder`). You want
`csv_to_folders` to be a
dictionary where the keys are CSV filenames and the values are lists of
folders. This code checks to see if the key `filename` has been created in
`csv_to_folders`, and if it
hasn't, creates it and set its value to an empty list (`[]`). Finally, after the code has
confirmed that the `filename`
key has been created and is a list, it appends the value of
`folder` to that list.

These last lines are tricky, so let's dig in a little more. The first
time the script comes across a CSV filename (like *CatalogRelated.csv*),
the script sets the value of that key in `csv_to_folders` to an empty list. If the same filename
exists in another BlueLeaks folder later on, the expression
`filename not in csv_to_folders` will evaluate to `False` (meaning
`csv_to_folders["CatalogRelated .csv"]` already exists), so the code following
the `if` statement won't run.
Finally, the code appends `folder`, the name of the BlueLeaks folder it's
currently looking in, to the list of folders that include that filename.

Pause and try running the script so far:

```
micah@trapdoor chapter-8 % python3 exercise-8-5.py /Volumes/datasets/BlueLeaks-extracted
```

This should take a moment to run but displays nothing, since you're not
yet using the `print()`
function anywhere. The code is simply creating the
`csv_to_folders` dictionary
and filling it up with data.



#### Display the Output

By the time the previous version of the script runs, the
`csv_to_folders` dictionary
should contain a complete set of CSV filenames, mapped to the BlueLeaks
sites where they were found. The following code should show you what the
program found:

```py
import click
import os

@click.command()
@click.argument("blueleaks_path")
def main(blueleaks_path):
    """Map out the CSVs in BlueLeaks"""
    csv_to_folders = {}

    for folder in os.listdir(blueleaks_path):
        blueleaks_folder_path = os.path.join(blueleaks_path, folder)

          if os.path.isdir(blueleaks_folder_path):
            for filename in os.listdir(blueleaks_folder_path):
                if filename.lower().endswith(".csv"):
                    if filename not in csv_to_folders:
                        csv_to_folders[filename] = []

                    csv_to_folders[filename].append(folder)

    for filename in csv_to_folders:
        print(f"{len(csv_to_folders[filename])} folders | {filename}")

if __name__ == "__main__":
    main()
```

The added code in bold loops through all of the keys (each a CSV
filename) in `csv_to_folders`,
then displays the number of BlueLeaks folders that contain that file
(`len(csv_to_folders[filename])`) along with the filename itself.

You can find this final script at
[https://github.com/micahflee/hacks-leaks-and-revelations/blob/main/chapter-8/exercise-8-5.py](https://github.com/micahflee/hacks-leaks-and-revelations/blob/main/chapter-8/exercise-8-5.py).
When you run it, the output should look like this:

```
micah@trapdoor chapter-8 % python3 exercise-8-5.py /Volumes/datasets/BlueLeaks-extracted
161 folders | CatalogRelated.csv
161 folders | Blog.csv
161 folders | EmailBuilderOptions.csv
--snip--
1 folders | HIDTAAgentCategory.csv
1 folders | Lost.csv
1 folders | AgencyContacts.csv
```

Since this script displays the number of folders at the beginning of
each line of output, you can pipe the output into `sort -n` to sort it numerically in ascending
order, like so:

```
micah@trapdoor chapter-8 % python3 exercise-8-5.py /Volumes/datasets/BlueLeaks-extracted | sort
-n
1 folders | 1Cadets.csv
1 folders | 1Mentors.csv
1 folders | 1Unit.csv
--snip--
161 folders | VideoDownload.csv
161 folders | VideoHistory.csv
161 folders | VideoOptions.csv
```

Most of the CSV files are in either a single folder or all 161 folders.
However, there are a few exceptions: *Donations.csv* should be in 10
folders, *SARs.csv* should be in 25, and so on. This information would
have taken you many hours of busywork to find manually.

At this point, you've learned the basics of navigating the filesystem in
Python. You've seen how to loop through folders using
`os.listdir()`, loop through
entire folder structures using `os.walk()`, and look up information
about the files and folders you find. In the
next section, you'll learn how to actually read the contents of a file
you find and create new files yourself.




### Reading and Writing Files

To follow the rest of this book, you'll need to know one more major
Python concept: how to read and write files. During a data
investigation, you'll almost certainly need to read the contents of
files, especially CSV and JSON files. You'll also probably want to be
able to create new files, by calculating some data of your own and
saving it to a spreadsheet, for example. In this section you'll learn
how to open files and write or read content to them.

In programming, to work with a file, you first need to open it and
specify the *mode*---that is, whether you're planning on *reading* from
or *writing* to this file. To open an existing file and access its
contents, open it for reading using mode `r`. To create a new file and put data in
it, open it for writing using mode `w`.


#### Opening Files

To prepare to work with a file, whether for writing or reading, you use
the built-in Python function `open()`. To open it for reading, you use the
following code:

```py
with open("some_file.txt", "r") as f:
    text = f.read()
```

This code uses a `with`
statement, which tells Python that after the `open()` function is done running, it should
set the variable `f` to that
function's return value. The `f` variable is a *file object*, a type of
variable that allows you to read or write data to a file. The first
argument to the `open()`
function is a path, and the second argument is the mode, which in this
example is `"r"` for reading.

In the code block after the `with` statement, you can call methods on
`f` to interact with the file.
For example, `f.read()` will
read all of the data in the file and return it---in this case, storing
it in the `text` variable.

To open a file for writing, you set the mode to `"w"` like so:

```py
with open("output.txt", "w") as f:
    f.write("hello world")
```

The `open()` function returns
the file object `f`. To write
data into the file, you can use the `f.write()` method. Here, this code is opening a
file called *output.txt* and writing the string `hello world` to it.

In the next two sections, you'll learn more about using
`f.write()` to write to files
and `f.read()` and
`f.readlines()` to read from
files.



#### Writing Lines to a File

Text files are made up of a series of individual characters. Consider a
text file with these contents:

```
Hello World
Hola Mundo
```

You could also represent the entire contents of this file as a Python
string:

```
"Hello World\nHola Mundo\n"
```

The first character of the string is `H`, then `e`, then `l`, and so on. The 12th character
(counting the space), `\n`, is
a special character known as a *newline* that represents a break between
lines. As with shell scripting, the backslash is the escape character in
Python, so a backslash followed by another character represents a single
special character.

Newlines are used to write lines to a file. Try running these commands
in your Python interpreter:

```py
>>> with open("output.txt", "w") as f:
...     f.write("Hello World\n")
...     f.write("Hola Mundo\n")
...
12
11
```

The `12` and `11` in the output represent the number of
bytes written. The first `f.write()` call wrote 12 bytes, because the
string `Hello World` takes 11
bytes of memory: it has 11 characters, plus 1 for the newline character.
The second call wrote 11 bytes, since `Hola Mundo` takes 10 bytes of memory, plus 1 for
the newline character.

In your terminal, use the following command to view the file you just
wrote:

```
micah@trapdoor ~ % cat output.txt
Hello World
Hola Mundo
```

If you had written the same code but without the newlines, the output
would have been `Hello WorldHola Mundo`, with no line breaks.



#### Reading Lines from a File

Run the following command to read the file you just created:

```py
>>> with open("output.txt", "r") as f:
...     text = f.read()
...
```

This code reads all of the data from the file
and saves it in the string `text`. In fact, this might look familiar:
earlier in this chapter, in the Exploring Dictionaries and Lists Full
of Data in Python section, we used similar code to load the
leaked Conti chat logs into a Python dictionary.

Since splitting text files into multiple lines is so common, file
objects also have a convenient method called `readlines()`. Instead of reading all of the data
into a file, it reads only one line at a time, and you can loop over the
lines in a `for` loop. Try
this out by running the following commands:

```py
>>> with open("/tmp/output.txt", "r") as f:
...     for line in f.readlines():
...         print(line)
...
Hello World

Hola Mundo
```

This code opens the file for reading, then loops through each line in
the file. Each line is stored in the variable `line`, then displayed with the
`print()` function. Because
the `line` variable in each
loop ends in `\n` (for
example, the first line is `Hello World\n`, not `Hello World`), and the `print()` function automatically adds an extra
`\n`, the output shows an
extra hard return after each line.

If you don't want to display these extra newlines, you can use the
`strip()` method to get rid of
any whitespace (spaces, tabs, or newlines) from the beginning and end of
the string. Run the same code, but this time strip out the newline
characters on each line:

```py
>>> with open("/tmp/output.txt", "r") as f:
...     for line in f.readlines():
...         line = line.strip()
...         print(line)
...
Hello World
Hola Mundo
```

You'll practice the basics of how to read and write files in Python in
the following exercise.




### Exercise 8-6: Practice Reading and Writing Files

In Exercise 7-5, you wrote a function that converts a string to an
alternating caps version, like `This book is amazing` to `ThIs bOoK Is aMaZiNg`. To practice your newfound reading and
writing files, in this exercise, you'll write a script to create an
alternating caps version of all of the text in an entire text file.

If you'd like a challenge, you can try
programming your own script to meet the following requirements:

-   Accepts two arguments, `input_filename` and `output_filename`, using Click
-   Opens the file `input_filename` for reading and loads its contents
    into the string `text`
-   Opens the file `output_filename` for writing and saves the
    alternating caps version of `text` to that new file

Otherwise, follow along with my explanation of the following code, which
implements this iNcReDiBlY uSeFuL command line program.

Start by copying the `alternating_caps()` function that you wrote in Exercise
7-5 into a new Python script called *exercise-8-6.py*. Next, make the
modifications highlighted in bold here (or copy the final script at
[https://github.com/micahflee/hacks-leaks-and-revelations/blob/main/chapter-8/exercise-8-6.py](https://github.com/micahflee/hacks-leaks-and-revelations/blob/main/chapter-8/exercise-8-6.py)):

```py
import click

def alternating_caps(text):
    """Returns an aLtErNaTiNg cApS version of text"""
    alternating_caps_text = ""
    should_be_capital = True

    for character in text:
        if should_be_capital:
            alternating_caps_text += character.upper()
            should_be_capital = False
        else:
            alternating_caps_text += character.lower()
            should_be_capital = True

    return alternating_caps_text

@click.command()
@click.argument("input_filename")
@click.argument("output_filename")
def main(input_filename, output_filename):
    """Converts a text file to an aLtErNaTiNg cApS version"""
    with open(input_filename, "r") as f:
        text = f.read()

    with open(output_filename, "w") as f:
        f.write(alternating_caps(text))

if __name__ == "__main__":
      main()
```

This code first imports the `click` module, used for the arguments, and
then defines the `alternating_caps()` function. Again, the `main()` function is a Click command, but this
time it takes two arguments, `input_filename` and `output_filename`.

Once the `main()` function runs, the section for reading
and writing files runs. The code opens `input_filename` for reading and loads all of the
contents of that file into the string `text`. It then opens
`output_filename` for writing
and saves the alternating caps version of that string into the new file.
It does so by running `alternating_caps(text)`, which takes `text` as an argument and returns its
alternating caps version, and then passes that return value directly
into `f.write()`, writing it
to the file.

To demonstrate how this script works, try running it on the famous "To
be, or not to be" soliloquy from *Hamlet*. First, save a copy of the
soliloquy found at
[https://github.com/micahflee/hacks-leaks-and-revelations/blob/main/chapter-8/shakespeare.txt](https://github.com/micahflee/hacks-leaks-and-revelations/blob/main/chapter-8/shakespeare.txt)
to a file called *shakespeare.txt*. Here are the original contents of
*shakespeare.txt*, displayed using the `cat` command:

```
micah@trapdoor chapter-8 % cat shakespeare.txt
To be, or not to be, that is the question:
Whether 'tis nobler in the mind to suffer
The slings and arrows of outrageous fortune,
Or to take Arms against a Sea of troubles,
And by opposing end them: to die, to sleep
No more; and by a sleep, to say we end
--snip--
```

Next, pass that filename into your script to create an alternating caps
version of that file. Here's what happens when I do it:

```
micah@trapdoor chapter-8 % python3 exercise-8-5.py shakespeare.txt shakespeare-mocking.txt
micah@trapdoor chapter-8 % cat shakespeare-mocking.txt
To bE, oR NoT To bE, tHaT Is tHe qUeStIoN:
wHeThEr 'TiS NoBlEr iN ThE MiNd tO SuFfEr
tHe sLiNgS AnD ArRoWs oF OuTrAgEoUs fOrTuNe,
Or tO TaKe aRmS AgAiNsT A SeA Of tRoUbLeS,
aNd bY OpPoSiNg eNd tHeM: tO DiE, tO SlEeP
No mOrE; aNd bY A SlEeP, tO SaY We eNd
--snip--
```

First, I ran the script, passing in *shakespeare.txt* as
`input_filename` and
*shakespeare-mocking.txt* as `output_filename`. The script itself displayed no output
(it doesn't include any `print()` statements), but it did create a new
file. I then used `cat` to
display the contents of that new file, which is indeed an alternating
caps version of Hamlet's soliloquy.



### Summary

Congratulations on making it through a crash course in the fundamentals
of Python programming! You've learned how to bring extra functionality
to your scripts with built-in and third-party Python modules. You've
also learned how to make your own CLI programs using Click, how to write
code that traverses the filesystem, how to work with structured data
using dictionaries and lists, and how to read and write files.

You'll use these skills throughout the
following chapters as you dig through various datasets, uncovering
revelations you'd never discover otherwise. In the next chapter, you'll
write Python programs that loop through rows in the BlueLeaks CSV
spreadsheets, transforming the data into a more workable format. You'll
get practice writing the content of law enforcement bulk email messages
to files, and you'll use Python to create your own CSV spreadsheets.
