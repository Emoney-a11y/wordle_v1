from pathlib import Path
# Change 1 : Something must be initialized here
import random

word_file = Path("5-letter-words.txt")

# def find_word_file():
# 	if word_file.exists():
# 		return word_file
# 	else:
# 		print(" Error - File not found! :( ")

# Using a reference document approach
def load_word_bank(filename = word_file):
	with open(filename, "r") as file:
		return [word for word in (line.strip().lower() for line in file) if len(word) == 5]
    
# word_bank = load_word_bank()

def user_guess(word_bank):
    
    while True:
        guess = input("Enter a 5 letter word: ").strip().lower()
        if len(guess) != 5:
            print("You made a mistake, word submission must be 5 letters long. ")
        elif guess not in word_bank:
            print("That's not a real word. You should feel bad. ")
        else:
            return guess

def score_guess(guess: str, target: str):
	result = ["B"] * 5
	target_chars = list(target)
	
	for i in range(5):
		if guess[i] == target [i]:
			result[i] = "G"
			target_chars[i] = None
            
	for i in range (5):
		if result[i] == "B" and guess[i] in target_chars:
			result[i] = "Y"
			target_chars[target_chars.index(guess[i])] = None
		
	return result
def emoji_feedback(score):
    emoji_map = {"G": "🟩", "Y": "🟨", "B": "⬛️"} 
    return "".join(emoji_map[s] for s in score)

def print_legend():
    print("🟩 Correct position")
    print("🟨 Wrong position")
    print("🟧 Right/wrong position - but another copy of this letter is still hiding")
    print("⬛️ Not in word\n")
    
    
def main():
    print("Wordle Test Project (Emoji Board)\n")
    print_legend()
    words = load_word_bank(word_file)
    target = random.choice(words)
    board = []
    
    
    for attempt in range(1, 7):
        guess = user_guess(words)
        score = score_guess(guess, target)
        board.append(emoji_feedback(score))
        
        
        
        print("\nCurrent Board:")
        for row in board:
            print(row)
        print()
        
        
        if guess == target:
            print(f"You got it in {attempt} guess{'es' if attempt > 1 else ''}!")
            return
        
        
        
        
        
    print(f"Out of guesses. The word was: {target}")



#print(f"Your guess was {guess}, the word was {sample}")

if __name__ == "__main__":
	main()
 
 # the strip function removes whitespace from strings
    # the lower function makes all characters lowercase
    # not in allows us to compare strings within arrays
    # != means not equals
    
    
    
    
    
    
    
#  							does it work NO 
# 												 problem is still the main()