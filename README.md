Ascii video viewer
==================

A tool for viewing simple ascii animations in the terminal
written in Python.

Installation
------------

1. Make sure you have git and Python installed
2. `git clone` the repository to your computer
3. `cd` into the `ascii-video-viewer` directory

Watching a file
---------------

To run an ascii video stored in a file with the name `file.txt`

1. Go to the `ascii-video-viewer` directory
2. Run `python watch.py file.txt` and enjoy the animation!
3. To exit, press `Ctrl+C`

If you run `python watch.py file.txt` on a simple text file
(that does not have `ascii video` as the first line),
the file will appear one paragraph per slide with the speed
one slide per second.

Making an animation
-------------------

To create an animation, follow the following structure:

1. The first line should be `ascii video`
2. The first paragraph (except the first line above) should
consist of lines with one of the following structures:
    + `title=<anything>`, anything you want to say
    + `speed=<float>`, the speed of the animation in Hz (default 1)
    + `left=<int>`, the left margin of the screen (default 5)
3. An empty line
4. Frames and commands followed by empty lines

+ A frame is a paragraph, with lines ending with `;`
(optional, for visualisation of leading spaces)
+ A command may be the following:
    + `move n`, move `n` times to the right, `n` may be negative
    + `sleep n`, keep the current image for `n` frames
