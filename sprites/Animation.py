class Animation:
    """
    Defines an animation. 
    """
    def __init__(self, start_row, num_frames, frame_duration, loop=False):
        self.start_row = start_row
        self.num_frames = num_frames
        self.frame_duration = frame_duration
        self.current_frame = 0
        self.time_elapsed = 0
        self.loop = loop
