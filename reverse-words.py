

def my_function(arg):
    # write the body of your function here

    new_list = arg.split()[::-1]
    
    # new_phrase.join(new_list)
    # another_list = new_list[::-1]

    # print another_list
    new_phrase = ' '.join(new_list)
    print new_phrase
my_function('test thing')