# glossary-in-python
A framework to create Dictionary in python. It can return transcription, definitions, links for pronunciation and examples for definitions of English words

## Uses FREE DICTIONARY API
https://dictionaryapi.dev/

## Classes

### Glossary

Glossary is a class which operates with a word given to it through new_word() method

It contains variables such as word, meanings, status, ready_for_request, phonetic, synonyms, antonyms
- word: word is obatained through new_word() and contains a string class is currently working with
- meanings: is a dictionary of definitions in a format {definition1: example1, ...}
- status: status becomes True when the response is obtained from API
- ready_for_request: is False at the moment when object is created. Becomes True when word is added through new_word()
- phonetic: is a dictionary in a format {transcription: link_for_audio}
- synonyms and antonyms are not currently used

It contains a number of methods:
- add_word(word) - replacing previous word Glossary worked with
- get() - sends request to an API. Obtains a responce and formats it.
- print() - prints formated data in terminal
- build_string() - returns a string of output same as in print(), which can be written into a file
- get_and_build(word) - unites add_word(word), get() and returns string as build_string()
- get_and_print(word) - same as get_and_build(word), but prints output in a termianl

