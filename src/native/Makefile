install:
	mkdir -p /usr/lib/mozilla/native-messaging-hosts
	cp -a download_with_kget.json /usr/lib/mozilla/native-messaging-hosts/
	cp -a download_with_kget.py /usr/lib/mozilla/native-messaging-hosts/
	chmod +x /usr/lib/mozilla/native-messaging-hosts/download_with_kget.py
	chown root:root /usr/lib/mozilla/native-messaging-hosts/download_with_kget.py
	chown root:root /usr/lib/mozilla/native-messaging-hosts/download_with_kget.json

uninstall:
	rm /usr/lib/mozilla/native-messaging-hosts/download_with_kget.py
	rm /usr/lib/mozilla/native-messaging-hosts/download_with_kget.json
