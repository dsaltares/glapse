#!/usr/bin/env python
# -*- coding: utf8  -*-

import threading
import os
import time
import re

class GlapseMain:
    
    def __init__(self):
        self.outputDir = os.getenv('HOME')
        self.quality = 80
        self.interval = 10
        self.numDigits = 9
        self.currentShot = 0
        self.done = True
    
    def startScreenshots(self, output, quality, interval):
        print 'Starting taking screenshots...'
        print 'Output folder: ' + str(output)
        print 'Quality: ' + str(quality)
        print 'Interval: ' + str(interval)
        
        # Update attributes
        self.outputDir = output
        self.quality = quality
        self.interval = interval
        self.currentShot = 0
        
        # Start a thread to take screenshots
        self.done = False
        self.thread = threading.Thread(target = self._takeScreenshot)
        self.thread.start()
        
        
    def stopScreenshots(self):
        print 'Stopped taking screenshots.'
        self.done = True
        self.thread.join()
        
        
    def makeVideo(self, gui, inputFolder, outputFile, FPS):
        # Build ffmpeg command
        command = 'ffmpeg -r ' + str(FPS) + ' -i ' + inputFolder + os.sep + '%0' + str(self.numDigits) + 'd.jpg ' + outputFile
        
        print command
        
        # Create thread to run command
        videoThread = threading.Thread(target = self._makeVideoThread, args = (command, gui))
        videoThread.start()
    
    def getPossibleOverwrite(self, output):
        regex = re.compile('[0-9]{' + str(self.numDigits) + '}.jpg')
        
        for f in os.listdir(output):
            match = regex.match(f)
            if match != None:
                return True
        
        return False

    def _takeScreenshot(self):
        # Run until we're done
        while not self.done:
            # Build scrot command
            fileName = "%09d" % (self.currentShot)
            fileName = fileName + '.jpg'
            
            command = 'scrot -q ' + str(self.quality) + ' ' + self.outputDir + os.sep + fileName
            
            print 'Taking screenshot: ' + command + '...'
            
            os.system(command)
            
            # Schedule next screenshot
            print 'Scheduling next screenshot...'
            self.currentShot = self.currentShot + 1
            time.sleep(self.interval)

    def _makeVideoThread(self, command, gui):
        # Make call system
        os.system(command)
        
        # Change GUI status
        gui.onMakeVideoFinished()
