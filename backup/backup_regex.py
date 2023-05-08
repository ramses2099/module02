import re


def main():
    text_to_search = """
    abcdefghijklmnopqrstuvwxyz
    ABCDEFGHIJKLMNOPQRSUVWXYZ
    0123456789
    
    Ha HaHa
    
    
    MetaCharacters (Need to be escaped):
    . ^ $ * + ? { } [ ] \ | ( )
    
    coreyms.com
    
    
    321-433-5439
    123.555.1234
    809.555.1234
    900.555.1234
    800.555.1234
    
    Mr. Schafer
    Mr Smith
    Ms Davis
    Mrs. Robinson
    Mr. T
    
    """

    sentence = "Start a sentence and then bring it to an end"

    pattern = re.compile(r"(Mr|Ms|Mrs)\.?\s[A-Z]\w*")
    matches = pattern.finditer(text_to_search)

    for match in matches:
        print(match)


if __name__ == "__main__":
    main()
# main
