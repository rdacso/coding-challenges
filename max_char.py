def max_char(string):
    """print the character that displays most often and only the first instance of that character. 

        >>> max_char('hello world')
        l

        >>> max_char('')
        

        >>> max_char('ho hello')
        h

        >>> max_char('1122333')
        3

        >>> max_char('123')
        1
    """

    counting_dict = {}
    for char in string:
        counting_dict[char] = counting_dict.get(char,0) + 1

    for key, value in counting_dict.iteritems():
        if value >= max(counting_dict.values()):  
            print key
            break




if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print "\n*** ALL TEST PASSED. AWESOMESAUCE!\n"