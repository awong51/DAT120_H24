import string

letters = string.ascii_lowercase
test_str = 'Dette er en test 123. STORE_og.små boksTaver'.lower()
resultat = ''
for letter in test_str:
    if letter not in string.ascii_lowercase:
        resultat += letter
        continue
    if letter in letters:
        resultat += letter
        letters = letters.replace(letter,'')


print(resultat)
