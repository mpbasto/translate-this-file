from translate import Translator

# Adding constants
TO_LANGUAGE = 'pt'
FROM_FILEPATH = './test.txt'
TO_ FILEPATH = './test-pt.txt'

# Instanciating translator object
translator = Translator(to_lang=TO_LANGUAGE)

# Translating document
try:
    with open(FROM_FILEPATH, mode='r') as from_file:
        text = from_file.read()
        translation = translator.translate(text)
        with open(TO_ FILEPATH, mode='w') as to_file:
            to_file.write(translation)
except FileNotFoundError as e:
    print(f'{e}!\n Oh no, I couldn\'t find the file you asked for! Check your file path, silly billy!')
