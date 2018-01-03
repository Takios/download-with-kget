MACHINE := $(shell uname -m)

ifeq ($(MACHINE), x86_64)
libdir = /usr/lib64/mozilla/native-messaging-hosts
manifest_file = download_with_kget.json_64
else
libdir = /usr/lib/mozilla/native-messaging-hosts
manifest_file = download_with_kget.json
endif


install:
	mkdir -p $(libdir)
	cp -a $(manifest_file) $(libdir)/download_with_kget.json
	cp -a download_with_kget.py $(libdir)/
	chmod +x $(libdir)/download_with_kget.py
	chown root:root $(libdir)/download_with_kget.py
	chown root:root $(libdir)/download_with_kget.json

uninstall:
	rm $(libdir)/download_with_kget.py
	rm $(libdir)/download_with_kget.json
