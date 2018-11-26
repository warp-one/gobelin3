import libtcodpy as libtcod

class Player(object):

    def __init__(self):
        pass

    def handle_keys(self):
        key = libtcod.console_check_for_keypress()  #real-time
        
        is_char = (key.vk == libtcod.KEY_CHAR)
        is_space = (key.vk == libtcod.KEY_SPACE)

        if is_char or is_space:
            letter = (chr(key.c) if key.c else key.vk)
            return letter
     
#        if key.vk == libtcod.KEY_ENTER and key.lalt:
#            libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())
        if key.vk == libtcod.KEY_ESCAPE:
            return "quit game"
        elif key.vk == libtcod.KEY_TAB:
            print libtcod.sys_get_last_frame_length()
        elif key.vk == libtcod.KEY_ENTER:
            return "test word"
        elif key.vk == libtcod.KEY_RIGHT:
            return "switch context"
            

            
