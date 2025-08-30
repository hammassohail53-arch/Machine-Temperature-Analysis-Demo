import socket
import time
import random

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 5555))

print("✅ Connected to monitoring server")

# Har 3 sec me machine apna "temperature" bhejti rahegi
while True:
    temperature = random.randint(50, 100)  # Fake machine temperature
    message = f"Temperature: {temperature} °C"
    client.send(message.encode())
    print("📤 Sent:", message)
    time.sleep(3)
