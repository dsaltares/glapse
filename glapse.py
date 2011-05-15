#!/usr/bin/env python
# -*- coding: utf-8  -*-


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
