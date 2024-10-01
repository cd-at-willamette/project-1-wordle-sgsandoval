########################################
# Name: Sonora
# Collaborators (if any):
# GenAI Transcript (if any):
# Estimated time spent (hr): too many... I will now be playing my wordle game in class because I've spent too much time on it to just abandon it.
# Description of any added extensions:
########################################

from WordleGraphics import *  # WordleGWindow, N_ROWS, N_COLS, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR, UNKNOWN_COLOR
from english import * # ENGLISH_WORDS, is_english_word
import random

def random_five_letter_word() -> str: #randomly shuffles words
        word = is_english_word
        random.shuffle(ENGLISH_WORDS)
        for word in ENGLISH_WORDS:
            if len(word) == 5:
                return word
        return "cloud" #my failsafe word, aka monday 9/30's wordle

def wordle():
    # The main function to play the Wordle game.
    import random
    
    answer_str = random_five_letter_word()

    def enter_action():
        current_row = gw.get_current_row()
        entered_word = ''.join(gw.get_square_letter(current_row, col) for col in range(5))
        print(entered_word, entered_word in ENGLISH_WORDS)
        if entered_word.lower() in ENGLISH_WORDS:
            gw.show_message("Well Done!")
            color_row(current_row, answer_str)
            if current_row < 5:  
                gw.set_current_row(current_row + 1)
            else:
                gw.show_message("You've used all attempts")
        else:
            gw.show_message("Not a Word")

    def color_row(row: int, answer: str):
        entered_word = ''.join(gw.get_square_letter(row, col) for col in range(5)).lower()
        remaining_answer_letters = list(answer.lower()) 
        colored_squares = [False] * 5

        # Color Green
        for col in range(5):
            letter = entered_word[col]
            if letter == remaining_answer_letters[col]:
                gw.set_square_color(row, col, CORRECT_COLOR)
                gw.set_key_color(letter, CORRECT_COLOR)
                colored_squares[col] = True  
                remaining_answer_letters[col] = None  

        # Color yellow
        for col in range(5):
            letter = entered_word[col]
            if not colored_squares[col]:  
                if letter in remaining_answer_letters:
                    letter_index = remaining_answer_letters.index(letter)
                    if letter_index is not None: 
                        gw.set_square_color(row, col, PRESENT_COLOR)
                        gw.set_key_color(letter, PRESENT_COLOR)
                        colored_squares[col] = True  
                        remaining_answer_letters[letter_index] = None  
        
        # Color gray
        for col in range(5):
            letter = entered_word[col]
            if not colored_squares[col]:
                gw.set_square_color(row, col, MISSING_COLOR)
                gw.set_key_color(letter, MISSING_COLOR)
    

    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)


# Startup boilerplate
if __name__ == "__main__":
    wordle()

