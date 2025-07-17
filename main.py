# UDP To MIDI: Main

# ==================================================================== #

import socket
import mido
from datetime import datetime

# ==================================================================== #

MIDI_OUTPUT = mido.open_output(mido.get_output_names()[0])

UDP_IP = "0.0.0.0"
UDP_PORT = 5005
SOCKET = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
SOCKET.bind((UDP_IP, UDP_PORT))

# ==================================================================== #

def timed_print(text: str) -> None:
	now = datetime.now()
	formatted_now = now.strftime("%H:%M:%S")
	print(f"{formatted_now} - {text}")

# ==================================================================== #

def udp_to_dict(data) -> dict:
	# Attempt to convert the UDP string into a python dictionary
	try:
		return eval(data.decode())
	except:
		timed_print(f"An error occured in the eval(data.decode()) step with the following message:")
		print('\t', data.decode())
		return None

# ==================================================================== #

def send_midi_message(message: dict) -> None:
	try:
		midi_message = mido.Message(
			'note_on',
			channel = message["channel"],
			note = message["note"],
			velocity = message["value"]
		)

		timed_print(f"{midi_message}")
		MIDI_OUTPUT.send(midi_message)	
	except:
		timed_print("An error occured in processing the following UDP message:")
		print('\t', message)

# ==================================================================== #

def main():
	timed_print(f"Listening for UDP packets on {UDP_IP}:{UDP_PORT}...")

	while True:
		# Recieve UDP packet
		data, addr = SOCKET.recvfrom(1024)

		message = udp_to_dict(data)
		if message is None:
			continue
		
		send_midi_message(message)

# ==================================================================== #

if __name__ == "__main__":
	main()