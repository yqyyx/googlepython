# Defines a "repeat" function that takes 2 arguments.
def repeat(s, exclaim):
    """
    Returns the string 's' repeated 3 times.
    If exclaim is true, add exclamation marks.
    """

    result = s + s + s # can also use "s * 3" which is faster (Why?) #一次分配空间 VS 多次分配空间
    if exclaim:
        result = result + '!!!'
    return result

def main():
    print repeat('Yay', False)      ## YayYayYay
    print repeat('Woo Hoo', True)   ## Woo HooWoo HooWoo Hoo!!!

# def main():
#     if name == 'Guido':
#         print repeeeet(name) + '!!!'
#     else:
#         print repeat(name)