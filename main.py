# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here 
    with open(filename, "r") as f:
        return f.read()


def count_words():
    text = read_file_content("./story.txt")
    # [assignment] Add your code here  
    
    #lower case the text  
    text = text.lower()
    
    #remove punctuations
    for character in text:
        if character in ".,!?'":
            text = text.replace(character, "")
    
    #split the text into words
    text_list = text.split()
    
    #define text dictionary
    text_dict = {}
    
    #count the occurence of words and store in dictionary
    for word in text_list:
        count = text_list.count(word)
        
        #dictionary takes care of duplicates
        text_dict[word] = count
    
    # return {"as": 10, "would": 20}
    return text_dict

print(count_words())