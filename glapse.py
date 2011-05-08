#!/usr/bin/env python
# -*- coding: utf8  -*-


import gtk
import locale
import gettext
import os

# Translate strings like _('string')
from gettext import gettext as _

from glapseGUI import glapseGUI


# App name and i18n dir
APP = 'glapse'
LANG = os.path.join(os.path.dirname(__file__), 'lang')

# Get translation domain
gettext.textdomain(APP)
gettext.bindtextdomain(APP, LANG)
#gtk.glade.textdomain(APP)
#gtk.glade.bindtextdomain(APP, LANG)


# Set the locale to LANG, or the user's default
locale.setlocale(locale.LC_ALL, '')

def main():
    # Create main window and start application
    glapse = glapseGUI.GlapseMainGUI()
    if glapse.checkDependencies():
        glapse.window.show()
        gtk.gdk.threads_init()
        gtk.main()
    

if __name__ == "__main__":
	main()
