import random

import libtcodpy as libtcod

import word_manager, word_effects, cursor, word


def typeset_text(text_block):
    individual_words = text_block.split()
    for w in individual_words:
        yield w

        
class PrinterManager(object):
    def __init__(self, printers=[]):
        self.printers = printers
        self.current_printer = None
        
        self.printer_spawn_effect = word_effects.WordEffect, random.randint, (10, 30)
        
    def add_printer(self, printer):
        self.printers.append(printer)
        if len(self.printers) == 1:
            self.current_printer = printer
        
    def remove_printer(self, printer):
        self.printers.remove(printer)
        
    def switch_printer(self):
        self.current_printer.clear()
        self.current_printer = self.printers[self.current_printer_index - 1]
        
        pse = self.printer_spawn_effect
        self.current_printer.apply_effect_to_all_words(*pse)
        
    def print_current(self):
        if not self.printers:
            return
        self.current_printer.print_all_words()
        
    def clear_current(self):
        if not self.printers:
            return
        self.current_printer.clear()
        
    def try_letter(self, letter):
        self.current_printer.try_letter(letter)
        
    def reset_queue(self):
        self.current_printer = self.printers[0]
        
    @property
    def current_printer_index(self):
        return self.printers.index(self.current_printer)
        

class Printer(object):

    def __init__(self, text, x, y, console, w=30, h=30):
        self.text = text
        self.width, self.height = w, h
        self.x, self.y = x, y
        self.lines = []
        self.console = console
        self.cursor = cursor.Cursor(libtcod.CHAR_BLOCK3, 0, 0, libtcod.white, self.console)
        self.spacing = 2
        
        self.word_manager = word_manager.InteractiveWordManager()
        
    def set_width_and_height(self, w, h):
        self.width, self.height = w, h
        
    def arrange_forme(self):
        self.lines = [word.Line(self.width)]
        
        for w in self.text:
            if self.lines[-1].add_word(w):
                continue
            else:
                self.lines.append(word.Line(self.width))
                self.lines[-1].add_word(w)
                
        for i, line in enumerate(self.lines):
            for w in line.words:
                w.y = self.y + i*self.spacing
        last_line = self.lines[-1]
        last_word = last_line.words[-1]
        self.cursor.x = last_word.x + last_word.length
        self.cursor.y = last_word.y
        
    def instruct_printer(self, instruction):
        if instruction == "print all":
            self.print_all_words()
                
    def print_all_words(self):
        for w in self.text:
            w.print_word()
        self.cursor.print_word()

    def apply_effect_to_all_words(self, effect, duration_function, dfargs):
        for w in self.text:
            w.current_effect = effect(duration_function(*dfargs))
                
    def add_word(self, text):
        new_word = word.Word(text, 0, 0, libtcod.grey, self.console)
        self.text.append(new_word)
        self.arrange_forme()
        self.add_interactive_word(new_word)
        return new_word
        
    def clear(self):
        for x in range(self.width):
            for y in range(self.height):
                libtcod.console_put_char(self.console, 
                                x, y, ' ', libtcod.BKGND_NONE)
                                
    def try_letter(self, letter):
        self.word_manager.try_letter(letter)
        
    def add_interactive_word(self, w):
        self.word_manager.add_interactive_word(w)
        
                
        