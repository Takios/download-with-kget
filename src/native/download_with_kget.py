#!/usr/bin/python3 -u
import sys
import struct
import json

from pydbus import SessionBus


def get_message():
    raw_length = sys.stdin.buffer.read(4)
    if len(raw_length) == 0:
        sys.exit(0)

    message_length = struct.unpack('@I', raw_length)[0]
    message_content = sys.stdin.buffer.read(message_length).decode("utf-8")
    return json.loads(message_content)

def encode_message(message_content):
    encoded_content = json.dumps(message_content).encode('utf-8')
    encoded_length = struct.pack('@I', len(encoded_content))
    return {'length': encoded_length, 'content': encoded_content}

# Send an encoded message to stdout
def send_message(encoded_message):
    sys.stdout.buffer.write(encoded_message['length'])
    sys.stdout.buffer.write(encoded_message['content'])
    sys.stdout.buffer.flush()


try:
    bus = SessionBus()
    dbus_kget = bus.get('org.kde.kget', '/KGet')
# KGet will get started by dbus if it's not running so trying a second time could be successful.
except Exception:
    try:
        dbus_kget = bus.get('org.kde.kget', '/KGet')
    except Exception:
        send_message(encode_message("Could not connect to KGet. Is it running?\n"))
        sys.exit(1)

while True:
    message = get_message()
    dbus_kget.importLinks([message])
