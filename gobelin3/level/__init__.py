import random

import libtcodpy as libtcod

import settings, printer

sample_texts = ["That's why she went into the caves. Always cresting the wave of the present like the cursor at the end of a line, no going back, only forward, uncovering each moment in incredulous suprise, but also with a kind of boredom, as the novelty of the future is constrained slowly by the vise of present circumstance creeping up upon it.",
                "how i long to go forward or back, or break the tyranny of the line completely, and move up or down the page with freedom. trampling what has already been read and stomping it to nonsense, or leaping forward to the future pages and creating such a vile terrain that the author will have to proceed in writing only treacherously.",
                "age comes upon my life with a rushing sound that freezes the possibilities that were presented to me as a child into a series of failed choices. a gorgon that moves only at one speed. how dare you read these pages and turn this story into stone as you go. the ugliness of committing it to your memory as if you took the story and threw it into a pit from which there is no escape.",
                "series serious serial aboard about above incredible increase incur"
                ]




class Level(object):

    def __init__(self, game):
        self.game = game
        self.foreground = libtcod.console_new(settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT)
        libtcod.console_set_default_background(self.foreground, libtcod.black)
        self.width, self.height = settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT
        
        
        self.printer_manager = printer.PrinterManager()
        
        
        
        for text in sample_texts[::-1]:
            new_printer = printer.Printer([], 1, 1, self.foreground)
            text_block = printer.typeset_text(text)
            for w in text_block:
                new_printer.add_word(w)
            new_printer.arrange_forme()
            self.printer_manager.add_printer(new_printer)
        self.printer_manager.reset_queue()
        
        
        
    def respond_to_player_input(self, player_action):
        if player_action == "test word":
            new_word = self.printer_manager.current_printer.add_word("yay")
            self.printer_manager.current_printer.add_interactive_word(new_word)
        elif player_action == "switch context":
            self.printer_manager.switch_printer()
        elif len(player_action) == 1: #lazy!
            self.printer_manager.try_letter(player_action)
            
        print player_action
        return
        
    def update_all(self):
        pass
    
    def render_all(self):
        self.printer_manager.print_current()
        
    def clear_all(self):
        self.printer_manager.clear_current()
