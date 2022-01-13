# CTE Interview

Hello and welcome to the interview process to Cloud Test Engineering team.
Please take your time to go through this exercies, failing to answer any (or all) questions doesn't
necesarilly disqualify you from proceeding through the interview process, it just prepares a working
ground for the spoken interview.

Good luck!

## Technical knowledge
Please answer in regards to your knowledge, don't use google.

* Roughly, how long did it take for you to get to this file?
	less than 10 seconds
* Why does this file have .md extension and what is the format?
	it is Markdown file extension applicated on plain text, probably for formatting and also it can be converted to html, also ported into github
* What will most probably happen in this shell scenario?
	Firstly we look on count (words, chars, etc.) in files starting with foo, then same for files starting with bar and then we remove all files with name starting with foo
  ```
  $ ls | grep ^foo | wc -l
       32000
  $ ls | grep ^bar | wc -l
       32000
  $ rm foo*
  ```
* You have two servers which are connected by physical network, but for some reason you're unable to
  reach service supposedly running on the second server from the first. What methods and utilities
  would you use for investigation of such issue and why?
	- Probably firstly check if network is running (ping on my interface, outside, ping on server, if server is answering then I would know that something is wrong with service but not necessary with the network or server itself, than I would probably
  use some secure method to get into that server remotely and continue from there, then test if the desired service is running or not and then restart it, check logs, etc. 
* What is the relationship between Makefile and .spec file
	- .spec file specifies all actions for Makefile for building, installing and removing our app 
* What is symmetric and asymmetric cryptography, what are the differences, and common usecases?
* What are relational and nosql databases, what are the differences, and common usecases?
	- Relational dbs are based on tables and relation between them, mostly used for structured data cases, nosql dbs can be for example document based, graph, key-value pair etc. Nosql is better for modern complex apps, also 
	for constantly changing datasets like in data science etc. 
* Explain the difference between rebase and merge in Git.
	- rebase merges feature branch with master, merge but in a way of new commit and so keeping a history
* What is virtual environment in python, how would you use it?
	- it is where all our dependencies and packages, interpreter etc. of one app should be to separated from other vems (apps and their dependencies, etc.)
	- it helps to keep our file system and apps clean and organized
* How do you prevent other users from touching your files on a shared linux machine?
	- probably changing persmissions of Read, write and execute over your home directory (or files itself), sudo chmod xxxx(code) / directory(file) path
* There are “users” and "phone_contacts" tables in a relational database (see below).
  Write a query to select all users' full name along with all phone contacts. 
  Every user can have no contacts or multiple contacts.
	SELECT users.first_name, users.surname, phone_contacts.phone_number
	FROM users
	LEFT JOIN phone_contacts ON users.id = phone_contacts.user_id
	
```
| id  | first_name | surname | ... |
|-----|------------|---------|-----|
| 1   | Peter      | Novak   |     |
| 2   | Jana       | Zelena  |     |
| 3   | Dan        | Vesely  |     |
| ... |            |         |     |

| id  | user_id | phone_number   |
|---- |---------|----------------|
| 1   | 1       | 00420777777777 |
| 2   | 1       | 00420888888888 |
| 3   | 2       | 00420999999999 |
| ... |         |                |
```
* What can you tell about the following string? `SGVsbG8gV29ybGQhCg==
	-seems like a hash

## Architecture and research
Feel free to do your online research for this part.

* Imagine you're tasked with maintenance of 5,000 servers with several different roles, this will
  include configuration changes, security patching, reboots, relatively simple tasks when performed
  on one machine. How would you approach this, what technology would you use, and why?
  I think that in this case it would be sufficient to use some type of orchestration and automatization like Puppet, Ansible, overall server managers.
  Firt thing for better backup and setup of new servers (or updates) and second for monitoring performence etc.

* How would you test utility which is supposed to change login shell for your user?

* In a situation where you have a service set up as master server with hot standby, and you have the
  identical setup prepared as your development instance, how would you proceed with migration to new
  version of the service? Describe each step, and reasons behind it.


* Try to think about the most methods you could use to transfer a file from one server to another,
  where both of them are physically accessible and are interconnected by network.
  Well we can obviously use any medium psychical medium (External storage, USB etc. tapes-> can be acutally the fastest way for massive size of data) 
  but way more efficient way is to use FTP (obviously, if we have secured conection), SCP, Maping servers
  for eachother as network disk, also it is possible to use third party SW but depends od security and trust, 

## Code exercise

* Take the [following function](https://raw.githubusercontent.com/samuelmarina/is-even/main/index.js),
  port it to python and simplify it to least possible amount of statements, without use of modulo
  operator, but ensure the functionality and logic stays the same.
* Write a small interactive python utlity that calculates matrix multiplication. None of the variables
  are passed as arguments, everything will be handled at runtime, please see the example run below.
  Write te utility in a way you'd write a production code which you'll have to maintain for the rest
  of your life, and as if you were dealing with real world client who can change their mind anytime.
  Use `python3` without any mathematical libraries (like numpy), and if you're familiar with `pytest`,
  try to use test driven development approach and attach all tests created during development.
  User inputs are shown here in square brackets for understanding, don't include those.

```
$ ./mx_mul.py
Matrix A
width: [2]
height: [3]
Matrix B
width: [1]
height: [2]
Matrix A values:
[1 2]
[5 3]
[6 7]
Matrix B values:
[5]
[1]
Result:
7
28
37
```
