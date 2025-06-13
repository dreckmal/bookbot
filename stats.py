def word_count(path_to_file):
    with open(path_to_file) as w:
        contents = w.read()
        number_count = len(contents.split())
    return(number_count)
    
frequency = {}
def alpha_count(path_to_file):
    with open(path_to_file) as w:
        contents = w.read()
        lower_case = contents.lower()
        for alpha in lower_case:
            if alpha in frequency:
                frequency[alpha] += 1
            else:
                frequency[alpha] = 1
    return(frequency)
