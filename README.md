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
git clone "git.github.com/Adoria298/repl"
````

## To Do

1. Allow REPL customisation.
    - Output prompt
    - Change default output
    - Colour coding?

## FAQs

### Why are builds provided, but not on PyPI?

I have provided builds in order to easily allow installation for those who want it. These builds are not on PyPi I because I feel that PyPI is for additions to standard library that are not already in it. As similar tools to this exist in the standard library itself ([cmd](https://docs.python.org/3/library/cmd.html) and [code](https://docs.python.org/3/library/code.html) being two examples), I have declined to publish this library to PyPI.

### Why is there a FAQ section, when the questions in it haven't been asked yet?

They will be asked by someone at some point. When they are asked, they will not have to wait for an answer.