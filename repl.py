# source code for repl

def repl(parser):
    parser(input("> "))
    repl(parser)

# tests
if __name__ == "__main__":
    repl(eval) # allows developer to check their changes in default repl