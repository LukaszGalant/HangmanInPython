from random import randrange

#funkja zmieniająca n-ty znak w stringu
def replacer(inputstring, index, new_letter):
    chars = list(inputstring)
    chars[index] = new_letter
    returnstring = "".join(chars)
    return returnstring

#ladowanie pliku i split
file = open("C:\\Users\\lukas\\Desktop\\Python-projekt\\wisielec.txt", "r")
file_content = file.read()
word_list = file_content.split(",")
file.close()

#wybor losowego slowa
secret_word = word_list[randrange(10)]

###########
print("Psssst! Ukryte słowo to: " + secret_word)
print("Nie mów nikomu! \n\n\n")

#tworzenie słowa gdzie wszystkie litery są zamienione na "_"
hidden_secret = ""
for char in secret_word:
    hidden_secret += "_"

#tu ustaw ilość żyć
lives = 6
while lives > 0:
    print("Ukryte słowo: " + hidden_secret)
    
    #podaj literę
    guess = input("\nPodaj literę: ")

    #jeżeli trafion0
    if guess in secret_word:
        
        #to zamień wszystkie "_" na trafienia
        for j in range (0,len(secret_word)):
            if (secret_word[j]==guess):
                hidden_secret = replacer(hidden_secret,j,guess)
            j = j + 1
        print("Znaleziono!")

        #jeżeli odgadnięto wszystkie litery
        if not "_" in hidden_secret:
            lives = -1       

    else:
        #jeżeli nie trafiono w literę to zmiejsz ilość żyć
        lives = lives - 1
        print("Nie znaleziono! Pozostało " + str(lives) + " prób.")

if(lives == 0):
    print("Przegrana :( \nUkryte słowo to: " + secret_word)
else: #to zadziała tylko dla lives == -1
    print("wygrana :) \nUkryte słowo to: " + secret_word)
