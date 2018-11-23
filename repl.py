"""
Package for generating REPLs for DSLs.
"""

__version__ = "v.0.1.0"

def repl(parser, style="chevron"):
    """
    Displays a REPL in stdin/stdout/stderr.

    Parameters:
        parser: function - a parser, e.g. eval(), that takes a line of code.
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
            "in": "In[{0}]: ",
            "out": "Out[{0}]: " # when possible
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
            prompt_str = profig["in"].format(line_num)
            line_num += 1
            parser(input(prompt_str))
            # TODO(adoria298): allow out prompts as well
            line_num += 1 
        else:
            prompt_str = profig["in"]
            parser(input(prompt_str))

# manual tests
if __name__ == "__main__":
    repl(eval) # allows developer to check their changes in default repl
    #repl(eval, "in/out")