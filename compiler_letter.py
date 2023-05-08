import re

def LetterCompiler(text):
    result = re.findall(r'([a-c]).',text)
    return result

# end def
