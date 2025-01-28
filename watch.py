#!/usr/bin/env python

import time
import sys


LINE_UP = '\033[1A'
LINE_CLEAR = '\x1b[2K'
TERMINAL_SIZE = 80


class AsciiVideo:
    """A class for ascii videos."""

    def __init__(self, ls, speed, left):
        """The initialiser for the class.

        Arguments:
            ls -- list of frames of the video;
            speed -- the speed of the video in Hz;
            left -- the left margin of the screen."""
        self.ls = ls
        self.speed = speed
        self.left = left
        self.size = self.get_size()[1]

    @classmethod
    def from_file(cls, filename):
        """Create a video from a text file."""
        ls = []
        speed = 1
        left = 5

        with open(filename, encoding='utf-8') as f:
            firstline = True
            header = False
            for line in f:
                if header:
                    if line.startswith('title='):
                        pass
                    elif line.startswith('speed='):
                        speed = float(line[6:-1])
                    elif line.startswith('left='):
                        left = int(line[5:-1])
                    else:
                        header = False
                elif firstline and line == 'ascii video\n':
                    header = True
                elif line == '\n':
                    ls.append([])
                else:
                    if len(ls) == 0:
                        ls.append([])
                    line = line.strip('\n')
                    if line.endswith(';'):
                        line = line[:-1]
                    ls[-1].append(line)

        return cls(ls, speed, left)
    
    def get_size(self):
        """Return the maximum size of the video in both dimensions."""
        ans = [0, 0]
        for img in self.ls:
            if len(img) > ans[0]:
                ans[0] = len(img)
            for line in img:
                if len(line) > ans[1]:
                    ans[1] = len(line)
        return ans
    
    def print_frame(self, index):
        """Print a frame #index of the video to the terminal."""
        img = self.ls[index]

        # `move n` -> move the screen `n` spaces to the right
        if len(img) == 1 and img[0].startswith('move ') and \
                not img[0].endswith(' '):
            times = int(img[0][5:])
            self.left = self.left + times
            if self.left < 0:
                self.left = TERMINAL_SIZE - self.size
            if self.left + self.size > TERMINAL_SIZE:
                self.left = 0

        # `sleep n` -> keep the current image for `n` frames
        elif len(img) == 1 and img[0].startswith('sleep ') and \
                not img[0].endswith(' '):
            times = int(img[0][6:])
            time.sleep(times / self.speed)

        # Anything else -> print a new frame
        else:
            for x in range(len(img)):
                print(' ' * self.left + img[x])
            time.sleep(1 / self.speed)
            for x in range(len(img)):
                print(LINE_UP, end=LINE_CLEAR)

    def show_once(self):
        """Play the video once."""
        for n in range(len(self.ls)):
            self.print_frame(n)

    def play(self):
        """Play the video for a long time."""
        try:
            print()
            for _ in range(10000):
                self.show_once()
        except KeyboardInterrupt:
            sys.exit()

    def __len__(self):
        """Return the length of the video in frames."""
        return len(self.ls)


if __name__ == '__main__':
    AsciiVideo.from_file(sys.argv[1]).play()
