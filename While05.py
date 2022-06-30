def main(s):
    """
    A variable of type str is given. Find how many lowercase letters there are and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    i = 0
    counter = 0
    while i <len(s):
        counter+=s[i].islower()
        i+=1
    return counter
print(main("fE2BddN3"))