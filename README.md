# `repl`

`repl` is a Read-Eval-Print-Loop generator written in Python. 

It is intended to be used with a DSL, as a console app. You should only ever need one function to make a REPL, with `repl`.

## Usage

As a python REPL: 

````python
>>> from repl import repl
>>> repl(eval)
> print("REPL within a repl!")
REPL within a repl!
> 
````
## Installation

````sh
$ python3 -m pip install rep
````

Or build from source:

````sh
$ git clone "git.github.com/Adoria298/repl"
$ python3 -m pip install -r requirements.txt
$ python3 setup.py
````

## To Do:

- Make basic functionality.
- Correct README.md
- Upload to Github
- Upload to PyPi
- Allow REPL customisation.