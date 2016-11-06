#!/usr/bin/env python2.7
import tempfile
import time

from SimpleCV import Display, Image, Camera


display = Display()
cam = Camera(1)
while not display.isDone():
    img = cam.getImage()
    img.save(display)
    if display.mouseLeft:
        _, filename = tempfile.mkstemp(suffix='.png')
        img.save(filename)
        img.drawText('Image saved: {}'.format(filename))
        img.save(display)
        time.sleep(3)
