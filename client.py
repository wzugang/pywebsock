from __future__ import print_function
import websocket

if __name__ == "__main__":
	websocket.enableTrace(True)
	#ws = websocket.create_connection("ws://echo.websocket.org/")
	ws = websocket.create_connection("ws://localhost/")
	print("Sending 'Hello, World'...")
	ws.send("subs")
	print("Sent")
	print("Receiving...")
	while True:
		result = ws.recv()
		print("Received '%s'" % result)
	ws.close()
