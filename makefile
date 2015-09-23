PREFIX ?= /usr
LIBINSTALLDIR ?= /lib

GLAPSELIBDIR = $(DESTDIR)$(PREFIX)$(LIBINSTALLDIR)/glapse

PACKAGES = glapse

all: compile
	@echo "Ready to install..."

compile:
	python -m compileall -q $(PACKAGES)
	-python -O -m compileall -q $(PACKAGES)

make-install-dirs:
	mkdir -p $(DESTDIR)$(PREFIX)/bin
	mkdir -p $(GLAPSELIBDIR)
	mkdir -p $(GLAPSELIBDIR)/glapseGUI
	mkdir -p $(GLAPSELIBDIR)/glapseControllers
	mkdir -p $(GLAPSELIBDIR)/data
	mkdir -p $(GLAPSELIBDIR)/data/glade
	mkdir -p $(GLAPSELIBDIR)/data/img
	mkdir -p $(DESTDIR)$(PREFIX)/share/pixmaps
	mkdir -p $(DESTDIR)$(PREFIX)/share/applications

uninstall:
	rm -f  $(DESTDIR)$(PREFIX)/bin/glapse
	rm -rf $(GLAPSELIBDIR)
	rm -f $(DESTDIR)$(PREFIX)/share/applications/glapse.desktop
	rm -f $(DESTDIR)$(PREFIX)/share/pixmaps/glapse-icon.png

install: install-target locale install-locale

install_no_locale: install-target

install-target: make-install-dirs
	install -m 644 glapse.py $(GLAPSELIBDIR)
	install -m 644 glapseGUI/*.py $(GLAPSELIBDIR)/glapseGUI/
	install -m 644 glapseControllers/*.py $(GLAPSELIBDIR)/glapseControllers/
	install -m 644 data/img/*.png $(GLAPSELIBDIR)/data/img/
	install -m 644 data/glade/*.glade $(GLAPSELIBDIR)/data/glade/
	install -m 644 data/glade/*.png $(GLAPSELIBDIR)/data/glade/
	install -m 644 data/img/glapse-icon.png $(DESTDIR)$(PREFIX)/share/pixmaps/glapse-icon.png
	install -m 644 data/glapse.desktop $(DESTDIR)$(PREFIX)/share/applications/
	install -m 755 glapse $(DESTDIR)$(PREFIX)/bin/


locale:
	msgfmt -c -v -o lang/es/LC_MESSAGES/glapse.mo po/es.po
	msgfmt -c -v -o lang/en/LC_MESSAGES/glapse.mo po/en.po
	msgfmt -c -v -o lang/de/LC_MESSAGES/glapse.mo po/de.po
	msgfmt -c -v -o lang/fr/LC_MESSAGES/glapse.mo po/fr.po
	msgfmt -c -v -o lang/ja/LC_MESSAGES/glapse.mo po/ja.po

install-locale:
	install -m 755 lang/es/LC_MESSAGES/glapse.mo $(DESTDIR)$(PREFIX)/share/locale/es/LC_MESSAGES
	install -m 755 lang/en/LC_MESSAGES/glapse.mo $(DESTDIR)$(PREFIX)/share/locale/en/LC_MESSAGES
	install -m 755 lang/de/LC_MESSAGES/glapse.mo $(DESTDIR)$(PREFIX)/share/locale/de/LC_MESSAGES
	install -m 755 lang/fr/LC_MESSAGES/glapse.mo $(DESTDIR)$(PREFIX)/share/locale/fr/LC_MESSAGES
	install -m 755 lang/ja/LC_MESSAGES/glapse.mo $(DESTDIR)$(PREFIX)/share/locale/ja/LC_MESSAGES


clean:
	-find . -name "*.py[co]" -exec rm -f {} \;
	find . -name "*~" -exec rm -f {} \;
	find po/* -depth -type d -exec rm -r {} \;

