## Project
This is the *Learning Progress Tracker (Python)* project that is part of Hyperskill platform from Jetbrains Academy.

## Project description
CLI project for students keeping tags on their learning progress

How to play: (note `<` added for input )

```bash
< add students
Enter student credentials or 'back' to return: 
< John Doe jdoe@email.net
The student has been added.
< back
Total 1 students have been added.
< add points
Enter an id and points or 'back' to return: 
< 1000 600 400 350 200
Points updated.
< back
< statistics
Most popular: Python, DSA, Databases, Flask
Least popular: n/a
Highest activity: Python, DSA, Databases, Flask
Lowest activity: n/a
Easiest course: Python
Hardest course: Flask
< back
< notify
To: jdoe@email.net
Re: Your Learning Progress
Hello, John Doe! You have accomplished our Python course!
To: jdoe@email.net
Re: Your Learning Progress
Hello, John Doe! You have accomplished our DSA course!
Total 1 students have been notified.
< exit
Bye!
```

Features:
- add students
- list students
- add course points (Python, DSA, Databases, Flask)
- check overall course statistics
- check statistics per course
- notify users which completed course via 'stdout' text email :)

Have fun

#### Install steps

Install everything (main + dev packages except optional groups)

```sh
peotry install
```

Install main packages only

```sh
peotry install --only main

```

If you need pre-commit

```sh
poetry install --with commit
```

If you decided to install pre-commit you can install .pre-commit files in your repo

```sh
peotry run pre-commit install -t pre-commit
poetry run pre-commit install -t pre-push
```

If the files are git staged, you can trigger pre-commit manually

```sh
poetry run pre-commit run --all-files
poetry run pre-commit run --hook-stage push -v
```

#### Makefile

Added 'Makefile' to make it easy to validate files
Check bellow command on usage

```sh
make help
```
