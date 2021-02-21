import random

print("Hello, welcome to HANGMAN")
class Game():
  def __init__(self):
    words = ['apple', 'peach', 'pineapple', 'cherry', 
         'pomegranate', 'blueberry', 'pear', 'watermelon', 
         'mandarin', 'grape', 'kiwi', 'banana'] 
 
    self.word = random.choice(words)
  
  def play(self):
    turns=10
    guesses=''
    while turns > 0: 
        failed = 0
        for char in self.word: 
            if char in guesses: 
                print(char+" ", end="")             
            else: 
                print("_"+" ", end="")
                failed += 1
        print("\n")         
        if failed == 0: 
            print("You Won! The word is:", self.word) 
            break  
        print("\n")            
        guess = input("Please enter a letter:").lower()
        if len(guess)==1 and guess!=" " :
            guesses += guess 
            if guess not in self.word:
                turns -= 1
                print("Wrong! You have", + turns, "more guesses")
            if turns == 0:
                print("GAME OVER")
        else:
          print("Input should be 1 letter!")
        
word=Game()
word.play()
