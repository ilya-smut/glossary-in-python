from classes import Glossary

glossary = Glossary()

while True:
    word = input('Please, enter the word: ')
    #with open('output.txt', 'w') as f:
    #    f.write(glossary.get_and_build(word))
    glossary.get_and_print(word)

