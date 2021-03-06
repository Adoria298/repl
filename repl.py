"""
Package for generating REPLs for DSLs.

Licence:

MIT License

Copyright (c) 2018 Adoria298

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

"""

__version__ = "0.0.2"

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
        """
        Test parser. Should have everything a parser needs, to function with repl().
        """
        if line == "greet":
            return "hi"
        else:
            return "incorrect"
    repl(test_parser, "in/out")