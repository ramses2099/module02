import re


def rearrange_name(name):
    """
    Re arrange name:
    """
    result = re.search(r"^([\w .]*), ([\w .]*)$", name)
    return "{} {}".format(result[2], result[1])


# end def
