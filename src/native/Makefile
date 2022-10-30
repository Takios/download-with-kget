
libdir = /usr/lib64/mozilla/native-messaging-hosts
libdir64 = /usr/lib/mozilla/native-messaging-hosts
bindir = /usr/local/bin
manifest_file = download_with_kget.json


install:
	mkdir -p $(libdir)
	mkdir -p $(libdir64)
	mkdir -p $(bindir)
	cp -a $(manifest_file) $(libdir)/download_with_kget.json
	cp -a $(manifest_file) $(libdir64)/download_with_kget.json
	cp -a download_with_kget.py $(bindir)/download_with_kget_integration
	chmod +x $(bindir)/download_with_kget_integration
	chown root:root $(bindir)/download_with_kget_integration
	chown root:root $(libdir)/download_with_kget.json
	chown root:root $(libdir64)/download_with_kget.json

uninstall:
	rm $(bindir)/download_with_kget_integration
	rm $(libdir)/download_with_kget.json
	rm $(libdir64)/download_with_kget.json
