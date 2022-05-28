# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here
    with open("./story.txt", "r") as readfile:
        readfile = readfile.read()
    return readfile
read_file_content("./story.txt")


def count_words():
    # [assignment] Add your code here
    text = read_file_content("./story.txt")
    use_text = use_text.split()

    count = {}
    for a in  use_text:
        if a in count:
            count[a] += 1
        else:
            count[a] = 1
    return count
count_words()     
 
