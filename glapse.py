#!/usr/bin/env python3
# -*- coding: utf-8  -*-

###############################################################################
# This file is part of gLapse.                                                #
#                                                                             #
# This program is free software: you can redistribute it and/or modify        #
# it under the terms of the GNU General Public License as published by        #
# the Free Software Foundation, either version 3 of the License, or           #
# any later version.                                                          #
#                                                                             #
# This program is distributed in the hope that it will be useful,             #
# but WITHOUT ANY WARRANTY; without even the implied warranty of              #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the               #
# GNU General Public License for more details.                                #
#                                                                             #
# You should have received a copy of the GNU General Public License           #
# along with this program.  If not, see <http://www.gnu.org/licenses/>.       #
#                                                                             #
# Copyright (C) 2011, David Saltares Márquez, <david.saltares@gmail.com>      #
###############################################################################
from gi.repository import Gtk
from gi.repository import Gdk

#from gi.repository import Gtk.glade
import locale
import gettext
import os
import os.path
import sys

from gettext import gettext as _

from glapseGUI import glapseGUI
from glapseControllers import configuration


# Idea taken from resistencia 2012 project (Pablo Recio Quijano)
if sys.platform == 'linux2':
    # Set process name.  Only works on Linux >= 2.1.57.
    try:
        import ctypes
        libc = ctypes.CDLL('libc.so.6')
        libc.prctl(15, 'glapse', 0, 0, 0)
    except:
        try:
             import dl
             libc = dl.open('/lib/libc.so.6')
             libc.call('prctl', 15, 'glapse\0', 0, 0, 0) # 15 is PR_SET_NAME
        except:
            pass

# Find out the location of glapses working directory, and insert it to sys.path
basedir = os.path.dirname(os.path.realpath(__file__))
if not os.path.exists(os.path.join(basedir, "glapse.py")):
    cwd = os.getcwd()
    if os.path.exists(os.path.join(cwd, "glapse.py")):
        basedir = cwd
sys.path.insert(0, basedir)

# General configuration
configuration = configuration.Configuration()

# App name and i18n dir
APP = 'glapse'
LANG = configuration.getLangDir()

# Set app translation domain
#gettext.bind_textdomain_codeset(APP, 'UTF-8')
locale.setlocale(locale.LC_ALL, '')
gettext.textdomain(APP)
gettext.bindtextdomain(APP, LANG)

# Set Glade translation domain
#Gtk.glade.textdomain(APP)
#Gtk.glade.bindtextdomain(APP, LANG)


def main():
    # Create main window and start application
    glapse = glapseGUI.GlapseMainGUI()
    if glapse.checkDependencies():
        glapse.window.show()
        Gdk.threads_init()
        Gtk.main()
    

if __name__ == "__main__":
    main()
