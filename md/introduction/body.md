I wrote this book to teach journalists, researchers, and anyone else who is curious about how to learn the technology and coding skills required to investigate these large troves of hacked or leaked data. However, I don’t assume any prior knowledge. Throughout the book, I explain everything you’ll need to know, along with anecdotes from the trenches of investigative journalism. And though much of it is technical, this book is not dry. All of the datasets that I use as teaching aids in this book are directly related to the dumpster fire that is 21st century current events: the rise of neofascism and the rejection of objective reality, the extreme partisan divide, and an internet overflowing with misinformation. You’ll get hands-on experience working with real datasets, including those from police departments, fascist groups, militias, a Russian ransomware gang, and social networks.

This book starts with important security and privacy considerations, including how to verify that datasets are authentic and how to safely communicate with sources, then moves on to more technical skills. You’ll learn to work with datasets in the your computer’s terminal and on remote servers in the cloud. You’ll learn how to make various kinds of datasets searchable, including how to scour email dumps for information. You’ll then move on to Python programming, with a focus on writing code to automate investigative tasks. These coding skills will allow you to analyze datasets that contain millions of files, which is impossible to do manually. Finally, I discuss two exciting real-world case studies from some of my own investigations. 

By the end of the book, you’ll have gained the skills to download and analyze your own datasets, extracting the revelations they contain and publishing your own groundbreaking reports.

### The Datasets You’ll Investigate

I’ve worked as an investigative journalist for The Intercept since 2013, reporting on a large variety of leaked datasets. The first dataset I cut my teeth on was the Snowden Archive: a collection of top secret documents from National Security Agency whistleblower Edward Snowden that revealed that the NSA spies on pretty much everyone in the world who uses a phone or the internet. I wrote a dozen articles and helped publish over 2,000 secret documents from that dataset, helping bring the issues of privacy and government surveillance to the forefront of public consciousness, and leading to the widespread adoption of privacy-protecting technologies. 

Revelations based on leaked datasets can change the course of history. In 1971, Daniel Ellsberg’s leak of military documents known as the Pentagon Papers led to the end of the Vietnam War. The same year, an underground activist group called the Citizens Committee to Investigate the FBI broke into a Federal Bureau of Investigation field office, stole secret documents, and leaked them to the media. This dataset mentioned COINTELPRO. NBC reporter Carl Stern used Freedom of Information Act requests to publicly reveal that this was a secret FBI operation devoted to surveilling, infiltrating, and discrediting left-wing political groups. This stolen FBI dataset also lead to the creation of the Church Committee, a Senate committee that investigated these abuses and reigned them in. More recently, Chelsea Manning’s 2010 leaks of Iraq and Afghanistan documents helped spark the Arab Spring, and documents and emails stolen by Russian military hackers helped elect Donald Trump as a US President in 2016. 

Huge data leaks like these used to be rare, but today they’re increasingly common. Today, in my work at The Intercept, I encounter datasets so frequently I feel like I’m drowning in data, and I simply ignore most of them because it’s impossible for me to investigate them all. Unfortunately, this often means that no one will report on those datasets, and their secrets will remain hidden forever. I hope this book helps to change that. 

As you make your way through this book, you’ll download a variety of real hacked and leaked datasets, learning how they’re structured and how to extract their secrets. You’ll spend the most time with BlueLeaks, a collection of 270GB of data hacked from hundreds of US law enforcement websites. The BlueLeaks data was hacked in the summer of 2020, in the midst of the Black Lives Matter uprising, and, as you’ll see, it’s full of evidence of police misconduct. BlueLeaks has been widely covered in the press—I’ve written several articles myself—but because most journalists don’t have the skills they need to analyze the data deeply, most of BlueLeaks hasn’t yet been reported on. 

You’ll also investigate a dataset full of over a million videos uploaded to the far-right social networking site Parler, including thousands of videos of the January 6, 2021 insurrection at the US Capitol. This dataset includes metadata for each video. The metadata contains information like what phone the video was filmed on and when, and for many of the videos, where. Since this dataset includes GPS coordinates, you’ll get hands-on experience plotting location data on a map. Some of these videos were used as evidence during Donald Trump’s second impeachment inquiry.

You’ll read emails from Nauru Police Force about Australia’s offshore detention centers, including many messages about refugees seeking Australian asylum, and from the President of Nauru himself. You’ll also sift through emails from the Oath Keepers, the far-right militia that participated in a seditious conspiracy to keep Trump in power after he lost the 2020 election. And you’ll read emails from a conservative think tank called Heritage Foundation, which includes homophobic arguments against gay marriage. These are just examples designed to teach you how to investigate different types of email dumps. Using the skills you learn, you’ll be able to research any email dumps you acquire in the future.

You’ll dig into databases from Epik, a Christian nationalist company that provides domain name and web hosting services to the far right, including sites known for hosting the manifestos of mass shooters. This dataset contains huge databases full of customer data, and it includes the true ownership information for domain names for extremist websites—information that’s supposed to be hidden behind a domain name privacy service. If you’re interested in extremism research, this dataset might be useful for future investigations.

You’ll read stories from many more datasets as well, including some which are private and not available for the public to download. These include chat logs from WikiLeaks, millions of messages posted to the far-right social network Gab, the internal database of the conservative activist group Tea Party Patriots, and others. 

### Requirements for Following Along

This book is an interactive tutorial: every chapter other than the case studies in the final section includes homework assignments. Many later assignments require you to have completed earlier ones, so I recommend you read this book sequentially. For example, in Chapter 2, you’ll encrypt a USB disk to which you’ll download a copy of the BlueLeaks dataset in Chapter 3. Several later chapters then include homework assignments in which you’ll use that copy of BlueLeaks. 

To get the most out of this book, read it with your computer open next to you, completing the homework assignments and trying out technologies and software as you learn about them. You don’t need anything except this book to complete all of the homework assignments. However, copies of the source code for every assignment are available in an online repository at https://github.com/micahflee/hacks-leaks-and-revelations, organized by chapter. If you prefer, you can copy and paste code from their repository into your own editor instead of typing it. The repository also includes code used in the book’s case studies and appendixes.

In order to make this book as accessible as possible, I’ve tried to keep the requirements simple and affordable. You will need:

* A computer that’s running Windows, macOS, or Linux. Windows is very different from macOS and Linux, but I’ll explain all the extra steps Windows users will need to take to set up their computers appropriately. If you’re a Linux user, I assume that you’re using Ubuntu; you may need to slightly modify the commands to match your version of Linux if you’re using a different version.
* A USB hard disk with at least 1 TB of disk space. You’ll use this to store the large datasets you’ll work with.
* An internet connection with the ability to download roughly 280 GB of datasets and several more gigabytes of software. If you live in a country with decent internet service, your home internet should work fine, though it may take hours or days to download the largest datasets in the book. Alternatively, you might find more powerful internet connections at local libraries, coffee shops, or university campuses. 
* For the two homework assignments in which you’ll work with datasets from servers in the cloud, you’ll also need a few US dollars’ worth of money and a credit card to pay a cloud hosting provider.

### What You’ll Learn

This book is split into five parts, with each part building on the previous part.

#### Part 1: Sources and Datasets

Part 1 discusses issues you should resolve before you start analyzing datasets: how to protect your sources, how to keep your datasets and your research secure, and how to acquire datasets safely. In Chapter 1, you’ll learn about how to protect your sources from retaliation. This includes how to safely communicate with sources, how to store sensitive datasets, and how to decide what information to redact. It also covers the critical step of how to authenticate datasets. You’ll learn how to secure your own digital life, and by extension, how to secure the data-driven investigations you’re working on. This includes using a password manager, encrypting hard disks, sanitizing potentially malicious documents using the Dangerzone application, and more.

In Chapter 2, you’ll learn how to acquire copies of hacked and leaked datasets. I’ll introduce Distributed Denial of Secrets (DDoSecrets), a transparency collective I’m involved with that hosts copies of all of the datasets you’ll work with in this book, and how to download datasets from DDoSecrets using BitTorrent. You’ll download a copy of BlueLeaks to an encrypted USB disk. I’ll explain several ways to acquire datasets directly from sources and introduce security and anonymity tools like Signal, Tor Browser, OnionShare, and SecureDrop.

#### Part 2: Tools of the Trade

At this point, the book starts to become more technical. In Part 2, you’ll get ample practice using the command line interface (CLI) to quickly assess leaked datasets and to use tools that don’t have graphical interfaces, developing skills you’ll use extensively throughout the rest of the book. 

In Chapters 3 and 4, you’ll learn the basics of controlling your computer through CLI commands, as well as various tips and tricks for quickly measuring and searching datasets like BlueLeaks from the CLI. You’ll set up a server in the cloud for remotely analyzing hacked and leaked datasets, using the Oath Keepers dataset, which contains emails from the far-right militia, as an example. 

In Chapter 5, you’ll learn to use Docker, technology that lets you run a variety of complex software crucial for analyzing datasets. You’ll then use Docker to run Aleph, software that can analyze large datasets, find connections for you, and search the data for keywords. Finally, Chapter 6 focuses on tools and techniques for investigating email dumps.

#### Part 3: Python Programming

Part 3 gets you started writing code in the Python programming language, focusing on the skills required to analyze hacked and leaked datasets. Chapter 7 introduces you to basic programming concepts: you’ll practice writing Python code that uses variables, loops, and functions. Chapter 8 builds on these fundamentals, focusing on the Python skills most useful for investigating datasets. You’ll learn to traverse filesystems and work with dictionaries and lists. Finally, you’ll put theory into practice by writing several Python scripts to help you investigate BlueLeaks and explore leaked chat logs from the Russian ransomware gang Conti.

#### Part 4: Structured Data

In Part 4, you’ll learn to work with some of the most common file formats in hacked and leaked datasets. In Chapter 9, you’ll learn all about spreadsheets, particularly the CSV file format, writing Python scripts to further investigate the BlueLeaks CSV files. Chapter 10 introduces a custom application that I developed and released along with this book, called BlueLeaks Explorer. You can use this app to investigate the many parts of BlueLeaks that haven’t yet been analyzed, hunting for new revelations about police intelligence agencies across the United States.

Chapter 11 focuses on the JSON file format. You’ll work with metadata from videos uploaded to the right-wing social media site Parler, writing Python scripts to filter through the list of a million videos, including thousands that were filmed during the January 6, 2021 insurrection. You’ll also learn about working with location data, and you’ll plot the locations of Parler videos on a map.

In Chapter 12, you’ll learn to extract revelations from SQL databases by working with the Epik dataset, which includes hacked data from an extremist hosting provider. You’ll use your new skills to discover domain names owned by one of the people behind QAnon and the far right image board 8kun.

#### Part 5: Case Studies

Part 5 covers two in-depth case studies from my own career, describing how I conducted major investigations using the skills you’ve learned so far. In both, I explain my investigative process: how I obtained my datasets, how I analyzed them using techniques described in this book, what Python code I wrote to aid this analysis, what revelations I discovered, and the social impact my journalism had.
In Chapter 13, I discuss my investigation into America’s Frontline Doctors (AFLDS), a right-wing anti-vaccine group founded during the COVID-19 pandemic to oppose public health measures. I’ll explain how I turned a collection of hacked CSV and JSON files into a major news report, revealing that a network of shady telehealth companies swindled tens of millions of dollars out of vaccine skeptics. My report led to a Congressional investigation of AFLDS.

In Chapter 14, I describe how I analyzed and reported on a massive dataset of leaked neo-Nazi chat logs. I also discuss my role in developing a public investigation tool for such datasets, called DiscordLeaks. This tool aided in a successful lawsuit against the organizers of the deadly Unite the Right rally in 2017, resulting in a settlement of over $25 million in damages against the leaders of the American fascist movement.

#### Appendixes

This book includes two appendixes. Appendix A includes tips for Windows users who are following along with this book. Appendix B teaches you web scraping, or how to write code that accesses websites for you, allowing you to automate investigative work or build your own datasets from public websites.

Grab your laptop, your USB hard disk, and perhaps a coffee or tea, and get ready to start hunting for revelations.