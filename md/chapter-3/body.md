If you’re like most people, you interface with your computer primarily via its graphical desktop environment: you move the pointer with your mouse or trackpad and click on icons to run programs and open documents. Programs open in windows that you can resize, maximize, minimize, and drag around the screen. You can run various programs at once in separate windows and switch between them. However, there’s an alternate, incredibly powerful interface you can use to communicate with your computer and give it instructions: the command line interface (CLI).

CLIs are text-based, rather than graphical, interfaces to using your computer. Instead of clicking on icons, you run programs by typing commands. After running a command, the CLI will typically show you text-based output from that command. To use the CLI on your computer, you open a terminal emulator (normally referred to as a terminal), which is a CLI running inside of a graphical window.

In this chapter, you’ll learn about using terminals and CLIs. Whether you’re using Windows, macOS, or Linux, you’ll learn how to install and uninstall software using the CLI, how file paths work, how to navigate around the folders on your computer, and how to use text editors. You’ll also write your first shell script, a file containing a series of CLI commands that you can run all at once. Shell scripts let you to automate common tasks. Instead of manually doing the same task over and over again, such as creating a backup of your work, you can just do it once in a script and then simply run your script whenever you need to do that task.

When learning command line skills, you can always look things up if you run into problems—I still do this every day. You’re likely not the first person to encounter any given command line issue, so with a few well-worded internet searches, you can find someone else’s solution.
You’ll need to be comfortable with command line basics to follow along with the rest of the book. You’ll get the most out of this chapter if you’re adventurous. While you’re reading, keep a terminal open, test out all the new commands I introduce, and do all of the homework assignments designed for your OS.

### Introducing the Command Line

In this section, I’ll explain what shells are, how users and paths work in different operating systems, and the concept of privilege escalation (running commands as a user with more permissions that you normally have), preparing you to start working on the command line.

### The Shell

The shell is the program that lets you run text-based commands, while the terminal is the graphical program that runs your shell. When you open a terminal and see a blinking text cursor waiting for commands, you’re using a shell. When hackers try to break into a computer, their initial goal is to “pop a shell”—to get access to the text-based interface that allows them to run whatever commands they want.

All operating systems, even mobile ones like Android and iOS, have shells. Different types of shells have different features. It’s possible to run different shells in the same terminal window, but most people just stick with their OS’s default shell. This book focuses on Unix shells, the kind that come with macOS and Linux. Most versions of Linux use a shell called bash, and macOS uses one called zsh. These shells are very similar, and for the purposes of this book you can think of them as the same thing.

Windows, on the other hand, is a different beast. It comes with two shells, an older one called Command Prompt (or cmd.exe) and a newer one called PowerShell. The syntax—the rules that define what different commands mean—that Windows shells use is very different from the syntax of Unix shells like bash and zsh. If you’re a Windows user, you’ll make light use of these shells, but mostly you’ll do work in a Unix shell as well. Setting up your computer so you can run Linux directly in Windows will be your first homework assignment.
To make your shell do something, like run a program, you carefully enter the correct command and then press ENTER (or RETURN on Mac keyboards—these keys are used interchangeably). To quit the shell, enter exit and press ENTER. Shells are very finicky: commands need to be entered using the correct capitalization, punctuation, and spacing, or they won’t work. Typos usually result in nothing more serious than error messages, though, and it’s easy to go to back to previous commands you ran and fix them. I’ll explain how to do this later in the chapter.

### Users and Paths

Although operating systems like Windows, macOS, and Linux are different in some ways, they all share basic concepts which you’re likely somewhat familiar with already, including users and paths. 
All OSes have users, separate accounts that different people use to log into the same computer. Users generally have home folders, also known as home directories, where each user’s files live. Figure 3-1 shows a screenshot of a terminal in Ubuntu, a type of Linux OS. My username is micah and the name of my Ubuntu computer is rogue. Your terminal will look different depending on your operating system, your username, and the name of your computer.
[f04001.png]

<<Screenshot showing the terminal app in Ubuntu.>>

Figure 1-1 A terminal in Ubuntu
All OSes also have filesystems, the collection of files and folders available on the computer. You briefly learned about filesystems in Chapter 1 while you were encrypting your USB disk. In a filesystem, each file and folder has a path, which you can think of kind of like the location, or address, of that file.
For example, if your username is alice, here’s the path of your home folder in different OSes:

Windows: C:\Users\alice
macOS: /Users/alice
Linux: /home/alice

Windows filesystems operate differently from from macOS or Linux filesystems in a few key ways. First, in Windows, disks are labeled with letters, and the main disk in which Windows itself is installed is called C: drive (C:)—other disks, like USB disks, get assigned other letters. In Windows, folders in a path are separated with a backslash (\), while the rest of computing uses forward slashes (/). In macOS and Linux, paths are case-sensitive, but not so in Windows. For example, in macOS you can store one file called Document.pdf and another called document.pdf in the same folder. If you try to do the same in Windows, saving the second file will overwrite the first.
It’s important to understand how to read paths when using the CLI for data science since you’ll need to include the location of your dataset or files inside your dataset in the commands you run. If you download a file called Meeting Notes.docx into the Downloads folder, and your username is alice, these are the paths to that file in different OSes:

Windows: C:\Users\alice\Downloads\Meeting Notes.docx
macOS: /Users/alice/Downloads/Meeting Notes.docx
Linux: /home/alice/Downloads/Meeting Notes.docx

When you plug in a USB disk, the OS mounts it to different paths in different OSes. If your disk is labeled datasets, the path that represents the location of that disk might look like this in different OSes:

Windows: D: (or whatever drive letter Windows decides to mount the disk to)
macOS: /Volumes/datasets
Linux: /media/alice/datasets

Different users have different privileges on your OS. To do something that your current user doesn’t have permissions to do, like install new software or access protected files, you’ll need to elevate your user privileges with the sudo command.

### Running Commands With Higher Privileges

Most users have limited privileges in an OS. However, the root user in Linux and macOS and the administrator user in Windows have absolute power. While alice may not be able to save files into bob’s home folder, for example, the root user has permissions to save files anywhere on the computer. When macOS machines ask you to enter your user password to change system preferences or install software, or when a Windows alert asks if you want to allow a program to make changes to your computer, the OS is asking your consent before switching from your unprivileged user account to the root or administrator user account. To run a command as the root user, you use a special command called sudo.

Most of the time that you have a terminal open, you run commands as an unprivileged user. To run a command as root in Linux and macOS, such as to install a new program, just put sudo in front of it, hit ENTER, and you’ll be prompted to enter the password of your regular user. As an example, the whoami command tells you which user just ran that command. On my computer, if I enter whoami without sudo, the output is is micah. However, if I enter while the output of sudo whoami, which requires me to enter the root password, the output is root:

```
micah@rogue:~$ whoami
micah
micah@rogue:~$ sudo whoami
[sudo] password for micah:
root
```

If you recently ran sudo, you can run it again without having to enter your password again until a few minutes have passed.

WARNING	Be very careful when running commands as root, since running the wrong commands as root user can accidentally delete all of your data or break your OS. Before using sudo, make sure you have a clear understanding of what you’re about to do.

You can only use sudo to gain root access if your current user has administrator access. If you’re the only user on your computer, you’re probably an administrator. The simplest way to find out is to just try using sudo and see whether you get a permission denied error.

Figure 3-2 shows a comic by Randall Monroe from his website XKCD that succinctly demonstrates the power of sudo.

[f04002.png]

<<In this XKCD comic, a person says, “Make me a sandwich.” Another person says, “What? Make it yourself.” The first person says, “Sudo make me a sandwhich.” The other person responds, “Okay.”>>

Figure 1-2 XKCD comic by Randall Monroe, from https://xkcd.com/149/
Before digging into the basics of using the command line, Windows users must install Ubuntu in Windows with Homework 3-1. If you’re a Mac or Linux user, skip to the “Basic Command Line Usage” section on page XX.

### Homework 3-1: Install Ubuntu in Windows

To work with Ubuntu on a Windows machine, you could install both OSes or use a virtual machine within Windows, as mentioned in Chapter 1. However, for our purposes it’s simplest to use the Windows Subsystem for Linux (WSL), a Microsoft technology that lets you run Linux programs directly in Windows. WSL allows you to open an Ubuntu window which will in turn open a bash shell and let you install and run Ubuntu software.

**NOTE**
Technically, WSL actually does use a VM, but it’s fast, managed by Windows, and runs entirely behind the scenes. 
To install WSL, open a PowerShell window as an administrator: click the Start button, search for powershell, right-click on Windows PowerShell, and choose Run as administrator. Then click Yes. Figure 3-3 shows a screenshot of this process, which may look slightly different depending on your version of Windows.

[f04003.png] 
<<Screenshot of opening PowerShell as an administrator in Windows.>>

Figure 1-3 Running a program as an administrator in Windows
In your administrator PowerShell window, enter the following command and press ENTER. (Like other shells, PowerShell can be finicky: enter commands exactly as directed.)

```
wsl --install -d Ubuntu
```

This wsl command installs the Windows Subsystem for Linux feature and downloads and installs Ubuntu Linux on your computer. Your screen should now look something like this:

```
PS C :\Windows\system32> wsl --install -d Ubuntu
Installing: Windows Subsystem for Linux
Windows Subsystem for Linux has been installed.
Downloading: WSL Kernel
Installing: WSL Kernel
WSL Kernel has been installed.
Downloading: GUI App Support
Installing: GUI App Support
GUI App Support has been installed.
Downloading: Ubuntu
The requested operation is succession. Changes will not be effective until the system is rebooted.
PS C:\Windows\system32> 
```

The final line of this output tells you to reboot your computer. Enter exit and press ENTER (or just close the window) to quit PowerShell, then reboot. After you log into Windows again, you should see an Ubuntu window with a prompt asking you to create a new user. This is because the Ubuntu that you just installed needs to keep track of its own users rather than the users that already exist on your Windows computer:

```
Installing, this may take a few minutes...
Please create a default UNIX user account. The username does not need to match your Windows username.
For more information visit: https://aka.ms/wslusers
Enter new UNIX username:
With the Ubuntu terminal window in focus, enter a username (mine is micah) and press ENTER. The terminal should then prompt you to make up a password:
New password:
```

It’s fine to use the same password you use to log into your Windows account, but if you want to create a new one, save it in your password manager. Enter your password and press ENTER. While you’re typing, nothing will appear in the Ubuntu terminal, but don’t worry, it’s working.

The terminal should now prompt you to re-enter your new password; do so and press ENTER. If all goes well, this should drop you into an Ubuntu shell with a prompt and a blinking cursor. My prompt says 

```
micah@cloak:~$ because my username is micah and the name of my Windows computer is cloak:
New password:
Retype new password:
passwd: password updated successfully
Installation successful!
--snip--
micah@cloak:~$
```

Now whenever you need access to a Linux system—to take advantage of tools to explore a new dataset, for instance—just open Ubuntu in your Windows computer. It’s still sometimes useful to use PowerShell. However, from this point onward, when I tell you to open a terminal, open an Ubuntu terminal window unless I specify otherwise.
From within your Ubuntu shell, you can access your Windows disks in the /mnt folder. For example, you can access the C: drive in /mnt/c and D: drive in /mnt/d.  

Let’s say I download a document using my web browser and I want to access it from Ubuntu. Since my username is micah, the path to my Downloads folder in Windows is /mnt/c/Users/micah/Downloads, so the document would be in that folder. If I want to access the BlueLeaks data that I downloaded to my USB disk from Ubuntu, the path to that would be /mnt/d/BlueLeaks, assuming that the USB disk’s drive is D:.
For more details on using Windows and WSL, including information on common problems related to using USB disks in WSL, as well as disk performance issues and various ways to deal with them, check out Appendix A. I recommend waiting until you’ve worked through at least Chapter 4 to start implementing these solutions since the instructions involve some more advanced CLI concepts that won’t be introduced until then.

### Basic Command Line Usage

To get comfortable with the command line, you’ll start by using it to explore the files and folders on your computer. This is a prerequisite to working with datasets, which in the end are just folders full of files and other folders. In this section, you’ll learn how to open a terminal; how to list files in any folder; the difference between relative and absolute paths; how to switch to different folders in your shell; and how to look up documentation on commands from within your terminal.

### Opening, Clearing, and Closing a Terminal

To get started, you’ll need to open a terminal. Skip to the subsection for your OS to learn how. 

### Opening a Windows Terminal

If you’re using Windows, open the Ubuntu app by clicking the Start button in the bottom-left corner of the screen and searching for “ubuntu,” and clicking Ubuntu. You’ll use Ubuntu most often for this book, but you occasionally might also need to open the native Windows terminals as well.

You can open PowersShell and Command Prompt the same way, by clicking Start and searching for them. I also recommend that you check out Microsoft program Windows Terminal, which you can get at https://aka.ms/terminal—after you install it, you open it the same way as well. This app lets you open different terminals in different tabs, and lets you choose between PowerShell, Command Prompt, Ubuntu, and other types of terminals.

However you want to do it, I recommend that you pin your terminal program to your taskbar, because you’ll be using it a lot: right-click on its icon on the task bar and select Pin to taskbar.

### Opening a macOS Terminal

On macOS, open an app called Terminal: open Finder, go to the Applications folder, double-click the Utilities folder, and double-click Terminal. Figure 3-4 shows my macOS terminal running zsh, the default macOS shell. My username is micah, and the name of my Mac is trapdoor.

[f04004.png]

<<Screenshot of the Terminal app in macOS.>>

Figure 1-4 My macOS terminal
I recommend snapping the Terminal app to your dock so you can quickly open it in the future. To do so, after you open Terminal, press CTRL and click on the Terminal icon on your dock, then choose Options4Keep in Dock.

### Opening a Linux Terminal

If you’re using Linux, open an app called Terminal (in most versions of Linux, you can open this program by pressing the Windows key, typing “terminal,” and pressing ENTER). If you’re running Ubuntu (or any other version of Linux that uses the graphical environment called Gnome) I recommend that you make the Terminal app stay on your dock so you can quickly open it in the future. Do this by right-clicking on its icon and selecting Add to Favorites.

### Clearing Your Screen and Exiting the Shell

Sometimes after using the terminal for a while, it’s nice to start fresh, without having to see all the previous commands you ran or their output or error messages. Try out this simple command to declutter your terminal:
```
clear
```

This clears everything off the screen, leaving you with nothing but a blank command prompt. Make sure to only clear your screen if you don’t need to see any of the output of your previous commands, because it will erase all of that. (In the Windows shells Command Prompt and PowerShell, you clear your screen using cls instead of clear.)
When you’re done using the CLI, exit your shell by running:

```
exit
```

You can also exit just by closing the terminal window. If you’re running a program when you close the terminal, that program will quit as well.

### Exploring Files and Directories

When you open a terminal, your shell starts out in your user’s home folder, represented as a tilde (~). Running the command to list files (ls) will show you the files in your home folder. Later on in this section you’ll learn how to change your shell to different folders.
The folder that your shell is currently in is called the current working directory, or just working directory. If you ever forget what directory you’re in, you can always run the pwd command (short for “print working directory”):

```
pwd
```

To start exploring, run the ls command in your terminal, which should list all of the files in your working directory. If there are no files, or if there are only hidden files, ls won’t list anything. To check for hidden files (whose filenames begin with a period on Unix-based systems), modify the ls command using -a (an abbreviated form of --all):

```
ls -a
```

When you add anything to the end of a command, like -a, you’re using a command line argument. Think of arguments as settings that change how the program you’re running will act—in this case, by showing hidden files instead of hiding them, which is the default behavior.
The ls command displays files in such a way as to take up as few lines in your terminal as possible. It’s often useful to display one file per line, though, and to get more information about the files such as their size, the time they were last modified, permissions, and if they’re a folder or not. Use -l (an abbreviated version of --format=long) to format the output as a list. You can use both -a and -l at the same time with -al:

```
ls -al
Running this on my Mac gives me the following output:
total 8
drwxr-x---+ 13 micah  staff   416 Nov 25 11:34 .
drwxr-xr-x   6 root   admin   192 Nov  9 15:51 ..
-rw-------   1 micah  staff     3 Nov  6 15:30 .CFUserTextEncoding
-rw-------   1 micah  staff  2773 Nov 25 11:33 .zsh_history
drwx------   5 micah  staff   160 Nov  6 15:31 .zsh_sessions
drwx------+  3 micah  staff    96 Nov  6 15:30 Desktop
drwx------+  3 micah  staff    96 Nov  6 15:30 Documents
drwx------+  3 micah  staff    96 Nov  6 15:30 Downloads
drwx------+ 31 micah  staff   992 Nov  6 15:31 Library
drwx------   3 micah  staff    96 Nov  6 15:30 Movies
drwx------+  3 micah  staff    96 Nov  6 15:30 Music
drwx------+  3 micah  staff    96 Nov  6 15:30 Pictures
drwxr-xr-x+  4 micah  staff   128 Nov  6 15:30 Public
```

The first column of this output describes the type of file—if it’s a directory (another name for a folder), or if it’s an ordinary file—as well as the file’s permissions. Directories start with d, and ordinary files start with -. The second column represents the number of links that the file has; this isn’t relevant for this book, so don’t worry about it.

The third and fourth columns represent the user and the group that owns the file. In addition to users, OSes also have groups of users which can have their own permissions. For example, in Linux, all users allowed to use sudo are in the sudo group. If you create or download a file, its user and group are normally your username. The fifth column is the file size in bytes. For example, the file called .zsh_history, my output is 2,773 bytes.

The next three columns represent the time the file was last modified, and the final column is the filename.

To see a listing of files in a folder other than the working directory, add the path to that folder to the end of the ls command. For example, this is how I’d create a listing of files in my code/hacks-leaks-and-revelations folder, which contains the files released with this book. You’ll download your own copy of these files in Homework 3-7.

```
micah@trapdoor ~ % ls -la code/hacks-leaks-and-revelations 
total 120
drwxr-xr-x  22 micah  staff    704 Dec 21 14:11 .
drwxr-xr-x  73 micah  staff   2336 Dec  6 16:45 ..
-rw-r--r--@  1 micah  staff   8196 Dec  9 16:12 .DS_Store
drwxr-xr-x  15 micah  staff    480 Dec 21 14:41 .git
-rw-r--r--   1 micah  staff     30 Dec 21 14:22 .gitignore
-rw-r--r--   1 micah  staff  35149 Sep 23 14:54 LICENSE
-rw-r--r--   1 micah  staff   6717 Dec 21 14:17 README.md
drwxr-xr-x   4 micah  staff    128 Sep 23 14:54 appendix-a
drwxr-xr-x   8 micah  staff    256 Dec  9 16:18 appendix-b
drwxr-xr-x   6 micah  staff    192 Dec 21 14:23 chapter-1
drwxr-xr-x   5 micah  staff    160 Dec 21 14:35 chapter-10
drwxr-xr-x  12 micah  staff    384 Dec 21 14:35 chapter-11
drwxr-xr-x  12 micah  staff    384 Dec 21 14:39 chapter-12
drwxr-xr-x   8 micah  staff    256 Nov 23 18:51 chapter-13
drwxr-xr-x   4 micah  staff    128 Dec 21 14:23 chapter-2
drwxr-xr-x  10 micah  staff    320 Dec 21 14:24 chapter-3
drwxr-xr-x  13 micah  staff    416 Dec 21 14:25 chapter-4
drwxr-xr-x  13 micah  staff    416 Dec 21 14:26 chapter-5
drwxr-xr-x  10 micah  staff    320 Dec 21 14:28 chapter-6
drwxr-xr-x  13 micah  staff    416 Dec 21 14:30 chapter-7
drwxr-xr-x  18 micah  staff    576 Dec 21 14:32 chapter-8
drwxr-xr-x  15 micah  staff    480 Dec 21 14:34 chapter-9
```

I use the ls command every time I’m working in a terminal, because it lets me see what files exist in whatever folders I’m interested in.

### Navigating Relative and Absolute Paths

Everything is relative, unless it’s absolute. Or at least, this is true for filesystem paths. Programs often require you to provide paths to files or folders; this happens pretty much whenever you run a program that works with specific files on your computer. For example, the path that I passed into ls in the previous section, code/hacks-leaks-and-revelations, is a relative path—it’s relative to the current working directory, my home folder. The absolute version of that path is /Users/micah/code/hacks-leaks-and-revelations—it will always provide the location of that folder regardless of my working directory.

Relative paths can change: for example, if I changed my working directory from my home folder (/Users/micah) to just /Users, then the relative path to that folder would change to micah/code/hacks-leaks-and-revelations. Absolute paths are always the same. No matter what your working directory is, you can reference a file with an absolute path.

Absolute paths always start with /, which is also known as the root path. If a path doesn’t start with /, then you know it’s a relative path. There are two keywords that represent relative paths to specific folders: . (pronounced “dot”), which is a relative path to the current folder, and .. (pronounced “dot dot”), which is a relative path to the parent folder. A parent folder is the folder that that contains the current folder. For example, the relative path to the parent folder of /Volumes/datasets is /Volumes.

### Changing Directories

You can use the cd command (short for “change directory”) to switch to a different folder; if you run ls again, it will show you the files in that different folder. 

Now that you understand a little about how paths work and how to list the files in a folder, you’re ready to begin using the cd command, which stands for “change directory.” To change your working directory to the folder in a relative or absolute path, run: 

```
cd path
```

For example, say I’m using macOS and have downloaded BlueLeaks to a datasets USB disk plugged into my machine. After opening a terminal, to change my working directory to the BlueLeaks folder, I run:

```
cd /Volumes/datasets/BlueLeaks
```

Alternatively, I could run the following to end up at the same place, assuming I start out in my home folder:

```
cd ../../Volumes/datasets/BlueLeaks
```

The first example uses the absolute path to the BlueLeaks folder, and the second uses the relative path.

Why does the relative path start with ../.. in this example? When I open the terminal, the working directory is my home folder, which in macOS is /Users/micah. The relative path .. would be its parent folder, /Users; the relative path ../.. would be /; the relative path ../../Volumes would be /Volumes; and so on.

As noted earlier, the tilde symbol (~) represents your home folder. No matter what your working directory is, you can run the following to go back to your home folder:

```
cd ~
```

To go to a folder inside your home folder, run cd ~/folder_name. For example, to go to your Documents folder, run:

```
cd ~/Documents
```

Navigating the filesystem like this can require a lot of typing. To speed things up, I’ll introduce tab completion later in this chapter.

### Running the Help Command 

Most commands let you use the argument -h, or --help, which will display detailed instructions explaining what the command does and how to use it. For example, try running:

```
unzip --help
```

This should show you instructions on all of the different arguments that are available to you when using the unzip command, which is used for extracting compressed ZIP files. Here’s the output I got when I ran this command on my Mac:

```
UnZip 6.00 of 20 April 2009, by Info-ZIP.  Maintained by C. Spieler.  Send
bug reports using http://www.info-zip.org/zip-bug.html; see README for details.

Usage: unzip [-Z] [-opts[modifiers]] file[.zip] [list] [-x xlist] [-d exdir]
  Default action is to extract files in list, except those in xlist, to exdir;
  file[.zip] may be a wildcard.  -Z => ZipInfo mode ("unzip -Z" for usage).

  -p  extract files to pipe, no messages     -l  list files (short format)
  -f  freshen existing files, create none    -t  test compressed archive data
  -u  update files, create if necessary      -z  display archive comment only
  -v  list verbosely/show version info       -T  timestamp archive to latest
  -x  exclude files that follow (in xlist)   -d  extract files into exdir
--snip--

```
This output briefly describes what each argument for the unzip command does. For example, if you use the -l argument, the command will show you a list of all of the files and folders inside the ZIP file, but without actually unzipping it.

Many commands also have manuals, otherwise known as man pages, which you can access with the man command. Manuals are sort of like the output of --help, except they tend to go into more details. To read the manual for the unzip command, run:

```
man unzip
The output should look similar to this:
UNZIP(1)                    General Commands Manual                   UNZIP(1) 

NAME 
       unzip - list, test and extract compressed files in a ZIP archive 

SYNOPSIS 
       unzip  [-Z] [-cflptTuvz[abjnoqsCDKLMUVWX$/:^]] file[.zip] [file(s) ...] 
       [-x xfile(s) ...] [-d exdir] 

DESCRIPTION 
       unzip will list, test, or extract files from a  ZIP  archive,  commonly 
       found  on MS-DOS systems.  The default behavior (with no options) is to 
       extract into the current directory (and subdirectories  below  it)  all 
       files  from  the  specified  ZIP archive.  A companion program, zip(1), 
       creates ZIP archives; both programs are compatible with  archives  cre‐ 
       ated  by  PKWARE's  PKZIP and PKUNZIP for MS-DOS, but in many cases the 
       program options or default behaviors differ. 

ARGUMENTS 
       file[.zip] 
              Path of the ZIP archive(s).  If  the  file  specification  is  a 
              wildcard, each matching file is processed in an order determined 
              by the operating system (or file system).  Only the filename can 
 Manual page unzip(1) line 1 (press h for help or q to quit)

```
You can scroll with both up and down arrows and the page up and page down keys, or search the man page by pressing /, then typing a search term. For example, to learn more details about how the unzip command’s -l argument works, press /, enter -l, and press ENTER. This will search the man page for -l and bring you to the first time it finds it. Press n to move on to the next occurrence of your search term.
When you’re finished, quit the man page by pressing q. As always, you can turn to an internet search if you need more information about any command, or about how to do anything in the shell not covered in this book.

### Tips for Navigating the Terminal

This section introduces ways to make working on the command line more convenient and efficient, along with tips for avoiding and fixing errors. It also shows how to handle problematic filenames, such as those with spaces, quotes, or other special characters. Having a decent understanding of these concepts will save you a lot of time in the future.

### Entering Commands with Tab Completion

Carefully typing exact commands and paths can be tedious and typo-prone. Fortunately, shells have a feature called tab completion that reduces the tedium and saves time: enter the first few letters of a command or a path, then press TAB. If your shell can, it will fill in the rest. 

For example, both macOS and Ubuntu come with a program called hexdump. In a terminal, enter hexd and press the TAB key. This should automatically fill in the rest of the full hexdump command. This also works for paths. For example, unix-like OSes use the /tmp folder to store for temporary files. Enter ls /tm, then press TAB. Your shell should finish it for you, typing out ls /tmp/.

What if you enter the first couple letters of a command or a path and there’s more than one option? Assuming that you have both Downloads and Documents folders in your home folder, try typing ls ~/Do and press TAB. You’ll probably hear a quiet beep, meaning that the shell doesn’t know how to proceed. Press TAB one more time, and it should display the options, like this:

```
micah@trapdoor tmp % ls ~/Do
Documents/  Downloads/
```

If you enter a c, so that your command so far is ls ~/Doc, and press TAB, it will complete to ls ~/Documents/. But if you enter a w, so that your command so far is ls ~/Dow, and press TAB, it should complete to ls ~/Downloads/.

If you have already typed out the path of a folder, you can also press TAB to list files in that folder, or to automatically complete the filename if there’s only one file in the folder. For example, say I have a USB disk called datasets, on which I’ve downloaded BlueLeaks, plugged into my Ubuntu computer. If I want to change to my BlueLeaks folder, I can enter the following and press TAB:

```
cd /Vo
This completes the command to:
cd /Volumes/
```

I press TAB again, and my computer beeps and lists the folders in /Volumes, which is my case are Macintosh HD and datasets. I type d, so my command is cd /Volumes/d, and press TAB, and it completes the command to:

```
cd /Volumes/datasets/
```

I press TAB again. My computer beeps again, and lists all of the files and folders in my datasets USB disk. I enter B (the first letter of BlueLeaks), and press TAB, which gives me:

```
cd /Volumes/datasets/BlueLeaks/
```

Finally, I press ENTER to change to that folder. To recap, instead of having to enter that whole path, I simply entered cd /Vo<TAB>d<TAB>B<TAB>, and my shell filled in the rest for me.

### Editing Commands

You can also edit commands in the CLI. If you start typing a command, you can press the left and right arrow keys to move the cursor around in the current command, allowing you to edit it before you run it. If your keyboard has them, you can press HOME to go to the beginning of the line and END to go to the end of it, and if you’re using a Mac, you can do the same by press FN-LEFT arrow and FN-RIGHT arrow. You can also cycle between commands you’ve already run, using the up and down arrows. If you just ran a command and want to run it again, or modify it and then run it, press the up arrow to return to it. Once you find the command you’re looking for, use the arrow keys to move your cursor to the right position to alter the command, and then press ENTER to run it again.

For example, I frequently run commands that give me a permission denied error because I accidentally ran them as my unprivileged user, when I should have run them as root. When this happens, I press the up arrow, then the HOME key to go to the beginning of the line (if you’re using a Mac, press FN-left arrow), add sudo to the beginning of the command, and press ENTER to successfully run the command.

### Dealing with Spaces in Filenames

In many written human languages, words are separated with spaces. Like, the words in the sentence “the cat drinks water” are “the,” “cat”, “drinks,” and “water.” This is also true in shells, but sometimes filenames have spaces in them too. If you don’t explicitly tell your shell that a space is part of a filename, the shell will assume that the space is there to separate parts of your command. For example, this command lists the files in the Documents folder:

```
ls -lh ~/Documents
```

Under the hood, your shell takes this string of characters and splits it into a list of parts that are separated by spaces: ls, -lh, and ~/Documents. The first part, ls, is the command to run. The rest of the parts are the command’s arguments. The -lh argument tells the program to display as a list and make the file sizes human-readable (this means it will convert the file sizes into larger units that are easier to read, like kilobytes, megabytes, and gigabytes; for example, it will tell you a file is 1.6MB instead of 1,638,890 bytes). The ~/Documents argument means you want to list the files in that folder.
Suppose you want to use the same command to list the files in a folder with a space in its name, like ~/My Documents. You might be tempted to enter this command:

```
ls -lh ~/My Documents
```

But this won’t work. When your shell tries to separate this into parts, it will come up with ls, -lh, ~/My, and Documents. The folder is called ~/My Documents, but the shell sees this as two separate arguments, ~/My and Documents. It will try to list the files in the folder ~/My (which doesn’t exist), then also list files in the folder Documents—which isn’t what you intended. 

There are two ways to solve this problem. The first is to put the name of the folder in quotes:

```
ls -lh "~/My Documents"
```

The shell sees anything within quotes as a single part. In this case, ls is the command and its arguments are -lh followed by ~/My Documents. 

Alternatively, you can use a backslash to escape the space:

```
ls -lh ~/My\ Documents
```
In the Unix family of OSes, backslash (\) is called the escape character. When the shell parses that string of characters, it treats an escaped space (\ followed by a space) as a piece of the part. Again, ls is the command and its arguments are -lh and ~/My Documents.

Using Single Quotes Around Double Quotes

You can use the escape character to escape more than spaces. Let’s say you have a filename that has a space and quotes in it, like Say "Hello".txt, and you want to use the rm command, which deletes a file, to delete it. Unfortunately, running this command as 

```
rm Say "Hello".txt 
```

won’t work. Your shell will split this into the words rm, Say, and "Hello".txt (and technically, because of how quotes work in shells, the shell will interpret that third argument as Hello.txt). You might try to solve this by simply adding more quotes:

```
rm "Say "Hello".txt"
```

However, this won’t work either, since you’re trying to quote something that has quotes in it already. 
To solve this problem, you can surround the argument with single quotes ('), otherwise known as apostrophes, like this:

```
rm 'Say "Hello".txt'
```

This time, when your shell sees an escaped quote (\") it won’t treat it as a normal quote. It will read the command as rm and the argument as Say "Hello".txt, exactly what you intended. 

To keep things simple, I recommend avoiding putting spaces, quotes, or other troublesome characters in filenames when possible. Sometimes you can’t avoid them, though, especially when working with datasets full of someone else’s files.

Tab completion also helps in these cases. With tab completion, you only have to enter enough of the filename so that when you press TAB, your shell will fill out the rest for you. If you want to delete a file in your working directory called Say "Hello".txt, you can enter rm Sa<TAB>, and it will complete the command to rm Say\ \"Hello\".txt for you, so you don’t have to think about how to escape everything properly. (In this case, the tab completion fixes the problem by using backslackes to escape the space and quote characters instead of putting the whole filename in single quotes, which is another way to do it.)

Installing and Uninstalling Software with Package Managers
Of the many powerful command line tools that let you quickly work with datasets, only some come preinstalled; you’ll need to install the rest yourself. While you’re likely used to installing software by downloading an installer from a website and then running it, the command line uses package managers.

Package managers are programs that let you install, uninstall, and update software. Nearly all CLI software is free and open source, so Linux operating systems come with large collections of software that you can easily install or uninstall with a single command. Package managers are so useful that package management projects have also appeared for macOS (like Homebrew) and for Windows (like Chocolately).
If you’re using Linux, in this book we’ll use the package manager called apt. This is what the popular Linux OSes like Ubuntu and Debian use, as well as all of the versions of Linux based on these. If you’re using a version of Linux that doesn’t use apt though, you’ll need to look up the package manager documentation for your OS.
If you’re using a Mac, start with Homework 3-2 to learn how to use Homebrew. If you’re using Linux or Windows with WSL, skip to Homework 3-3 to learn how to use Ubuntu’s package manager, called apt. Since this book mostly uses Unix shells, it doesn’t cover Chocolately, which installs Windows software instead of Linux software.

### Homework 3-2: Manage Packages with Homebrew on macOS

To install Homebrew, macOS’s package manager, open a browser and go to Homebrew’s website at https://brew.sh. On the home page, you should find the command to install the tool. Copy and paste the installation command into your terminal, and press ENTER. 

```
micah@trapdoor ~ % /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
This is what the output looks like on my Mac:
==> Checking for `sudo` access (which may request your password)...
Password:
```

Enter your user password (the one you use to log into your Mac) and press ENTER to change your status from unprivileged user to root. No characters will appear in the terminal while you’re typing, but don’t worry, it’s working.

After you enter your password, Homebrew should show you a list of paths for files that it will install. The output should end with Press RETURN to continue or any other key to abort:. Press ENTER and wait for Homebrew to finish installing. As is common for CLI programs, Homebrew will show you exactly what it’s doing in the terminal, and if any problems arise, it will fail and show you an error message.

The command to install Homebrew works like this: first, it uses a program called cURL, which I discuss later in this chapter, to download a shell script from https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh. It then runs that script using the bash shell. The script itself uses sudo, meaning that if you enter your password, it will run commands as root on your computer. 
WARNING	Copying and pasting commands into your terminal like this can be dangerous: if a hacker tricks you into running the wrong shell script, they could hack your computer. Only copy and paste into your terminal commands from sources you trust.

Now that you installed Homebrew, you have access to a new command, brew, which you can use to install more software. To check whether Homebrew has a certain program available to install, run:

```
brew search program_name
```

For example, neofetch is a CLI program that displays information about your computer (and makes you look cool while doing it). To see if it’s available in Homebrew, run:

```
brew search neofetch
```

The ouptut should show you a list of packages that have neofetch in their names or descriptions—in this case, neofetch should be one of the packages. Similarly combine brew search with other program names to check whether they’re available to install. 

When you find a package you want to install, you can install it by running:

```
brew install program_name
```

For example, to install neofetch, run:

```
brew install neofetch
```

This should download and install this package, giving you the new command neofetch. Try running it:

```
neofetch
```

Figure 3-5 shows a screenshot of neofetch running on my Mac. The figure is black-and-white in print, but if you run the command on your computer, you should see a rainbow of colors.

[f04005.png]

<<Screenshow of a terminal running neofetch in macOS. It shows a rainbow-colored Apple logo made out of text characters.>>

### Figure 1-5 Running neofetch on my Mac

To uninstall programs you installed with Homebrew, pair brew uninstall with the program name:

```
brew uninstall program_name
```

For example:

```
brew uninstall neofetch
```

To update all the programs you’ve installed with Homebrew to their latest versions, run:

```
brew update
```

You can also run brew help to see some examples of how to use this command.

Now that you have a package manager installed, let’s practice using the popular CLI tool called cURL—you can install it with brew if you don’t already have it—that lets you download web pages directly from your terminal. Skip to the “Play with cURL” section on page XX.
Homework 3-3: Manage Packages with Apt on Windows or Linux
Ubuntu and similar Linux OSes (including Ubuntu in WSL, if you’re a Windows user) use a package manager called apt. You must run most apt commands as root. Before installing or updating software, make sure your OS has an up-to-date list of available software by opening a terminal and running:

```
sudo apt update
```

When I run that command on my Linux computer, I get the following output:

```
Hit:1 http://us.archive.ubuntu.com/ubuntu jammy InRelease
Hit:2 http://security.ubuntu.com/ubuntu jammy-security InRelease
Hit:3 http://us.archive.ubuntu.com/ubuntu jammy-updates InRelease
Hit:4 http://us.archive.ubuntu.com/ubuntu jammy-backports InRelease
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
178 packages can be upgraded. Run 'apt list --upgradable' to see them.
```

This tells me I have 178 packages that can be upgraded. I upgrade all of this software by running:

```
sudo apt upgrade
```

This is very similar to the previous command, but upgrade is used to actually install new versions of software, while update is used to just check and see if there are updates available. Here’s the output I get when I run that command:

```
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
Calculating upgrade... Done
The following packages will be upgraded:
--snip--
178 upgraded, 0 newly installed, 0 to remove and 0 not upgraded.
64 standard security updates
Need to get 365 MB of archives.
After this operation, 2,455 kB of additional disk space will be used.
Do you want to continue? [Y/n] 
```

I type Y and press ENTER to install the updates. Starting with sudo apt update, do the same for your own machine. 

Now you’re ready to install new software. To check whether the package manager has a certain program available to install, run:

```
apt search program_name
```

You don’t need to use sudo with this search command because it’s not installing or uninstalling anything. However, once you find a package you want to install, you’ll run:

```
sudo apt install program_name
```

For example, neofetch is a CLI program that displays information about your computer (and makes you look cool while doing it). To see if neofetch is available in your package manager, run:

```
apt search neofetch
```

The output should show you a list of packages that have neofetch in their names or descriptions—in this case, neofetch should be one of the packages.

Next, install neofetch:

```
sudo apt install neofetch
```
As when you updated your software, apt should show you a list of packages that you must install in order to use neofetch. Type Y and press ENTER to download and install them all. Once installation is complete, try running neofetch:

```
neofetch
```

Figure 3-6 shows a screenshot of neofetch running on my Ubuntu computer. The figure is black-and-white in print, but if you run the command on your computer, you’ll see several different colors.

[f04006.png]

<<Screenshow of a terminal running neofetch in Ubuntu. It shows an Ubuntu logo made out of text characters.>>
Figure 1-6 Running neofetch on my Ubuntu computer

To uninstall a package, run:

```
sudo apt remove program_name
```

For example, to uninstall neofetch, run this:

```
sudo apt remove neofetch
```

Now that you have a package manager installed, let’s practice using the popular CLI tool called cURL that lets you download web pages directly from your terminal.

### Package Management for Non-Ubuntu Linux Users

This book includes commands for installing Ubuntu packages using apt, but you should be able to follow along with this book no matter what version of Linux you’re using. Several other Linux distributions also rely on apt, like Debian, Linux Mint, Pop! OS, or others. If you’re using one of these, chances are the apt commands will just work. But if not, it’s possible that the names of software packages could be slightly different. If you hit that issue, run apt search software_name to find the name of the package that you should be installing for your OS.

If you’re using a version of Linux that doesn’t use apt as it’s package manager, you’ll need to slightly modify the commands listed in this book to use your Linux distribution’s package manager instead. For example, if you’re running Fedora, Red Hat, CentOS, or other similar Linux distributions, you’ll use a package manager called DNF (or, if you’re using an older version of one of these distributions, it’s called yum). You can learn how to use DNF by reading Fedora’s documentation at https://docs.fedoraproject.org/en-US/quick-docs/dnf/. If you use Arch Linux, you’ll use a package manager called pacman. You can learn how to use pacman from Arch’s wiki at https://wiki.archlinux.org/title/Pacman.

These are the package managers that popular Linux distributions use, but there are plenty of others too. If you’re using a different version of Linux not mentioned here, then make sure to read your OS’s package management documentation so you can get comfortable searching for, installing, uninstalling, and updating software or your computer from the terminal. When you come across an apt command in this book, use your OS’s package manager software instead.

Package management commands should be the only commands you need to worry about. Other Linux commands listed in this book should be the same.

### Homework 3-4: Practice Using the CLI with cURL

The cURL program is a common way to load web pages from the command line. To load all of the HTML code for the website 
https://www.torproject.org, you can run curl https://www.torproject.org. In this homework, you’ll learn how to find out whether you have a command installed or not using the which command, how to download web pages using the curl command, how to save the output from a command (specifically, the web page downloaded with curl) into a file using redirection, and how to view the contents of files directly from the terminal using the cat command. 

### The which Command

The which command tells you whether a given CLI programs is installed or not. Run the following command:

```
which curl
```

This should either show you a path to where the curl program is installed on your computer (probably something like /usr/bin/curl), or bring you straight back to the shell prompt, which means curl isn’t installed.
If necessary, install cURL using your package manager using sudo apt install curl for Windows with WSL and Linux machines and brew install curl for Macs. Now try running which curl again; this time, it should tell you the path of the cURL program.
Downloading a Web Page with cURL
In your terminal, run:
curl example.com
When you load a web page in your web browser, your browser knows what content should be displayed and how it should look based on the HTML code that makes up the web page, along well other types of code like CSS and JavaScript. The output of that curl command should show you all of the raw HTML from the web page hosted at https://example.com, without rendering it for you in a browser. If you load that site in a browser and then view the HTML source (in most browsers you can do this by pressing CTRL-U in Windows or Linux, or Apple-U in macOS), you should see the same HTML code that was displayed in your terminal.
Some websites are designed to work well with cURL by showing you text that’s easy to read in a terminal, as opposed to showing you HTML. For example, https://ifconfig.co will tell you your IP address, geolocate it for you, and tell you what country and city it thinks you’re in. Try running the following command:
curl https://ifconfig.co
This should display your IP address. Next, run the following:
curl https://ifconfig.co/country
When I run this command, my output is United States. You can try connecting to a VPN server in another country and then run it again—it should detect your web traffic as coming from that other country. Pretty cool, right?
Save a Web Page to a File
Let’s take cURL a step further. This time, run the following to load https://example.com and save it to a file:
cd /tmp
curl example.com > example.html
The first line, cd /tmp, changes your working directory to /tmp, which is a temporary folder—files you store automatically get deleted. The second line loads https://example.com, but instead of displaying the site’s contents for you in the terminal, it redirects those contents into the file example.html, and doesn’t display anything in the terminal. The > character takes the output of the command to its left and saves it into the filename to its right. This is called redirection. Since you changed to the /tmp folder before running the curl command, and the filename you provided was a relative path, it saved to the file /tmp/example.html.
Run a directory listing to make sure you’ve stored the file correctly:
ls -lh
This should list all the files in /tmp, which should include a file called example.html. You can display the contents of that file in your terminal using the cat command:
cat /tmp/example.html
It’s not always easy to read the contents of a file in the terminal. When you view files in your terminal, long lines will word-wrap, sometimes making them difficult to make sense of, and your terminal isn’t the best interface for reading or searching large files. For a better way to view text files, particularly source code such as HTML, shell scripts, or any other code instructions written by humans that computers are intended to follow, you’ll need to install a text editor.
Homework 3-5: Install a Text Editor
There are many different types of files, but they all fit into one of two categories: text files and binary files. Text files are simpler to work with. As the name implies, they’re made up of letters, numbers, punctuation, and a few special characters. Source code, like Python scripts (discussed in Chapters 7 and 8), shell scripts, and HTML, CSS, and JavaScript files, are all examples of text files. Spreadsheets in CSV format and JSON files (discussed in Chapters 9 and 11) are also text files. You can use the cat command to display text files, as you did in the previous homework assignment.
Binary files are made up of data that’s more than just letters, numbers, and punctuation, and are designed for computers programs to understand, not humans. If you try to view the contents of a binary file using the cat command, you’ll just see gibberish. Instead you must use specialized programs that understand those binary formats. Office documents like PDFs, Word documents, or spreadsheets in Excel format, are binary files, as are images (like PNG and JPEG files), videos (like MP4 and MOV files), and compressed data like zip files.
Text files aren’t always easy to understand (if you’re not familiar with HTML, viewing HTML might look a bit gibberish too), but it’s at least possible to display them in a terminal, which isn’t true for binary files. For example, if you try using cat to display the contents of binary files like PNG images in your terminal, the output will look something like this:

```
?PNG

IHDR?L??
?D?ؐ???? Pd@?????Y????????u???+?2???ע???@?!N???? ^?K??Eׂ?(??U?N????E??ł??.?ʛ?u_??|?????g?s?ܙ{?@;??sQ
 ?x?)b?hK`?/??L???t?+???eC????+?@????L??????/@c@웗7?qĶ?F
                                                        ?L????N??4Ӈ4???!?????
--snip--
```

Your terminal can’t actually display all of the characters that make up PNG images, so those characters just don’t get displayed. If you actually want to see the information stored in a PNG, you can’t just view the contents with cat. Instead, you need to open it in software that’s designed to view images.

**NOTE**
The term binary file is a technically a misnomer, because all files are represented by computers as binary—strings of ones and zeros. 

When working with datasets, and when writing shell scripts and Python code, you need a text editor, a program designed to edit text files. I like a free and open source text editor called Visual Studio Code (VS Code), which I’ll use in homework assignments in the rest of this book. If you’re already familiar with another text editor, feel free to keep using that one instead.

Download and install VS Code from https://code.visualstudio.com. After it’s installed, open it for the first time. VS Code comes with a CLI command called code that makes it easy to open files in VS Code directly from your terminal. Try using it to open the example.html file from the previous homework:

```
curl example.com > /tmp/example.html
code /tmp/example.html
```

The first line of code saves the HTML from example.com in the file /tmp/example.html (just like you did in Homework 3-4), and the second line opens this file in VS Code.

When you open new files and folders in VS Code, it will ask whether you trust each file’s author, giving you the option to open the file in Restricted Mode. For the homework assignments in this book, you can open files without using Restricted Mode. To learn more about when to use this mode, you can check out the VS Code documentation.
When you open example.html in VS Code, the file should look something like this:

```
<!doctype html>
<html>
<head>
    <title>Example Domain</title>

    <meta charset="utf-8" />
    <meta http-equiv="Content-type" content="text/html; charset=utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <style type="text/css">
    body {
        background-color: #f0f0f2;
        margin: 0;
        padding: 0;
        font-family: -apple-system, system-ui, BlinkMacSystemFont, "Segoe UI", "Open Sans", "Helvetica Neue", Helvetica, Arial, sans-serif;

    }
--snip--
```

You should see the same HTML code that you saw in your terminal in Homework 3-4, but this time it should it should be much easier to read.

On your computer, different parts of the file should appear in different colors. This coloring is called syntax highlighting, a very useful feature of VS Code and many other text editors. Looking at code with syntax highlighting makes it far quicker and easier for your brain to interpret source code, and also for you to catch mistakes in syntax.

VS Code is highly customizable and includes a wide variety of extensions that add extra functionality and make the program more pleasant to use. When you open new types of files, for instance, VS Code might ask if you’d like to install extensions for better support for those files.

Using your text editor, it’s time to write your first shell script.

### Homework 3-6: Write Your First Shell Script

Now that you have some experience running commands in a shell and have set up a text editor, you’re ready to write your first shell script: a text file that contains a list of shell commands. You can run shell scripts the same way you run other commands—in fact, many CLI commands are actually just shell scripts, such as the man command which you used earlier in this chapter, which displays the manual for other commands.

When you run a shell script, your shell runs each command inside of it, one at a time. Essentially, a shell script is a way for you to create your own new commands built out of other commands. You can even make them accept command line arguments. In fact, because shell scripts are just lists of commands, you can open a shell script in a text editor, select everything, copy it to the clipboard, paste it into the terminal, and press ENTER, and that will be the same as running the script. 

Before we get started, you’ll need a folder to save your work. To keep things organized, you should create a homework folder in your datasets USB disk and store your shell script there. I’ll show you how to do this all from the terminal.

### Navigate to Your USB Disk

Make sure your datasets USB disk is plugged in and mounted, and open up a terminal. In order to change your working directory to the datasets disk, you’ll need to figure out the path to it on your OS. 
Windows

After mounting your USB disk, open File Explorer to find its drive letter. You can do this by clicking on This PC on the left. This page will show you all of your connected drives and their drive letters. Then change your working directory to the disk by running the following command, substituting d for the correct drive letter:

```
cd /mnt/d/
```

Your shell’s working directly should now be your datasets USB disk. You can run ls to make sure you see the files you expect to see on this disk.

### macOS
After mounting your datasets USB disk, open a terminal and change your working directory to the disk by running the following command:

```
cd /Volumes/datasets
```

Your shell’s working directly should now be your datasets USB disk. You can run ls to make sure you see the files you expect to see on this disk. (If you named your USB disk something other than datasets, you may need to modify the command to use the correct path to your USB disk.)

### Linux

After mounting your datasets USB disk, open a terminal and change your working directory to the disk. In Linux, the path to your disk is probably something like /media/<username>/datasets. For example, my username is micah so I would run this command:

```
cd /media/micah/datasets
```

Your shell’s working directly should now be your datasets USB disk. You can run ls to make sure you see the files you expect to see on this disk.

### Create a Homework Folder
The mkdir command creates a new folder. Now that you’re in your USB disk in your terminal, run mkdir homework create a new folder called homework, and then switch to it:

```
mkdir homework
cd homework
```

Now make a folder for your Chapter 3 homework:

```
mkdir chapter-3
```

Now that you have a homework folder, and a chapter-3 folder inside it, let’s open the homework folder in VS Code.

### Open a VS Code Workspace
Each VS Code window is called a workspace, and you can add folders to it, which allow you to easily open any files in that folder, or create new ones. To open a VS Code workspace for your homework folder, run the following command:

```
code .
```

If the argument that you pass into code is a folder, like . (remember, . Is a relative path that represents the current working directory), then VS Code will add that folder your workspace. If the path is a file, like in the previous homework when you opened /tmp/example.html, it will just open that file.

Next, create a new file in the chapter-3 folder. To do this, right-click on the chapter-3 folder, choose New file, name your file homework-3-6.sh (shell scripts typically use the file extension .sh), and press ENTER. This should create a new file which you can edit. Since the file extension is .sh, VS Code should correctly guess that this is a shell script and use the right type of syntax highlighting. Figure 3-7 shows a screenshot of a VS Code workspace with the homework folder added, and with the empty file homework-3-6.sh created.

<<The Explorer panel on the left shows the homework folder, and the editor on the right shows the content of homework-3-6.sh, which is an empty text file.>>

Figure 1-7 Screenshot of VS Code, with the homework folder open in a workspace

As you can see, the VS Code window is split into two main parts. The panel on the left called Explorer shows the contents of all of the folders added to your workspace. In this case, it shows homework and everything that it contains, which is a chapter-3 folder and the homework-3-6.sh file you just created. The right side of the window is the editor, where you will type out the shell script.

### Write the Shell Script
Enter the following text into homework-3-6.sh in VS Code, and save the file:

```
#!/bin/bash
echo "Hello world! This is my first shell script."
# Display the current user
echo "The current user is:"
whoami
# Display the current working directory
echo "The current working directory is:"
pwd
```

In shell scripts, lines the start with the hash character (#) are called comments. Comments don’t affect how your code works—running the exact same script without comments will run the same way—but you can use them as notes to remind yourself of what you’re doing. Believe me, you’ll be happy that you commented your code when you come back to a script you wrote months or years later, trying to understand what you were thinking when you first wrote it. Anyone else who ends up working with your code, perhaps trying to fix something or add features, will appreciate comments for the same reason.

In homework-3-6.sh, the very first line that starts with #! is called the shebang, which tells the shell which interpreter to use when running this script. The interpreter is the program that opens the script and tries running it. In this case, the shell will use /bin/bash, which means it’s a bash script.

The first character of the shebang in homework-3-6.sh is a hash character, which means that it’s technically a comment in bash and zsh. That means your shell will ignore this line once it starts running your script.

Even if you’re using a different shell besides bash, like zsh, for example, this shebang tells your computer to run this script using bash. Syntax in zsh versus bash is slightly different, which is why you must specify the interpreter. For the purposes of this book, you’ll stick to writing bash scripts, so you’ll add that same shebang to the top of all of your shell scripts. (macOS and nearly all versions of Linux, including the Ubuntu installed in WSL in Windows, come with bash.)

The echo command displays text to the terminal. The whoami command displays the name of the user running the script. The pwd command displays the current working directory.

### Run the Shell Script

Before you can run a script, you need to make it executable by using the chmod command. The chmod command lets you change permissions on files, and you use it like this: chmod permissions filename. To mark a file as executable, which means that it’s a program that can be run, use +x as the permissions argument. Run this in your terminal (from within your homework folder) to make your script executable:

```
chmod +x ./chapter-3/homework-3-6.sh
```

You can now run the script, either by entering its absolute path, or by entering its relative path starting with ./, which lets your shell know that you’re typing out the relative path to a script. Run the script with its relative path:

```
./chapter-3/homework-3-6.sh
```

Here’s the output I get when I run this script on my Mac:
Hello world! This is my first shell script.
The current user is:

```
micah
The current working directory is:
/Volumes/datasets/homework
```

The current user is micah and the current working directory is /Volumes/datasets/homework. This script shows you different output depending on your working directly. To demonstrate the differences, here’s what happens when I switch to my home folder and then run it again:

```
micah@trapdoor homework % cd ~
micah@trapdoor ~ % /Volumes/datasets/homework/chapter-3/homework-3-6.sh 
Hello world! This is my first shell script.
The current user is:
micah
The current working directory is:
/Users/micah
```

The output is the same, except this time the current working directory has changed to /Users/micah. Try switching to your own home folder with cd ~ and running the script again.
The script also shows different output depending on what user is running it. So far I’ve been running it as my micah user, but here’s what the output looks like when I run it as root:

```
micah@trapdoor ~ % sudo /Volumes/datasets/homework/chapter-3/homework-3-6.sh
Password:
Hello world! This is my first shell script.
The current user is:
root
The current working directory is:
/Users/micah
```

This time, the output lists the current user as root. Try running the script as root on your own computer.

This is your first script, but there will be many more throughout this book. In order to aid you in learning, I’ve put a copy of the code for every homework assignment online. In the next assignment, you’ll download a copy of all of this code so you can have it locally on your computer.

### Homework 3-7: Clone the Book’s Git Repository

Programmers store source code in git repositories. A git repository, or git repo for short, is a collection of files (usually source code), and the history of how those files have changed over time. By storing your code in git repos, you can host it on GitHub, a popular website for hosting git repos, or similar websites. Git repos also help you share your code with others, and they make it easier for multiple people to write code for the same project. When you clone a git repo, you download a copy of it to your computer.

This book comes with a git repo containing the code for every homework assignment in this book. It also contains the code used in the Chapter 13 case study about America’s Frontline Doctors, and links to additional code and resources for the Chapter 14 case study about neo-Nazi chat logs. Finally, it includes additional instructions and source code for you to reference related to the book’s appendices. You can find the git repo at https://github.com/micahflee/hacks-leaks-and-revelations.

First, check whether git is installed on your machine by running:

```
which git
```

If git is installed, you’ll see its path in the output, like /usr/bin/git. If it’s not installed, this command won’t display anything in the terminal. In that case, install git by entering the appropriate command for your OS: brew install git for macOS users or sudo apt install git for Linux and WSL users.

Next, in your terminal, change to your USB disk folder. On my macOS computer, I do this as follows:

```
cd /Volumes/datasets
```

Check the previous homework assignment if you need a reminder on how to find the path to your datasets USB disk for your OS. Once there, run this command to clone the repo:

```
git clone https://github.com/micahflee/hacks-leaks-and-revelations.git
```

This should create a new folder called hacks-leaks-and-revelations containing all of the code from the book’s repo.

Finally, add the book’s git repo folder to your VS Code workspace. In VS Code, click File4Add Folder to Workspace, then browse for the hacks-leaks-and-revelations folder on your USB disk. This will add the book’s code to your VS Code workspace so you can easily browse through all of the files.

You now have access to solutions for all future homework! I walk you through the programming process in all of future programming assignments in this book, and I think that you’ll learn the most if you follow along a step at a time. However, you can also run the complete scripts taken directly from the git repo, or copy and paste code they contain into your own programs.
