#!/usr/bin/env python
# -*- coding: utf-8  -*-

class Configuration:
	
	def __init__(self):
		self.version = 0.1
		self.dataDir = '/usr/share/glapse'
		self.libDir = '/usr/lib/glapse'
		self.binPath = '/usr/bin/glapse'
		self.langDir = '/usr/share/locale'
		
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

