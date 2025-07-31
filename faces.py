def convert(string):
    converted_text=string.replace(':)','🙂')
    converted_text= converted_text.replace(':(','🙁')
    return converted_text
    
    
def main():
    sentence=input('Enter a sentence')
    result=convert(sentence)
    print(result)

main()