#!/usr/bin/env python
# -*- coding: utf8  -*-


import gtk

from glapseGUI import glapseGUI


def main():
    # Create main window and start application
    glapse = glapseGUI.GlapseMainGUI()
    if glapse.checkDependencies():
        glapse.window.show()
        gtk.gdk.threads_init()
        gtk.main()
    

if __name__ == "__main__":
	main()
