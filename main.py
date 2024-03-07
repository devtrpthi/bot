def main():
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()
        length = count_words(file_contents)
        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{length} were found in the document")
        letters = count_letters(file_contents)
        sorted_letters = sorted(letters.items(), key=lambda item: item[1], reverse=True)
        for char, count in sorted_letters:
            print(f"The '{char}' character was found {count} times")
        print("--- End report ---")


def count_words(text):
    words = text.split()
    return len(words)

def count_letters(text):
    result={}
    new_text = text.lower()
    for char in new_text:
        if char.isalpha():
            result[char] = result.get(char,0)+1
    list_of_dicts = [{key:value} for key, value in result.items()]
    return result


        
    
if __name__=="__main__":
    main()
