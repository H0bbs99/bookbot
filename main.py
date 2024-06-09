    #Counts the number of words
def count_words(text):
    word = text.split()
              
    return (len(word))
    

# Counts to the letters of each script and returns to lower case
def count_characters(text):
    character ={}
    for letter in text.lower():
        if letter.isalpha():
            if letter in character:
               character[letter] += 1
            else:
                character[letter] = 1

              
    return character

# Converts dictionary to dictionary of dictionaies for character counts.
def convert_to_list(char_dict):
    char_list =  []
    for letter, count in char_dict.items():
        char_list.append({"character": letter, "num": count})
    
    return char_list

# Allows for sorting characters by number
def sort_on(dict):
    return dict["num"]

#Cleanly prints the results of the book
def clean_print(words, char):
    print(f"{words} words are found in the document\n\n")

    for i in char:
        print(f"The '{i["character"]}' was found {i["num"]} times")


               
         


 



    


def main():
    
    
    letters = {}
    words = 0
    file_contents =[]

    # Counts the total number of words in a text
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    
        words = count_words(file_contents)

        letters = count_characters(file_contents)

        letters = convert_to_list(letters)
        
        letters.sort(reverse=True, key=sort_on)

        clean_print(words, letters)


        

   
    
    
    # Counts the total number of each word and adds it to a dicctionary

    #for word in words:
     #   text = word.lower()
      #  text = text.split()
        
       # print(f"Text: {text}")
        #for letter in text:
         #   if letter == letters{letter}:



    
        
    
              

main()
