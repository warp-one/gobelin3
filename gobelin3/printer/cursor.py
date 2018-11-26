import libtcodpy as libtcod

import word

class Cursor(word.Word):

    lighter_grey = libtcod.light_grey * 1.3

    def print_word(self):
        if self.default_color == libtcod.white:
            self.default_color = self.lighter_grey
        else:
            self.default_color = libtcod.white
        libtcod.console_set_default_foreground(self.console, self.default_color)
        libtcod.console_put_char(self.console, 
                        self.x, self.y, self.text, libtcod.BKGND_NONE)
        
