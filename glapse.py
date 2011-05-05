#!/usr/bin/env python
# -*- coding: utf8  -*-


import gtk

from glapseGUI import glapseGUI


def main():
    # Create main window and start application
    glapse = glapseGUI.glapseGUI()
    glapse.window.show()
    gtk.main()
    

if __name__ == "__main__":
	main()