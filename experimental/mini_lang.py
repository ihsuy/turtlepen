import sys
sys.path.insert(0, "../turtlepen")

from turtlepen import blocks, tools, turtle


commands = {
    "F":blocks.Forward,
    "R":blocks.Rotate,
    "U":blocks.PenUp,
    "D":blocks.PenDown,
    "B":blocks.BackToCenter,
}

def get_indentation(s, nspace=4):
    return (len(s)-len(s.lstrip()))//nspace

def get_cmd(s):
    tokens = s.lstrip().split(' ')
    return tokens

# parse lines and output a compiled action object
def rp(lines,n=1):
    actions = []
    i = 0
    while i < len(lines):
        line = lines[i]
        i+=1
        
        indent = get_indentation(line)
        cmd, *args = get_cmd(line)

        # repeats indented lines
        if cmd == "P":
            sublines = []
            while i < len(lines) and get_indentation(lines[i])>indent:
                sublines.append(lines[i])
                i+=1
            # recursively call rp on indented lines
            actions.append(rp(sublines, n=int(args[0])))
        else:
            actions.append(commands[cmd](*map(int, args)))
        
    return blocks.Repeat(n, actions)


### ### ### ### ### ### ### ### 
# test
tt = turtle.Turtle()

with open('./experimental/script2.txt', 'r') as f:
    lines = f.read().split('\n')
    action = rp(lines, n=1)
    action.apply(tt)
    tools.visualize_trace(tt)