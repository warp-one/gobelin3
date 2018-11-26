class WordEffect(object):
    def __init__(self, duration_in_frames):
        self.duration = duration_in_frames
        self.time_left = duration_in_frames
        
    def tick(self, color):
        self.time_left -= 1
        return color * (1 - (self.time_left * 1.)/self.duration)
