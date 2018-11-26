import libtcodpy as libtcod

import settings, level, player

# FEATURE IDEAS
#
# Atmospheric effects: whenever printing to a specific console, multiply the
# color value by the pixel from a gif of water, clouds, lighting, etc.
#
# all words should be interactive. at worst they can play the sound of a foot
# on the cave floor or other some such small thing

class Game(object):

    the_map = None

    def __init__(self, w, h):
        self.width, self.height = w, h

        libtcod.console_set_custom_font(settings.FONT_IMG,
                libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_ASCII_INROW,
                )
        libtcod.console_init_root(self.width, self.height, 
                'the caves', False, renderer=libtcod.RENDERER_GLSL)
        libtcod.sys_set_fps(settings.LIMIT_FPS)

        self.current_level = level.Level(self)
        self.player = player.Player()
            
    def execute(self):
        while not libtcod.console_is_window_closed():
            self.current_level.update_all()
            self.current_level.render_all()
            libtcod.console_blit(self.current_level.foreground, 0, 0, 
                                 self.width, self.height, 0, 0, 0)
            libtcod.console_flush()
            self.current_level.clear_all()
            player_action = self.player.handle_keys()
            if player_action:
                self.current_level.respond_to_player_input(player_action)
            
            if player_action == "quit game":
                break

if __name__ == '__main__':
    game = Game(settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT)
    game.execute()
