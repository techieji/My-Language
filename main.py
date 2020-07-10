import re
import sys
import pprint

whitespace = re.compile(r"[ |\t]+")               # Example:     
newline    = re.compile(r"\n")     

identifier = re.compile(r"[a-z]+[A-Za-z0-9]*")       # Example: aId
dataname   = re.compile(r"[A-Z]+[A-Za-z0-9]*")       # Example: AData

integer    = re.compile(r"-?[0-9]+")                   # Example: 123
fraction   = re.compile(r"[0-9]+/[0-9]+")            # Example: 123/456
radical    = re.compile(r"-/\([0-9]+\)")             # Example: -/(3)
constant   = re.compile(r"(pi|tau|e)")               # Example: tau
decimal    = re.compile(r"[0-9]*.[0-9]+")            # Example: .73

plus       = re.compile(r"\+")
minus      = re.compile(r"-")
multiply   = re.compile(r"\*")
# Note the lack of a divide operator, it being present in the fraction datatype
match      = re.compile(r"=")
assign     = re.compile(r"<-")
cast       = re.compile(r":")
terminate  = re.compile(r"\.")

priorities = {
    'plus': plus,
    'minus': minus,
    'multiply': multiply,
    'match': match,
    'assign': assign,
    'cast': cast,
    'terminate': terminate,
    'integer': integer,
    'fraction': fraction,
    'radical': radical,
    'constant': constant,
    'decimal': decimal,
    'identifier': identifier,
    'dataname': dataname,
    'whitespace': whitespace,
    'newline': newline
}

def lex(inp: str) -> list:
    lexout = []
    lines = inp.split("\n")
    for line in lines:
        while line != "":
            for name in priorities:
                pattern = priorities[name]
                match = pattern.match(line)
                if match != None:
                    lexout.append((name, line[match.span()[0]:match.span()[1]]))
                    line = line[match.span()[1]:]
                    # print(f"line: {line}")
        lexout.append(("newline", "\n"))
    return lexout
    
def translate(lexout):
    transout = []
    for x in lexout:
        if x[0] == 'identifier':
            transout.append(x[1])

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        #inp = sys.argv[1]
        pprint.pprint(lex(f.read()))
