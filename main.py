def main():
    
    letters = {}
    words = 0
    
    # Counts the total number of words in a text
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        words = file_contents.split()
    
    print(len(words))

    # Counts the total number of each word and adds it to a dicctionary

    for word in words:
        text = word.lower()
        text = text.split("")
        
        print(text)

        #for letter in text:
         #   if letter == letters{letter}:



    
        
    
              

main()
