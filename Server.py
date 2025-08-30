import socket
import threading

# Machine data ko store karne ke liye
machine_data = {}

# Broadcast sab clients ko nahi, sirf server pe log karna hai
def handle_client(client_socket, address):
    while True:
        try:
            # Machine (client) ka data receive karo
            data = client_socket.recv(1024).decode()
            if not data:
                break

            # Data ko save karo dictionary me
            machine_data[address] = data

            # Console pe print karo
            print(f"📡 Data from {address}: {data}")

        except:
            print(f"❌ Connection lost: {address}")
            client_socket.close()
            break

# Server setup
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("127.0.0.1", 5555))  # localhost
server.listen()

print("✅ Machine Monitoring Server started...")

while True:
    client_socket, addr = server.accept()
    print(f"🔗 Machine connected: {addr}")
    thread = threading.Thread(target=handle_client, args=(client_socket, addr))
    thread.start()
