# Simple access to the XL3 Streaming API.
# Requires XL3 API license option to be installed on the target meter.
# https://www.nti-audio.com/wp-content/uploads/download-manager-files/XL3-API-Manual.pdf

from websocket import create_connection  # pip install websocket-client

ConnectKey = "ZRZFA-SF2QT"   # Your Connect Key
url = "wss://connect.nti-audio.com/api/" + ConnectKey + "/stream2/"
ws = create_connection(url)
passwordPrompt = ws.recv()
ws.send(b'00000\n')   # Your password set on your XL3

identificationMessage = ws.recv()

print(identificationMessage)

command = f"SOH"
q = command + '\n'
ws.send(q)
print(f"Sent: {command}")
i = 0
while i < 4:
    i += 1
    print(f"Received ({i}): {ws.recv()}")
