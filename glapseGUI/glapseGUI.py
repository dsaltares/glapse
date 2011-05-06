#!/usr/bin/env python
# -*- coding: utf8  -*-

import os
import gtk

class GlapseMainGUI:
    
    def __init__(self):
        # Get Builder
        builder = gtk.Builder()
        
        # Set path to find Glade file
        path = os.path.dirname(__file__) + '/../data/glade/glapseGUI.glade'
		
        # Build file from Glade file
        builder.add_from_file(path)
		
        # Get objects
	self.window = builder.get_object("wndGlapse")
	self.imgLogo = builder.get_object("imgLogo")
        self.btnScrOutput = builder.get_object("btnScrOutput")
	self.txtScrOutput = builder.get_object("txtScrOutput")
        self.spinScrQuality = builder.get_object("spinScrQuality")
        self.spinScrInterval = builder.get_object("spinScrInterval")
        self.btnScrStart = builder.get_object("btnScrStart")
        self.btnScrStop = builder.get_object("btnScrStop")
        self.btnVideoInput = builder.get_object("btnVideoInput")
	self.txtVideoInput = builder.get_object("txtVideoInput")
        self.btnVideoOutput = builder.get_object("btnVideoOutput")
	self.txtVideoOutput = builder.get_object("txtVideoOutput")
        self.spinVideoFPS = builder.get_object("spinVideoFPS")
        self.btnMakeVideo = builder.get_object("btnMakeVideo")
		
        # Connect signals
	builder.connect_signals(self)
	
	# Load logo
	self.imgLogo.set_from_file(os.path.dirname(__file__) + '/../data/img/glapse-icon-small.png')
	
	# Default spin buttons value
	self.spinScrInterval.set_value(10);
	self.spinScrQuality.set_value(80);
	self.spinVideoFPS.set_value(10);
	
	# Default path
	self.txtScrOutput.set_text(os.getenv('HOME') + '/glapse-screens')
	self.txtVideoInput.set_text(os.getenv('HOME') + '/glapse-screens')
	self.txtVideoOutput.set_text(os.getenv('HOME') + '/glapse-screens/timelapse.mpg')
	
    
    def onDestroy(self, widget):
		gtk.main_quit()
		
    def onBtnScrOutputClicked(self, widget):
	action =  gtk.FILE_CHOOSER_ACTION_SELECT_FOLDER
        buttons = (gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL, gtk.STOCK_SAVE, gtk.RESPONSE_OK)
	title = 'Screenshots output folder'

        chooser = gtk.FileChooserDialog(title = title, parent = None, action = action, buttons = buttons, backend = None)
        
	if chooser.run() == gtk.RESPONSE_OK:
            self.txtScrOutput.set_text(chooser.get_filename())
	
	chooser.destroy()
	
    def onBtnVideoInputClicked(self, widget):
	action =  gtk.FILE_CHOOSER_ACTION_SELECT_FOLDER
        buttons = (gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL, gtk.STOCK_SAVE, gtk.RESPONSE_OK)
	title = 'Video input folder'

        chooser = gtk.FileChooserDialog(title = title, parent = None, action = action, buttons = buttons, backend = None)
        
	if chooser.run() == gtk.RESPONSE_OK:
            self.txtScrOutput.set_text(chooser.get_filename())
	
	chooser.destroy()
	
    def onBtnVideoOutputClicked(self, widget):
	action =  gtk.FILE_CHOOSER_ACTION_SAVE
        buttons = (gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL, gtk.STOCK_SAVE, gtk.RESPONSE_OK)
	title = 'Video output file'

        chooser = gtk.FileChooserDialog(title = title, parent = None, action = action, buttons = buttons, backend = None)
        
	if chooser.run() == gtk.RESPONSE_OK:
            self.txtScrOutput.set_text(chooser.get_filename())
	
	chooser.destroy()
	
