# `repl`

`repl` is a Read-Eval-Print-Loop generator written in Python. 

It is intended to be used with a DSL, as a console app. You should only ever need one function to make a REPL, with `repl`.

## Usage

As a python REPL: 

````python
>>> from repl import repl
>>> repl(eval)
> print("REPL within a REPL!")
REPL within a repl!
> 
````
## Installation

Clone from Github:

````sh
$ git clone "git.github.com/Adoria298/repl"
````

## To Do:

- Upload to PyPi
- Allow REPL customisation.
    - Different prompt
    - Change default output
    - Colour coding?