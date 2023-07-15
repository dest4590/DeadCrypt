import socket
import threading
import base64

HOST = 'server_ip'
PORT = 4444

def crypt(text: str):
    # double encoding, xdd
    b85double = base64.b85encode(base64.b85encode(text.encode())) # bytes

    return base64.b64encode(b85double) # bytes

def handle_client(client_socket, addr):
    print(f'new client: {addr}')

    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        
        data = bytes(data).decode()
        
        try:
            dots_count = data.split(':', 1)[0]
            final_dots_count = data.split(':', 1)[1].split('@', 1)[0]

            if final_dots_count.count(':') == int(dots_count):
                client_socket.sendall(crypt('D3ADCR7PT_TRUE'))

        except Exception:
            client_socket.sendall("it's not as easy as it seems".encode())

    client_socket.close()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:

    server_socket.bind((HOST, PORT))

    server_socket.listen()


    while True:
        client_socket, addr = server_socket.accept()

        client_thread = threading.Thread(target=handle_client, args=(client_socket, addr))
        client_thread.start()
