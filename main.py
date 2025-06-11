def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return(file_contents)

def main():
    text_output = get_book_text("./books/frankenste")
    print(text_output)





main()