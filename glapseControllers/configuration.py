#!/usr/bin/env python
# -*- coding: utf-8  -*-

import os

class Configuration:
	
	def __init__(self):
		self.version = 0.1
		#self.dataDir = '/usr/share/glapse/data'
		#self.libDir = '/usr/lib/glapse'
		#self.binPath = '/usr/bin/glapse'
		#self.langDir = '/usr/share/locale'
		
		self.dataDir = os.path.realpath(os.path.join(os.path.dirname(__file__), '../data'))
		self.libDir = os.path.realpath(os.path.join(os.path.dirname(__file__), '../glapseControllers'))
		self.binPath = os.path.realpath(os.path.join(os.path.dirname(__file__), '../'))
		self.langDir = os.path.realpath(os.path.join(os.path.dirname(__file__), '../lang'))
		
	def getVersion(self):
		return self.version
	
	def getDataDir(self):
		return self.dataDir
	
	def getLibDir(self):
		return self.libDir
		
	def getBinPath(self):
		return self.binPath
		
	def getLangDir(self):
		return self.langDir

