def word_count(path_to_file):
    with open(path_to_file) as w:
        contents = w.read()
        number_count = len(contents.split())
    return(number_count)
    
