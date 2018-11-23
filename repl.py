# source code for repl

def repl(parser, style="chevron"):
    prompt = {
        "chevron": {
            "line_nums": False,
            "in": "> ",
            "out": ""
        },
        "in/out": {
            "line_nums": True,
            "in": "In[{0}]: ",
            "out": "Out[{0}]: "
        }
    }
    profig = prompt[style] # prompt config - to save typing
    if profig["line_nums"]:
        line_num = 0
        line_nums = True
    else: 
        line_nums = False

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
    #repl(eval) # allows developer to check their changes in default repl
    repl(eval, "in/out")