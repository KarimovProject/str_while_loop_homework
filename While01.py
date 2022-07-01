def main(s):
    """
    A variable of type str is given. Find how many numbers it contains and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    i = 0
    counter = 0
    while i <len(s):
        counter+=s[i].isdigit()
        i+=1
    return counter
print(main("f32fddh3"))