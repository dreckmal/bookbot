def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return(file_contents)


def word_count(path_to_file):
    with open(path_to_file) as w:
        contents = w.read()
        number_count = len(contents.split())
    return(number_count)
    



def main():
#    text_output = get_book_text("./books/frankenstein.txt")
    how_many_words = word_count("./books/frankenstein.txt")    

    
#    print(text_output)
    print(f'{how_many_words} words found in document')



main()
