#!/usr/bin/env python
# -*- coding: utf8  -*-

class GlapseMain:
    
    def startScreenShots(self, output, quality, interval):
        print 'GlapseMain: stating taking screenshots...'
        print 'Output folder: ' + str(output)
        print 'Quality: ' + str(quality)
        print 'Interval: ' + str(interval)
        
    def stopScreenShots(self):
        print 'GlapseMain: stopped taking screenshots...'
