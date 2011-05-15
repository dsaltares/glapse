#!/usr/bin/env python
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

import gtk
import gtk.glade
import locale
import gettext
import os

from gettext import gettext as _

from glapseGUI import glapseGUI


# App name and i18n dir
APP = 'glapse'
LANG = os.path.join(os.path.dirname(__file__), 'lang')

# Set app translation domain
#gettext.bind_textdomain_codeset(APP, 'UTF-8')
locale.setlocale(locale.LC_ALL, '')
gettext.textdomain(APP)
gettext.bindtextdomain(APP, LANG)

# Set Glade translation domain
gtk.glade.textdomain(APP)
gtk.glade.bindtextdomain(APP, LANG)


def main():
    # Create main window and start application
    glapse = glapseGUI.GlapseMainGUI()
    if glapse.checkDependencies():
        glapse.window.show()
        gtk.gdk.threads_init()
        gtk.main()
    

if __name__ == "__main__":
	main()
