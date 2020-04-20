dictionary_list_of_words = {
    "banan": "banana",
    "pomarańcz": "orange",
    "książka": "book",
    "dziewczyna": "girl",
    "skuter": "scooter",
    'zasłony':'drapes'
}
def remove_word():
    klucz = input("jakie słowo chceszu usunąć?: ")
    if klucz in dictionary_list_of_words:
        return dictionary_list_of_words.pop(klucz)
        print("usunięto pomyślnie!")
    elif klucz not in dictionary_list_of_words:
        print("Nie ma takiego słowa jak: " ,klucz,", w słowniku")
        remove_word()
def add_word():
    klucz = input("podaj klucz (słowo) które chciałbyś zdefiniować(PL): ")
    definicja = input("podaj definicję(ENG): ")
    dictionary_list_of_words[klucz] = definicja
    print("dodano pomyślnie")
def update_word():
    klucz = input("jakie słowo chcesz z'updatet'ować?: ")
    if klucz in dictionary_list_of_words.keys():
        dictionary_list_of_words.update([(klucz, klucz)])
        print("zmieniono słowo w słowniku")
        print(dictionary_list_of_words)
    elif klucz not in dictionary_list_of_words:
        print("Nie ma takiego słowa jak: " ,klucz,", w słowniku")
        add_word()
print("1: Dodaj kolejne słowo")
print("2: Usuń kolejne słowo")
print("3: Zrób update słowa")
print("4: Zakończ")
options = input("Co chciałbyś zrobić ze słownikiem: ")
if (options == "1"):
    add_word()
elif(options == "2"):
     remove_word()
elif(options == "3"):
    update_word()
elif (options == "4"):
    print("zakańczam działanie programu")
    quit()
else:
    print("Nie wybrano żadnej opcji, wpisz poprawną liczbę z dostępnych opcji: ")