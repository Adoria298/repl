"""
Package for generating REPLs for DSLs.
"""

__version__ = "0.0.1"

def repl(parser, style="chevron"):
    """
    Displays a REPL in stdin/stdout/stderr.

    Parameters:
        parser: function - a parser, e.g. eval(), that takes a line of code, and returns printable output
        style: string - the prompt style. Defaults to "chevron".
            options:
                "chevron" - a single chevron "> " for input, no output indicator
                "in/out"  - displays "In[<line number>]: " for input, the 'In' is replaced with 'Out' for output.
    Returns:
    
    None

    """
    # config
    prompt = {
        "chevron": {
            "line_nums": False,
            "in": "> ",
            "out": ""
        },
        "in/out": {
            "line_nums": True,
            "in": "In[{0}]:",
            "out": "Out[{0}]:" # when possible
        }
    }
    profig = prompt[style] # prompt config - to save typing
    if profig["line_nums"]:
        line_num = 0
        line_nums = True
    else: 
        line_nums = False

    # actual config
    while True:
        if line_nums:
            in_str = profig["in"].format(line_num)
            line_num += 1
            out_str = profig["out"].format(line_num)
            line_num += 1
        else:
            in_str = profig["in"]
            out_str = profig["out"]
        output = parser(input(in_str))
        print(out_str, output)

# manual tests
if __name__ == "__main__":
    #repl(eval) # allows developer to check their changes in default repl
    def test_parser(line):
        if line == "greet":
            return "hi"
        else:
            return "incorrect"
    repl(test_parser, "in/out")