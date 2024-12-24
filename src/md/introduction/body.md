I wrote this book for journalists, researchers, hacktivists, and anyone
else who wants to learn the technologies and coding skills required to
investigate these troves of hacked or leaked data. I don't assume any
prior knowledge. Along with lessons on programming and technical tools,
I've incorporated many anecdotes and firsthand tips from the trenches of
investigative journalism. In a series of hands-on projects, you'll work
with real datasets, including those from police departments, fascist
groups, militias, a Russian ransomware gang,
and social networks. Throughout, you'll engage head-on with the dumpster
fire that is 21st-century current events: the rise of neofascism and the
rejection of objective reality, the extreme partisan divide, and an
internet overflowing with misinformation.

By the end of the book, you'll have gained the skills to download and
analyze your own datasets, extracting the revelations they contain and
transforming previously unintelligible information into your own
groundbreaking reports.


## Why I Wrote This Book

I've worked as an investigative journalist for The Intercept since 2013,
reporting on a large variety of leaked datasets. The first dataset I cut
my teeth on was the Snowden Archive: a collection of top-secret
documents from National Security Agency whistleblower Edward Snowden
revealing that the NSA spies on pretty much everyone in the world who
uses a phone or the internet. I wrote a dozen articles and helped
publish over 2,000 secret documents from that dataset, helping bring the
issues of privacy and government surveillance to the forefront of public
consciousness and leading to the widespread adoption of
privacy-protecting technologies.

Huge data leaks like these used to be rare, but today they're
increasingly common. In my work at The Intercept, I encounter datasets
so frequently I feel like I'm drowning in data, and I simply ignore most
of them because it's impossible for me to investigate them all.
Unfortunately, this often means that no one will report on them, and
their secrets will remain hidden forever. I hope this book helps to
change that.

Revelations based on leaked datasets can change the course of history.
In 1971, Daniel Ellsberg's leak of military documents known as the
Pentagon Papers led to the end of the Vietnam War. The same year, an
underground activist group called the Citizens' Commission to
Investigate the FBI broke into a Federal Bureau of Investigation field
office, stole secret documents, and leaked them to the media. This
dataset mentioned COINTELPRO. NBC reporter Carl Stern used Freedom of
Information Act requests to publicly reveal that COINTELPRO was a secret
FBI operation devoted to surveilling, infiltrating, and discrediting
left-wing political groups. This stolen FBI dataset also led to the
creation of the Church Committee, a Senate committee that investigated
these abuses and reined them in. More recently, Chelsea Manning's 2010
leaks of Iraq and Afghanistan documents helped spark the Arab Spring,
and documents and emails stolen by Russian military hackers helped elect
Donald Trump as US president in 2016.

As you make your way through this book, you'll download a variety of
real hacked and leaked datasets for yourself, learning how they're
structured and how to extract their secrets---and perhaps, someday,
you'll change history yourself. You'll read stories from many more
datasets as well, some of which are private and not available for the
public to download.



## What You’ll Learn

This book is split into five parts, with each building on the previous
part. You'll begin with security and privacy considerations, including
how to verify that datasets are authentic and how to safely communicate
with sources. You'll then work with datasets in your computer's terminal
and on remote servers in the cloud and learn how to make various kinds
of datasets searchable, including how to scour email dumps for
information. You'll get a crash course in Python programming, with a
focus on writing code to automate investigative tasks. These coding
skills will allow you to analyze datasets that contain millions of
files, which is impossible to do manually. Finally, I'll discuss two
exciting real-world case studies from some of my own investigations.

The following outline describes each chapter in greater detail.

**Part I: Sources and Datasets**

Part I discusses issues you should
resolve before you start analyzing datasets: how to protect your
sources, how to keep your datasets and your research secure, and how to
acquire datasets safely.

In Chapter 1, you'll learn about
how to protect your sources from retaliation. This includes how to
safely communicate with sources, how to store sensitive datasets, and
how to decide what information to redact. It also covers the critical
step of how to authenticate datasets, using the example of chat logs
from WikiLeaks and patient records from a far-right anti-vaccine group.
You'll learn how to secure your own digital life and, by extension, how
to secure the data-driven investigations you're working on. This
includes using a password manager, encrypting hard disks and USB disks,
sanitizing potentially malicious documents using the Dangerzone
application, and more.

In Chapter 2, you'll learn how to
acquire copies of hacked and leaked datasets. I'll introduce Distributed
Denial of Secrets (DDoSecrets), a transparency collective I'm involved
with that hosts copies of all of the datasets you'll work with in this
book, and you'll learn how to download datasets from DDoSecrets using
BitTorrent. I'll explain several ways to acquire datasets directly from
sources and introduce security and anonymity tools like Signal, Tor
Browser, OnionShare, and SecureDrop. As an example, I'll explain how I
communicated with a source who leaked data from the conservative
activist group Tea Party Patriots.

You'll also download a copy of the BlueLeaks dataset, one of the primary
datasets you'll work with in this book. BlueLeaks is a collection of
270GB of data hacked from hundreds of US law enforcement websites in the
summer of 2020, in the midst of the Black Lives Matter uprising. As
you'll see, it's full of evidence of police misconduct. BlueLeaks has
been widely covered in the press, but most of it hasn't been reported on
yet. By the end of this book, you'll have the tools you need to conduct
your own BlueLeaks investigations.

**Part II: Tools of the Trade**

In Part II, you'll practice using the
command line interface (CLI) to quickly assess leaked datasets and to
use tools that don't have graphical interfaces, developing skills you'll
apply extensively throughout the rest of the book.

In Chapter 3, you'll learn the
basics of controlling your computer through CLI commands, as well as
various tips and tricks for quickly measuring and searching datasets
like BlueLeaks from the command line. You'll also write your first shell
script, a file containing a series of CLI commands.

In Chapter 4, you'll expand your
basic command line skills, learning new commands and setting up a server
in the cloud to remotely analyze hacked and leaked datasets. As an
example, you'll work with the Oath Keepers dataset, which contains
emails from the far-right militia that participated in a seditious
conspiracy to keep Trump in power after he lost the 2020 election.

In Chapter 5 you'll learn to use
Docker, a technology that lets you run a variety of complex software
crucial for analyzing datasets. You'll then use Docker to run Aleph,
software that can analyze large datasets, find connections for you, and
search the data for keywords.

Chapter 6 focuses on tools and
techniques for investigating email dumps. You'll read emails from the
Nauru Police Force about Australia's offshore detention centers,
including many messages about refugees seeking Australian asylum, and
from the president of Nauru himself. You'll also investigate emails from
a conservative think tank called the Heritage Foundation, which include
homophobic arguments against gay marriage. Using the skills you learn,
you'll be able to research any email dumps you acquire in the future.

**Part III: Python Programming**

In Part III, you'll get a crash
course in writing code in the Python programming language, focusing on
the skills required to analyze the hacked and leaked datasets covered in
future chapters.

Chapter 7 introduces you to basic
programming concepts: you'll learn to write and execute Python scripts
and commands in the interactive Python interpreter, doing math, defining
variables, working with strings and Boolean logic, looping through lists
of items, and using functions.

Chapter 8 builds on the Python
fundamentals covered previously. You'll learn to traverse filesystems
and work with dictionaries and lists. Finally, you'll put theory into
practice by writing several Python scripts to help you investigate
BlueLeaks and explore leaked chat logs from the Russian ransomware gang
Conti.

**Part IV: Structured Data**

In Part IV, you'll learn to work with
some of the most common file formats in hacked and leaked datasets.

In Chapter 9, you'll learn the
structure of the CSV (comma-separated value) file format, viewing CSV
files in both graphical spreadsheet software and text editors. You'll
then write Python scripts to loop through the rows
of a CSV file and to save CSV files of your
own, allowing you to further investigate the CSV spreadsheets in the
BlueLeaks dataset.

Chapter 10 introduces a custom
application called BlueLeaks Explorer that I developed and released
along with this book, outlining how I built the app and showing you how
to use it. You can use this app to investigate the many parts of
BlueLeaks that haven't yet been analyzed, hunting for new revelations
about police intelligence agencies across the United States. If you ever
need to develop an app to investigate a specific dataset, you can also
use this chapter as inspiration.

Chapter 11 focuses on the JSON
file format and the Parler dataset of over a million videos uploaded to
the far-right social networking site Parler, including thousands of
videos of the January 6, 2021, insurrection at the US Capitol. This
dataset includes metadata for each video in JSON format, including
information like when the video was filmed and in what location. Some of
these videos were used as evidence during Donald Trump's second
impeachment inquiry. You'll write Python scripts to filter through these
videos and plot the GPS coordinates of Parler videos on a map, so you
can work with similar location data in future investigations.

In Chapter 12, you'll learn to
extract revelations from SQL databases by working with the Epik dataset.
Epik is a Christian nationalist company that provides domain name and
web hosting services to the far right, including sites known for hosting
the manifestos of mass shooters. The Epik dataset contains huge
databases full of hacked customer data, along with the true ownership
information for domain names for extremist websites---information that's
supposed to be hidden behind a domain name privacy service. You'll use
your new skills to discover domain names owned by one of the people
behind QAnon and the far-right image board 8kun. If you're interested in
extremism research, the Epik dataset might be useful for future
investigations.

**Part V: Case Studies**

Part V covers two in-depth case
studies from my own career, describing how I conducted major
investigations using the skills you've learned so far. In both, I
explain my investigative process: how I obtained my datasets, how I
analyzed them using techniques described in this book, what Python code
I wrote to aid this analysis, what revelations I discovered, and what
social impact my journalism had.

In Chapter 13, I discuss my
investigation into America's Frontline Doctors (AFLDS), a right-wing
anti-vaccine group founded during the COVID-19 pandemic to oppose public
health measures. I'll explain how I turned a collection of hacked CSV
and JSON files into a major news report, revealing that a network of
shady telehealth companies swindled tens of millions of dollars out of
vaccine skeptics. My report led to a congressional investigation of
AFLDS.

In Chapter 14 I describe how I
analyzed and reported on massive datasets of leaked neo-Nazi chat logs.
I also discuss my role in developing a public investigation tool for
such datasets, called DiscordLeaks. This tool aided in a successful
lawsuit against the organizers of the deadly Unite the Right rally in 2017, resulting in a settlement of
over $25 million in damages against the leaders of the American fascist
movement.

**Appendixes**

Appendix A includes tips for
Windows users completing the exercises in this book to help your code
run more smoothly. Appendix B
teaches you *web scraping*, or how to write code that accesses websites
for you so that you can automate your investigative work or build your
own datasets from public websites.



## What You’ll Need

This book is an interactive tutorial: every chapter other than the case
studies in Part V includes exercises. Many
later exercises require you to have completed earlier ones, so I
recommend reading this book sequentially. For example, in Chapter 1, you'll encrypt a USB disk to which you'll download a copy of the BlueLeaks dataset in Chapter 2.


Read this book with your computer open next to you, completing the
exercises and trying out technologies and software as you learn about
them. The source code for every exercise, as well as the code used in
case studies and appendixes, is available in an online repository
organized by chapter at
[https://github.com/micahflee/hacks-leaks-and-revelations](https://github.com/micahflee/hacks-leaks-and-revelations).

To make this book as accessible as possible, I've tried to keep the
requirements simple and affordable. You will need the following:

-   **A computer that's running Windows, macOS, or Linux.** Windows is
    very different from macOS and Linux, but I'll explain all the extra
    steps Windows users will need to take to set up their computers
    appropriately. If you're a Linux user, I assume that you're using
    Ubuntu; if you're using a different version of Linux, you may need
    to slightly modify the commands.
-   **A USB hard disk with at least 1TB of disk space.** You'll use this
    to store the large datasets you'll work with.
-   **An internet connection that can download roughly 280GB of datasets
    and several more gigabytes of software.** If you live in a country
    with decent internet service, your home internet should work fine,
    though it may take hours or days to download the largest datasets in
    the book. Alternatively, you might find more powerful internet
    connections at local libraries, coffee shops, or university
    campuses.
-   For the two exercises in which you'll work with datasets from
    servers in the cloud, you'll also need **a few US dollars (or the
    equivalent) and a credit card** to pay a cloud hosting provider.

Now grab your laptop, your USB hard disk, and perhaps a coffee or tea,
and get ready to start hunting for revelations.