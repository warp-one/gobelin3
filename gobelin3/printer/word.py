import string

import libtcodpy as libtcod  
                
class Line(object):

    def __init__(self, line_length):
        self.line_length = line_length
        self.words = []
        
    def add_word(self, word):
        if self.current_length + word.length < self.line_length:
            word.x = self.current_length + 1
            self.words.append(word)
            return self.words
        else:
            return False
            
    def empty_line(self):
        self.words = []
        
    @property
    def current_length(self):
        return sum([w.length for w in self.words]) + len(self.words)
        
        
class Word(object):

    def __init__(self, text, x, y, color, console):
        self.text = text
        self.x, self.y = x, y
        self.default_color = color
        self.console = console
        self.current_letter_index = 0
        self.completion_event = None
        self.current_effect = None
        
    def advance_letter_index(self, i=1):
        self.current_letter_index += i
        if self.current_letter_index >= self.num_letters:
            self.reset()
            return self.text
            
    def reset(self):
        self.current_letter_index = 0
        
    def print_word(self):
        if self.current_effect:
            base_color = self.current_effect.tick(self.default_color)
            if self.current_effect.time_left <= 0:
                self.current_effect = None
        else:
            base_color = self.default_color
        
        for i, letter in enumerate(self.text):
            if i < self.current_letter_index:
                letter_color = self.default_color + libtcod.dark_grey
            else:
                letter_color = base_color
                
            libtcod.console_set_default_foreground(self.console, letter_color)
            libtcod.console_put_char(self.console, 
                            self.x + i, self.y, letter, libtcod.BKGND_NONE)
                            
   
                            
    @property
    def current_letter(self):
        return self.text[self.current_letter_index].lower()
        
    @property
    def first_letter(self):
        return self.text[0].lower()
        
    @property
    def length(self):
        return len(self.text)
        
    @property
    def num_letters(self):
        return len(string.strip(self.text, string.punctuation))
        
    @property
    def cleared_fragment(self):
        return self.text[:self.current_letter_index]

        
