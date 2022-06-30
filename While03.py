import string
def main(s):
    """
    A variable of type str is given. Find how many punctuations it contains and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    i=0
    while i <len(s):
        n = s.translate(str.maketrans('', '', string.punctuation))
        x = len(n)
        i+=1
    return x
print(main("q$#efry!"))