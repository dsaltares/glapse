#!/usr/bin/env python
# -*- coding: utf8  -*-

import os
import gtk

from glapse import glapseMain

class GlapseMainGUI:
    
    def __init__(self):
	
	# Version
	self.version = 0.1
	
	print ''
	print 'gLapse v0.1 - Take screenshots, glue them together'
	print '=================================================='
	print ''
	
	print 'Initialising GUI...'
	
	# Get Builder
        builder = gtk.Builder()
        
        # Set path to find Glade file
        path = os.path.dirname(__file__) + '/../data/glade/glapseGUI.glade'
		
        # Build file from Glade file
        builder.add_from_file(path)
		
        # Get objects
	self.window = builder.get_object('wndGlapse')
	self.imgLogo = builder.get_object('imgLogo')
	self.lblStatus = builder.get_object('lblStatus')
        self.btnScrOutput = builder.get_object('btnScrOutput')
	self.txtScrOutput = builder.get_object('txtScrOutput')
        self.spinScrQuality = builder.get_object('spinScrQuality')
        self.spinScrInterval = builder.get_object('spinScrInterval')
        self.btnScrStart = builder.get_object('btnScrStart')
        self.btnScrStop = builder.get_object('btnScrStop')
        self.btnVideoInput = builder.get_object('btnVideoInput')
	self.txtVideoInput = builder.get_object('txtVideoInput')
        self.btnVideoOutput = builder.get_object('btnVideoOutput')
	self.txtVideoOutput = builder.get_object('txtVideoOutput')
        self.spinVideoFPS = builder.get_object('spinVideoFPS')
        self.btnMakeVideo = builder.get_object('btnMakeVideo')
	
	self.dlgDependenciesError = builder.get_object('dlgDependenciesError')
	self.aboutDlg = builder.get_object('aboutDlg')
		
        # Connect signals
	builder.connect_signals(self)
	
	# Get controller class
	self.controller = glapseMain.GlapseMain()
	
	# Load logo and icon
	self.imgLogo.set_from_file(os.path.dirname(__file__) + '/../data/img/glapse-icon-small.png')
	self.window.set_icon_from_file(os.path.dirname(__file__) + '/../data/img/glapse-icon-small.png')
	#self.aboutDlg.set_logo_icon_name(os.path.dirname(__file__) + '/../data/img/glapse-icon-small.png')
	
	# Default spin buttons value
	self.spinScrInterval.set_value(10);
	self.spinScrQuality.set_value(80);
	self.spinVideoFPS.set_value(10);
	
	# Default path
	self.txtScrOutput.set_text(os.getenv('HOME') + '/glapse-screens')
	self.txtVideoInput.set_text(os.getenv('HOME') + '/glapse-screens')
	self.txtVideoOutput.set_text(os.getenv('HOME') + '/glapse-screens/timelapse.mp4')
	
	# Disable stop screenshots
	self.btnScrStop.set_sensitive(False)
	
	print 'GUI Loaded.'
	
    
    def onDestroy(self, widget):
	
	print 'Closing gLapse...'
	
	gtk.main_quit()
		
    def onBtnScrOutputClicked(self, widget):
	action =  gtk.FILE_CHOOSER_ACTION_SELECT_FOLDER
        buttons = (gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL, gtk.STOCK_SAVE, gtk.RESPONSE_OK)
	title = 'Screenshots output folder'

        chooser = gtk.FileChooserDialog(title = title, parent = None, action = action, buttons = buttons, backend = None)
        chooser.set_current_folder(os.getenv('HOME'))
	
	if chooser.run() == gtk.RESPONSE_OK:
            self.txtScrOutput.set_text(chooser.get_filename())
	
	chooser.destroy()
	
    def onBtnVideoInputClicked(self, widget):
	action =  gtk.FILE_CHOOSER_ACTION_SELECT_FOLDER
        buttons = (gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL, gtk.STOCK_SAVE, gtk.RESPONSE_OK)
	title = 'Video input folder'

        chooser = gtk.FileChooserDialog(title = title, parent = None, action = action, buttons = buttons, backend = None)
	chooser.set_current_folder(os.getenv('HOME'))
        
	if chooser.run() == gtk.RESPONSE_OK:
            self.txtScrOutput.set_text(chooser.get_filename())
	
	chooser.destroy()
	
    def onBtnVideoOutputClicked(self, widget):
	action =  gtk.FILE_CHOOSER_ACTION_SAVE
        buttons = (gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL, gtk.STOCK_SAVE, gtk.RESPONSE_OK)
	title = 'Video output file'

        chooser = gtk.FileChooserDialog(title = title, parent = None, action = action, buttons = buttons, backend = None)
        chooser.set_current_name(os.getenv('HOME') + os.sep + 'timelapse.mp4')
	
	if chooser.run() == gtk.RESPONSE_OK:
            self.txtScrOutput.set_text(chooser.get_filename())
	
	chooser.destroy()
	
    def onBtnScrStartClicked(self, widget):
	# Get options
	output = self.txtScrOutput.get_text()
	quality = self.spinScrQuality.get_value()
	interval = self.spinScrInterval.get_value()
	
	# Disable start, enable stop
	self.btnScrStart.set_sensitive(False)
	self.btnScrStop.set_sensitive(True)
	
	# Set status
	self.lblStatus.set_text('Taking screenshots...')
	
	# Call controller
	self.controller.startScreenshots(output, quality, interval)
	
    def onBtnScrStopClicked(self, widget):
	# Disable stop, enable start
	self.btnScrStop.set_sensitive(False)
	self.btnScrStart.set_sensitive(True)
	
	# Set status
	self.lblStatus.set_text('Idle')
	
	# Call controller
	self.controller.stopScreenshots()
	
    def onBtnAboutClicked(self, widget):
	#Show about dialog
	self.aboutDlg.run()
	self.aboutDlg.hide()
	
    def onBtnMakeVideoClicked(self, widget):
	# Chanche status bar
	self.lblStatus.set_text('Creating video...')
	
	# Call controller
	self.controller.makeVideo(self, self.txtVideoInput.get_text(), self.txtVideoOutput.get_text(), self.spinVideoFPS.get_value())
	
    def onMakeVideoFinished(self):
	# Chanche status bar
	self.lblStatus.set_text('Idle')
    
    def isExecutable(self, filePath):
	return os.path.exists(filePath) and os.access(filePath, os.X_OK)
	
    def which(self, program):
	filePath, fileName = os.path.split(program)
	
	if filePath and self.isExecutable(program):
	    return True
	else:
	    for path in os.environ['PATH'].split(os.pathsep):
		exeFile = os.path.join(path, program)
		if self.isExecutable(exeFile):
		    return True
	
	return False
    
    def checkDependencies(self):
	# Check wether all dependencies are installed or not
	dependencies = ('ffmpeg', 'scrot')
	
	for dependence in dependencies:
	    if not self.which(dependence):
		self.dlgDependenciesError.set_markup(dependence + ' was not found')
		self.dlgDependenciesError.format_secondary_text('Pleasy, install the package and launch gLapse again')
		self.dlgDependenciesError.run()
		self.dlgDependenciesError.destroy()
		return False
	
	return True
		
