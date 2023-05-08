import re


def rearrange_name(name):
    """
    Re arrange name:
    """
    result = re.search(r"^([\w .]*), ([\w .]*)$", name)
    if result is None:
        return name
    return "{} {}".format(result[2], result[1])

def LetterCompiler(text):
    result = re.findall(r'([a-c]).',text)
    return result

# end def
