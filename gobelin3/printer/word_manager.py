from string import ascii_lowercase

class InteractiveWordManager(object):

    def __init__(self):
        self.word_hoard = {char: [] for char in ascii_lowercase + ' '} 
        self.active_word = None
        
    def try_letter(self, letter):
        letter = letter.lower()
        if self.active_word:
            word_category = self.word_hoard[self.active_word.first_letter]
            if letter == self.active_word.current_letter:
                is_cleared = self.active_word.advance_letter_index()
                if is_cleared:
                    print "yay!"
                    self.remove_interactive_word(self.active_word)
                    self.change_active_word(None)
            elif letter == self.active_word.first_letter and self.active_word.current_letter_index == 1:
                current_word_index = word_category.index(self.active_word)
                self.change_active_word(word_category[current_word_index - 1])
            else:
                word_fragment = self.active_word.cleared_fragment + letter
                word_fragment_first_letter = word_fragment[0].lower()
                for w in self.word_hoard[word_fragment_first_letter]:
                    if self.is_match(word_fragment, w):
                        self.change_active_word(w)
                        self.active_word.advance_letter_index(i=len(word_fragment)-1)
                        return
                self.active_word.reset()
                self.active_word = None
        else:
            word_category = self.word_hoard[letter]
            if word_category:
                self.change_active_word(word_category[0])
                
    def change_active_word(self, new_word):
        if self.active_word:
            self.active_word.reset()
        if new_word:
            new_word.advance_letter_index()
        self.active_word = new_word
        
    def add_interactive_word(self, word):
        self.word_hoard[word.first_letter].append(word)

    def remove_interactive_word(self, word):
        self.word_hoard[word.first_letter].remove(word)
        
    def is_match(self, letters, word):
        if letters.lower() == word.text[:len(letters)].lower():
            return True
        else:
            return False