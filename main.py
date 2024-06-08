    #Counts the number of words
def count_words(text):
        word = text.split()
        print(len(word))
        
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
               

               
         


 



    


def main():
    
    
    letters = {}
    words = 0
    file_contents =[]

    # Counts the total number of words in a text
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    
        words = count_words(file_contents)

        letters = count_characters(file_contents)

        print(letters)

   
    
    
    # Counts the total number of each word and adds it to a dicctionary

    #for word in words:
     #   text = word.lower()
      #  text = text.split()
        
       # print(f"Text: {text}")
        #for letter in text:
         #   if letter == letters{letter}:



    
        
    
              

main()
