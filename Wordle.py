import random

#wordslist.txt was taken from here https://gist.github.com/dracos/dd0668f281e685bad51479e5acaadb93
with open('wordslist.txt', 'r') as wordsFile:
    words = wordsFile.read().split('\n')


def Setup():
    print("This is Wordle")
    print("\t✅ - letter is the word and is in correct spot")
    print("\t🟨 - letter is the word and is not in the right spot")
    print("\t _ - letter is not in the word")
    print()

def main():
    Setup()
    hiddenWord = words[random.randint(0, len(words))]
    attempts = 5

    while (attempts > 0):
        guess = input("Enter Guess (5 Letter Word): ").lower()
        if (guess not in words): 
            print("Word not in word list, Try another word\n")
            continue

        if (guess == hiddenWord):
            print("Good Guess!!!")
            break
        else:
            result = ""
            for hiddenLetter, guessLetter in zip(hiddenWord, guess):
                if (hiddenLetter == guessLetter.lower()):
                    result += " ✅ "
                elif (guessLetter in hiddenWord):
                    result += " 🟨 "
                else:
                    result += " _ "

            print(result)
            print(f"{attempts -1} are left.\n")
        
        attempts -= 1
    
    if (attempts == 0): 
        print(f"All attempts were used, the word was {hiddenWord.upper()}.")
            
main()