def main():
    vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
    string = input('Enter a word or sentence: ')
    output = ''
    
    for char in string:
        if char not in vowels:
            output += char  # append character if it's not a vowel

    print('twttr lingo:', output)

main()